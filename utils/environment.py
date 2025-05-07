# utils/environment.py
import os
from dotenv import load_dotenv

load_dotenv()

class Environment:
    def __init__(self, env=None):
        self.env = env or os.environ.get("TEST_ENV", "dev")

    def get_url(self):
        return os.getenv(f"{self.env.upper()}_URL")

    def get_username(self, role):
        return os.getenv(f"{self.env.upper()}_{role.upper()}_USERNAME")

    def get_password(self, role):
        return os.getenv(f"{self.env.upper()}_{role.upper()}_PASSWORD")

    def is_dev(self):
        return self.env == "dev"

    def is_prod(self):
        return self.env == "prod"