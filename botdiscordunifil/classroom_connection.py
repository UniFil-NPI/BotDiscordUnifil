import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')

def main():
    if not API_KEY:
        print("Não tem chave de API.")
        return

    service = build('classroom', 'v1', developerKey=API_KEY)

    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print('Nenhum curso encontrado.')
    else:
        print('Cursos:')
        for course in courses:
            print(f'{course["name"]} ({course["id"]})')

if __name__ == '__main__':
    main()
