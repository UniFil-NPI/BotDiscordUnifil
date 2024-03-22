from random import choice, randint 

def get_response(user_input: str) -> str:
        lowered: str = user_input.lower() 

        if lowered == '': 
                return "1"
        elif 'hello' in lowered:  
                return "Hello World!"
        else: 
                return "erro"
