from enum import Enum
from typing import Self

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(str, Enum):
    WEBKIT = 'webkit',
    FIREFOX = 'firefox',
    CHROMIUM = 'chromium',

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        env_nested_delimiter=".",
    )

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    # Добавили метод initialize
    @classmethod
    def initialize(cls) -> Self: # Возвращает экземпляр класса Settings
        # Указываем пути
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("browser_state.json")

        # Создаем директории, если они не существуют
        videos_dir.mkdir(exist_ok=True)  # Если директория существует, то игнорируем ошибку
        tracing_dir.mkdir(exist_ok=True)
        # Создаем файл состояния браузера, если его нет
        browser_state_file.touch(exist_ok=True) # Если файл существует, то игнорируем ошибку

        # Возвращаем модель с инициализированными значениями
        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file,
        )

# Инициализируем настройки
settings = Settings.initialize()

