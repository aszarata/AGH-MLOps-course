import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from settings import Settings
from dotenv import load_dotenv


def test_settings_loaded_correctly_when_env_is_dev():
    mock_environment("dev")

    settings = Settings(SECRET="a")
    assert settings.ENVIRONMENT == "dev"
    assert settings.APP_NAME == "Development App"


def test_settings_loaded_correctly_when_env_is_test():
    mock_environment("test")

    settings = Settings(SECRET="a")
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "Testing App"


def test_settings_loaded_correctly_when_env_is_prod():
    mock_environment("prod")

    settings = Settings(SECRET="a")
    assert settings.ENVIRONMENT == "prod"
    assert settings.APP_NAME == "Production App"


def mock_environment(environment):
    env_file = f".env.{environment}"
    load_dotenv(dotenv_path=env_file, override=True)
