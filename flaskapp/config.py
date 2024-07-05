import os
# OpenAI API key
OPEN_AI_SECRET_KEY = os.environ.get("OPEN_AI_SECRET_KEY")

# Database (postgres) connection details
DB_PROTOCOL = os.environ.get("DB_PROTOCOL")
DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")
DB_IPADDRESS = os.environ.get("DB_IPADDRESS")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")