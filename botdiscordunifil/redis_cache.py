import redis
import json
from datetime import date

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def set_cache(self, key, value, expiration=3600):
        try:
            # Converte o objeto 'date' em string antes de armazenar
            value_json = json.dumps(value, default=self.json_serializer)
            self.client.set(key, value_json, ex=expiration)
            print(f"Valor armazenado no cache com a chave: {key}")
        except Exception as e:
            print(f"Erro ao armazenar no cache: {e}")

    def get_cache(self, key):
        try:
            value_json = self.client.get(key)
            if value_json:
                return json.loads(value_json)
            else:
                print(f"Chave {key} não encontrada no cache.")
                return None
        except Exception as e:
            print(f"Erro ao recuperar do cache: {e}")
            return None
    def json_serializer(self, obj):
        """ Função auxiliar para serializar tipos complexos """
        if isinstance(obj, date):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    def clear_cache(self, key):
        try:
            self.client.delete(key)
            print(f"Chave {key} removida do cache.")
        except Exception as e:
            print(f"Erro ao remover do cache: {e}")

    def clear_all_cache(self):
        try:
            self.client.flushdb()
            print("Todos os dados do cache foram removidos.")
        except Exception as e:
            print(f"Erro ao limpar o cache: {e}")

    def get_cached_students(self, course_id):
        cache_key = f"course_{course_id}_students"
        return self.get_cache(cache_key)

    def set_cached_students(self, course_id, students_data, expiration=3600):
        cache_key = f"course_{course_id}_students"
        self.set_cache(cache_key, students_data, expiration)
        print(f"Students for course {course_id} cached.")

    def get_cached_courses(self):
        cache_key = "active_courses"
        return self.get_cache(cache_key)

    def set_cached_courses(self, courses_data, expiration=3600):
        cache_key = "active_courses"
        self.set_cache(cache_key, courses_data, expiration)

    def get_cached_coursework(self, course_id):
        cache_key = f"course_{course_id}_coursework"
        return self.get_cache(cache_key)

    def set_cached_coursework(self, course_id, coursework_data, expiration=3600):
        cache_key = f"course_{course_id}_coursework"
        self.set_cache(cache_key, coursework_data, expiration)

    def get_cached_pendings(self, course_id):
        cache_key = f"course_{course_id}_pendings"
        return self.get_cache(cache_key)

    def set_cached_pendings(self, course_id, pendings_data, expiration=3600):
        cache_key = f"course_{course_id}_pendings"
        self.set_cache(cache_key, pendings_data, expiration)
