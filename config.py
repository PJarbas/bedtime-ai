import os
from typing import Tuple

from openai import OpenAI
from together import Together
from pydantic_settings import BaseSettings
from dotenv import load_dotenv 

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class AppConfig(BaseSettings):
    """
    Application configuration settings.
    """

    llm_model: str = os.getenv("LLM_MODEL", "")
    base_url: str = os.getenv("BASE_URL", "")
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    image_model_key: str = os.getenv("TOGETHER_API_KEY", "")


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


def get_image_model_client() -> Together:
    """
    Get the image model client.
    Returns:
        Together: The image model client.
    """
    config = get_app_config()
    client = Together(api_key=config.image_model_key)
    return client
