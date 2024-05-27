import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/classroom.courses.readonly"]

def get_classroom_courses():
    """Fetches the first 10 courses the user has access to from the Google Classroom API."""
    creds = None
    if os.path.exists("token.json"):
        print("O Token foi carregado com sucesso.")
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        print("O Token não existe ou foi expirado.")
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("classroom", "v1", credentials=creds)
        results = service.courses().list(pageSize=20).execute()
        courses = results.get("courses", [])
        return courses

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

if __name__ == '__main__':
    courses = get_classroom_courses()
    if courses:
        for course in courses:
            print(course["enrollmentCode"])
    else:
        print("Nenhum curso encontrado.")
