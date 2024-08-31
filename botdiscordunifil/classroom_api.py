import os.path
import datetime
import asyncio
import ssl  
import google.auth.transport.requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import certifi
import httplib2

SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses", 
    "https://www.googleapis.com/auth/classroom.coursework.students", 
    "https://www.googleapis.com/auth/classroom.announcements",
    "https://www.googleapis.com/auth/classroom.rosters", 
    "https://www.googleapis.com/auth/classroom.profile.emails"
]

import ssl
import certifi

ssl_context = ssl.create_default_context(cafile=certifi.where())
ssl_context.minimum_version = ssl.TLSVersion.TLSv1_2

class GoogleClassroomAuthenticator:
    def __init__(self, token_path="token.json"):
        self.token_path = token_path
        self.creds = None

    def authenticate(self):
        if os.path.exists(self.token_path):
            print("O Token foi carregado com sucesso.")
            self.creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    print("O token foi gerado novamente.")
                    self.creds.refresh(Request())
                else:
                    print("Token inválido ou expirado.")
                    return None
        else:
            print("O Token não existe.")
            return None
        return self.creds

class GoogleClassroomService:
    def __init__(self, creds):
        self.creds = creds
        self.service = build("classroom", "v1", credentials=self.creds, cache_discovery=False)

    def list_courses(self, page_size=100):
        try:
            results = self.service.courses().list(pageSize=page_size).execute()
            courses = results.get("courses", [])
            active_courses = [course for course in courses if course.get('courseState') == 'ACTIVE']
            return active_courses
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def list_coursework(self, course_id):
        try:
            results = self.service.courses().courseWork().list(courseId=course_id).execute()
            coursework = results.get("courseWork", [])
            return coursework
        except HttpError as error:
            print(f"An error occurred while fetching coursework: {error}")
            return None

    def list_students(self, course_id):
        try:
            results = self.service.courses().students().list(courseId=course_id).execute()
            students = results.get("students", [])
            return students
        except HttpError as error:
            print(f"An error occurred while fetching students: {error}")
            return None

    def list_student_submissions(self, course_id, coursework_id):
        try:
            print(f"Fetching submissions for course_id: {course_id}, coursework_id: {coursework_id}")
            results = self.service.courses().courseWork().studentSubmissions().list(
                courseId=course_id,
                courseWorkId=coursework_id,
                pageSize=10
            ).execute()
            submissions = results.get("studentSubmissions", [])
            return submissions
        except HttpError as error:
            print(f"An error occurred while fetching submissions: {error}")
            return None

    def get_student_by_email(self, course_id, email):
        try:
            students = self.list_students(course_id)
            student = next((s for s in students if s['profile']['emailAddress'].lower() == email.lower()), None)
            return student
        except HttpError as error:
            print(f"An error occurred while fetching the student by email: {error}")
            return None

    def list_student_emails(self, course_id):
        try:
            students = []
            request = self.service.courses().students().list(courseId=course_id)
            while request is not None:
                response = request.execute()
                students.extend(response.get('students', []))
                request = self.service.courses().students().list_next(request, response)

            emails = [student['profile']['emailAddress'] for student in students]
            return emails
        except HttpError as error:
            print(f"An error occurred while fetching student emails: {error}")
            return None

class Course:
    def __init__(self, course_data):
        self.id = course_data.get("id")
        self.name = course_data.get("name")
        self.section = course_data.get("section")
        self.enrollment_code = course_data.get("enrollmentCode")
        self.course_data = course_data

    def __str__(self):
        return f"Course: {self.name}, Section: {self.section}, Enrollment Code: {self.enrollment_code}"

class GoogleClassroomManager:
    def __init__(self):
        self.authenticator = GoogleClassroomAuthenticator()
        self.creds = self.authenticator.authenticate()
        if not self.creds:
            raise Exception("Autenticação falhou.")
        self.service = GoogleClassroomService(self.creds)

    def list_student_emails(self, course_id):
        return self.service.list_student_emails(course_id)

    def get_courses(self):
        courses_data = self.service.list_courses()
        if courses_data:
            courses = [Course(course_data) for course_data in courses_data]
            return courses
        return []

    def get_coursework(self, course_id):
        coursework_data = self.service.list_coursework(course_id)
        if coursework_data:
            return coursework_data
        return []

    def get_students(self, course_id):
        students_data = self.service.list_students(course_id)
        if students_data:
            return students_data
        return []

    async def get_pendings(self, course_id):
        coursework_list = self.get_coursework(course_id)
        students = self.get_students(course_id)

        if not coursework_list or not students:
            print("Nenhuma tarefa ou aluno encontrado.")
            return []

        pending_assignments = []

        submission_tasks = [self._fetch_submissions(course_id, coursework['id']) for coursework in coursework_list]
        submissions_results = await asyncio.gather(*submission_tasks)

        for coursework, submissions in zip(coursework_list, submissions_results):
            due_date = coursework.get('dueDate')
            if due_date:
                due_date = datetime.date(due_date['year'], due_date['month'], due_date['day'])
                for submission in submissions:
                    if submission['state'] in ['NEW', 'CREATED']:
                        student = next((s for s in students if s['userId'] == submission['userId']), None)
                        if student:
                            pending_assignments.append({
                                "student_name": student['profile']['name']['fullName'],
                                "student_id": student['userId'],
                                "coursework_title": coursework['title'],
                                "due_date": due_date,
                                "course_id": course_id
                            })

        return pending_assignments

    async def get_student_pendings_by_name(self, student_name):
        courses = self.get_courses()
        if not courses:
            print("Nenhum curso ativo encontrado.")
            return []

        all_pending_assignments = []

        pending_tasks = [self.get_pendings(course.id) for course in courses]
        results = await asyncio.gather(*pending_tasks)

        for pending_assignments in results:
            if not pending_assignments:
                continue

            student_pendings = [
                pending for pending in pending_assignments 
                if student_name.lower() in pending['student_name'].lower()
            ]

            all_pending_assignments.extend(student_pendings)

        return all_pending_assignments

    async def get_student_pendings_by_email(self, student_email):
        courses = self.get_courses()
        if not courses:
            print("Nenhum curso ativo encontrado.")
            return []

        all_pending_assignments = []

        for course in courses:
            student = self.service.get_student_by_email(course.id, student_email)
            if student:
                coursework_list = self.get_coursework(course.id)
                submission_tasks = [self._fetch_submissions(course.id, coursework['id']) for coursework in coursework_list]
                submissions_results = await asyncio.gather(*submission_tasks)

                for coursework, submissions in zip(coursework_list, submissions_results):
                    due_date = coursework.get('dueDate')
                    if due_date:
                        due_date = datetime.date(due_date['year'], due_date['month'], due_date['day'])
                        for submission in submissions:
                            if submission['userId'] == student['userId'] and submission['state'] in ['NEW', 'CREATED']:
                                all_pending_assignments.append({
                                    "student_name": student['profile']['name']['fullName'],
                                    "student_email": student['profile']['emailAddress'],
                                    "coursework_title": coursework['title'],
                                    "due_date": due_date,
                                    "course_id": course.id,
                                    "course_name": course.name
                                })

        return all_pending_assignments

    async def _fetch_submissions(self, course_id, coursework_id):
        try:
            loop = asyncio.get_event_loop()
            submissions = await loop.run_in_executor(None, self.service.list_student_submissions, course_id, coursework_id)
            return submissions or []
        except Exception as error:
            print(f"An error occurred while fetching submissions: {error}")
            return []

async def main():
    try:
        manager = GoogleClassroomManager()
        courses = manager.get_courses()
        if not courses:
            print("Falha ao carregar os classrooms.")
            return
    except Exception as e:
        print(e)

if __name__ == '__main__':
    asyncio.run(main())
