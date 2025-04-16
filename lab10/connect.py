import psycopg2
from config import load_config

def connect(config):
    try:
        with psycopg2.connect(**config) as conn:
            print("✅ Успешное подключение к PostgreSQL")
            return conn
    except psycopg2.DatabaseError as error:
        print("❌ Ошибка подключения:", error)

if __name__ == "__main__":
    config = load_config()
    connect(config)
