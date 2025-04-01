from typing import Tuple

from openai import OpenAI
from pydantic import Field
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """
    Application configuration settings.
    """

    llm_model: str = Field("qwen/qwen-vl-plus:free", description="LLM model to use")
    base_url: str = Field(None, description="Base URL for the LLM API")
    api_key: str = Field(None, description="API key for the LLM API")

    class Config:
        """
        Configuration settings for the AppConfig class.
        """

        extra = "allow"
        env_file = ".env"  # Optional: Use .env file to load settings


def get_app_config() -> AppConfig:
    """
    Load config and prompt user if settings are missing.

    Returns:
        AppConfig: The application configuration settings.
    """
    config = AppConfig()
    return config


def get_llm_client() -> Tuple[OpenAI, str]:
    """
    Get the OpenAI client.

    Returns:
        Tuple[OpenAI, str]: A tuple containing the OpenAI client and the LLM model name.
    """
    config = get_app_config()

    model = config.llm_model

    client = OpenAI(base_url=config.base_url, api_key=config.api_key)
    return client, model
