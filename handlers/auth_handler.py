import os

from dotenv import load_dotenv
from vkbottle import UserAuth


async def save_token_via_credentials(login: str, password: str):
    try:
        token = await UserAuth().get_token(login, password)
        with open(".env", "w") as env_file:
            env_file.write(f"TOKEN=\"{token}\"")
        print("Токен успешно сохранен в файле .env")
    except Exception as e:
        print(f"Не удалось получить токен: {e}")
        print("Проверьте правильность введенных данных")
        print("Либо посетите https://vkhost.github.io/")
        print("И авторизируйтесь напрямую через токен")
        exit(0)


def save_token(token: str):
    with open(".env", "w") as env_file:
        env_file.write(f"TOKEN=\"{token}\"")
    print("Токен успешно сохранен в файле .env")
    

def get_token() -> str:
    load_dotenv()
    token = os.getenv("TOKEN")
    if token is None:
        raise ValueError("Токен не найден в файле .env.")
    return token
