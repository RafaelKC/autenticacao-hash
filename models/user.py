import hashlib
import json
import uuid


class User:
    def __init__(self, nome, email, password):
        if len(nome) > 40:
            raise ValueError("Name must be less or equal than 40 characters")
        if len(email) > 80:
            raise ValueError("Email must be less or equal than 80 characters")
        if len(password) > 4:
            raise ValueError("Password must be less or equal than 4 characters")

        self.id = str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.password = hashlib.md5(password.encode('utf-8')).hexdigest()

    def save_user(self):
        json_user = json.dumps(self.__dict__)

        with open(f'users/{self.id}-{self.nome}.user.txt', 'w+', encoding='utf-8') as f:
            json.dump(json_user, f, ensure_ascii=False, indent=4)
