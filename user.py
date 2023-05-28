from dataclasses import dataclass

from typing import List


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str


@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: List[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig