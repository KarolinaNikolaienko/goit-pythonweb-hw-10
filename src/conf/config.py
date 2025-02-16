class Config:
    DB_URL = "postgresql+asyncpg://postgres:python08@localhost:5432/contacts_app"
    JWT_SECRET = "pythonweb10"  # Секретний ключ для токенів
    JWT_ALGORITHM = "HS256"  # Алгоритм шифрування токенів
    JWT_EXPIRATION_SECONDS = 3600  # Час дії токена (1 година)


config = Config()
