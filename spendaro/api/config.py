import os

# FastAPI configurations
DEBUG=os.environ.get('DEBUG', True)
API_PORT = os.environ.get('API_PORT', 8000)
API_DOCS_URL = os.environ.get('API_DOCS_URL', '/docs')

# Database configurations set as environment variables at the Docker level (see docker-compose.dev.yml)
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')
POSTGRES_DRIVER = 'postgresql+psycopg2'