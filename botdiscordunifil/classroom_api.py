import os
import datetime
import asyncio
import ssl
import discord
from discord.ext import commands
from redis_cache import RedisCache  
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import certifi

SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses",
    "https://www.googleapis.com/auth/classroom.coursework.students",
    "https://www.googleapis.com/auth/classroom.announcements",
    "https://www.googleapis.com/auth/classroom.rosters",
    "https://www.googleapis.com/auth/classroom.profile.emails"
]

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
            print(f"Students for course {course_id}: {students}")
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
        self.redis_cache = RedisCache()

    async def cache_all_data(self):
        courses = self.get_courses(force_update=True)
        for course in courses:
            course_id = course.id
            self.get_students(course_id, force_update=True)
            self.get_coursework(course_id, force_update=True)
            await self.get_pendings(course_id, force_update=True)

    def get_students(self, course_id, force_update=False):
        if not force_update:
            students = self.redis_cache.get_cached_students(course_id)
            if students:
                return students

        students_data = self.service.list_students(course_id)
        if students_data:
            self.redis_cache.set_cached_students(course_id, students_data)
            return students_data
        return []

    def get_courses(self, force_update=False):
        if not force_update:
            courses = self.redis_cache.get_cached_courses()
            if courses:
                return [Course(course_data) for course_data in courses]

        courses_data = self.service.list_courses()
        if courses_data:
            self.redis_cache.set_cached_courses(courses_data)
            return [Course(course_data) for course_data in courses_data]
        return []

    async def get_courses_for_student(self, email):
        courses = self.service.list_courses()  
        student_courses = []
        
        for course_data in courses:
            course = Course(course_data)  
            students = self.get_students(course.id) 
            
            if any(student['profile']['emailAddress'].lower() == email.lower() for student in students):
                student_courses.append(course)  

        return student_courses


    def get_coursework(self, course_id, force_update=False):
        if not force_update:
            coursework = self.redis_cache.get_cached_coursework(course_id)
            if coursework:
                return coursework

        coursework_data = self.service.list_coursework(course_id)
        if coursework_data:
            self.redis_cache.set_cached_coursework(course_id, coursework_data)
            return coursework_data
        return []

    async def get_pendings(self, course_id, force_update=False):
        if not force_update:
            pendings = self.redis_cache.get_cached_pendings(course_id)
            if pendings:
                return pendings

        coursework_list = self.get_coursework(course_id)
        students = self.get_students(course_id)

        if not coursework_list or not students:
            return []

        pending_assignments = []

        for coursework in coursework_list:
            submissions_key = f"course_{course_id}_coursework_{coursework['id']}_submissions"
            if not force_update:
                submissions = self.redis_cache.get_cache(submissions_key)
            else:
                submissions = None

            if not submissions:
                submissions = await self._fetch_submissions(course_id, coursework['id'])
                self.redis_cache.set_cache(submissions_key, submissions, expiration=3600)

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

        self.redis_cache.set_cached_pendings(course_id, pending_assignments)
        return pending_assignments

    async def get_student_pendings_by_email(self, student_email):
        loop = asyncio.get_event_loop()
        courses = await loop.run_in_executor(None, self.get_courses)
        
        all_pending_assignments = []
        for course in courses:
            student = await loop.run_in_executor(None, self.service.get_student_by_email, course.id, student_email)
            if student:
                coursework_list = await loop.run_in_executor(None, self.get_coursework, course.id)
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
            return []

async def main():
    try:
        manager = GoogleClassroomManager()
        await manager.cache_all_data()  
        print("Cache carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar o cache: {e}")


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} está online e sincronizado!')


if __name__ == '__main__':
    bot.run(os.getenv('DISCORD_TOKEN'))
