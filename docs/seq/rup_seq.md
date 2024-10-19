									Bot de Discord
# Diagrama de Sequência
 
#### Histórico da Revisão
| Data   | Versão       | Descrição  |  Autor  |
| :---------- | :--------- | :-------------------------------- | :-------------------------------- |
| 20/05/2024 | 1.0 | Criação do Doc.| Gabriel Zanoni(@GbrielZanoni) |
| 21/05/2024 | 1.1 | Conversão para M.D| Gabriel Zanoni(@GbrielZanoni)|
| 30/05/2024 | 1.2 | Diagrama Refeito  | Gabriel Zanoni(@GbrielZanoni)|
| 22/08/2024 | 1.3 | Diagrama Refeito  | Gabriel Zanoni(@GbrielZanoni)|
| 19/10/2024 | 1.4 | Diagrama Refeito  | Gabriel Zanoni(@GbrielZanoni)|


![AS-IS](https://i.imgur.com/J6kMj7S.png)

```python
@startuml
Usuário -> Bot: /courses
Bot -> GoogleClassroomManager: get_courses_for_student(discord_id)
GoogleClassroomManager -> Bot: get_student_by_discord_id(discord_id)
Bot -> API: request student email by discord_id
API -> Bot: return student email

alt Email Obtido
  GoogleClassroomManager -> RedisCache: get_cached_courses(student_email)
  alt Dados no Cache
    RedisCache -> GoogleClassroomManager: return courses
    GoogleClassroomManager -> Bot: return courses
    Bot -> Usuário: show courses
  else Dados não no Cache
    RedisCache -> RedisCache: print "Chave active_courses não encontrada no cache."
    GoogleClassroomManager -> GoogleClassroomAuthenticator: authenticate()
    GoogleClassroomAuthenticator -> GoogleClassroomAuthenticator: check token
    GoogleClassroomAuthenticator -> GoogleClassroomAPI: request token
    GoogleClassroomAPI -> GoogleClassroomAuthenticator: return token
    GoogleClassroomAuthenticator -> GoogleClassroomManager: return creds
    GoogleClassroomManager -> GoogleClassroomService: new GoogleClassroomService(creds)
    GoogleClassroomManager -> GoogleClassroomService: list_courses(student_email)
    GoogleClassroomService -> GoogleClassroomAPI: get courses
    GoogleClassroomAPI -> GoogleClassroomService: return courses
    GoogleClassroomService -> GoogleClassroomManager: return courses
    GoogleClassroomManager -> RedisCache: set_cached_courses(student_email, courses)
    RedisCache -> RedisCache: print "Valor armazenado no cache com a chave: active_courses"
    GoogleClassroomManager -> Bot: return courses
    Bot -> Usuário: show courses
  end
else Email Não Obtido
  GoogleClassroomManager -> Bot: return "Você não está registrado."
  Bot -> Usuário: show "Você não está registrado."
end

Usuário -> Bot: /tasks <course_id>
Bot -> GoogleClassroomManager: get_coursework(student_email, course_id)
GoogleClassroomManager -> RedisCache: get_cached_coursework(student_email, course_id)
alt Dados no Cache
  RedisCache -> GoogleClassroomManager: return coursework
  GoogleClassroomManager -> Bot: return coursework
  Bot -> Usuário: show coursework
else Dados não no Cache
  RedisCache -> RedisCache: print "Chave course_<course_id>_coursework não encontrada no cache."
  GoogleClassroomManager -> GoogleClassroomService: list_coursework(course_id)
  GoogleClassroomService -> GoogleClassroomAPI: get coursework
  GoogleClassroomAPI -> GoogleClassroomService: return coursework
  GoogleClassroomService -> GoogleClassroomManager: return coursework
  GoogleClassroomManager -> RedisCache: set_cached_coursework(student_email, course_id, coursework)
  RedisCache -> RedisCache: print "Valor armazenado no cache com a chave: course_<course_id>_coursework"
  GoogleClassroomManager -> Bot: return coursework
  Bot -> Usuário: show coursework
end

Usuário -> Bot: /calendar
Bot -> GoogleClassroomManager: get_courses_for_student(discord_id)
GoogleClassroomManager -> Bot: get_student_by_discord_id(discord_id)
Bot -> API: request student email by discord_id
API -> Bot: return student email

alt Email Obtido
  GoogleClassroomManager -> RedisCache: get_cached_courses(student_email)
  alt Dados no Cache
    RedisCache -> GoogleClassroomManager: return courses
    GoogleClassroomManager -> Bot: return courses
    Bot -> Usuário: show courses
  else Dados não no Cache
    RedisCache -> RedisCache: print "Chave active_courses não encontrada no cache."
    GoogleClassroomManager -> GoogleClassroomService: list_courses(student_email)
    GoogleClassroomService -> GoogleClassroomAPI: get courses
    GoogleClassroomAPI -> GoogleClassroomService: return courses
    GoogleClassroomService -> GoogleClassroomManager: return courses
    GoogleClassroomManager -> RedisCache: set_cached_courses(student_email, courses)
    RedisCache -> RedisCache: print "Valor armazenado no cache com a chave: active_courses"
    GoogleClassroomManager -> Bot: return courses
  end

  Bot -> GoogleClassroomManager: get_coursework(student_email, course_id)
  GoogleClassroomManager -> RedisCache: get_cached_coursework(student_email, course_id)
  alt Dados no Cache
    RedisCache -> GoogleClassroomManager: return coursework
    GoogleClassroomManager -> Bot: return coursework
    Bot -> Usuário: show calendar
  else Dados não no Cache
    RedisCache -> RedisCache: print "Chave course_<course_id>_coursework não encontrada no cache."
    GoogleClassroomManager -> GoogleClassroomService: list_coursework(course_id)
    GoogleClassroomService -> GoogleClassroomAPI: get coursework
    GoogleClassroomAPI -> GoogleClassroomService: return coursework
    GoogleClassroomService -> GoogleClassroomManager: return coursework
    GoogleClassroomManager -> RedisCache: set_cached_coursework(student_email, course_id, coursework)
    RedisCache -> RedisCache: print "Valor armazenado no cache com a chave: course_<course_id>_coursework"
    GoogleClassroomManager -> Bot: return coursework
    Bot -> Usuário: show calendar
  end
else Email Não Obtido
  GoogleClassroomManager -> Bot: return "Você não está registrado."
  Bot -> Usuário: show "Você não está registrado."
end
@enduml
``` 