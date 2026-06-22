import random
import string

def generate_password(length=12):
   
    characters = string.ascii_letters + string.digits
    
    
    password_list = [random.choice(characters) for _ in range(length)]
    
    random.shuffle(password_list)
    
    
    return "".join(password_list)


print(f"Generated Password: {generate_password(16)}")