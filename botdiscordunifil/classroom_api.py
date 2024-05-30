import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
   "https://www.googleapis.com/auth/classroom.courses", 
   "https://www.googleapis.com/auth/classroom.coursework.students", 
   "https://www.googleapis.com/auth/classroom.announcements"
]

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
                    print("Token inválido ou expirado. Por favor, forneça um token válido.")
                    return None
        else:
            print("O Token não existe. Por favor, forneça um token válido.")
            return None
        return self.creds

class GoogleClassroomService:
    def __init__(self, creds):
        self.creds = creds
        self.service = build("classroom", "v1", credentials=self.creds)

    def list_courses(self, page_size=20):
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

if __name__ == '__main__':
    try:
        manager = GoogleClassroomManager()
        courses = manager.get_courses()
        if courses:
            for course in courses:
                print(course)
                coursework = manager.get_coursework(course.id)
                if coursework:
                    print("Atividades:")
                    for work in coursework:
                        print(f"- {work['title']}")
                else:
                    print("Nenhuma atividade encontrada.")
        else:
            print("Nenhum curso ativo encontrado.")
    except Exception as e:
        print(e)
