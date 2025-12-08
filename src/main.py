from dotenv import load_dotenv
import os

# Загружаем переменные из файла .env
load_dotenv()

def print_author():
    # Читаем переменную AUTHOR из окружения и присваиваем её переменной author
    author = os.getenv("AUTHOR", "Неизвестно")
    print(f"Автор проекта: {author}")

# Проверка работы функции
if __name__ == "__main__":
    print_author()

print('Hello from repository!')
