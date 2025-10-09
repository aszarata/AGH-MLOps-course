import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = f".env.{environment}"
    load_dotenv(dotenv_path=env_file, override=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    with open("secrets.yaml", "r") as f:
        secrets = yaml.safe_load(f)
    for key, val in secrets.items():
        os.environ[key] = val

    settings = Settings(SECRET=os.environ.get("SECRET_VALUE"))

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("SECRET: ", settings.SECRET)
