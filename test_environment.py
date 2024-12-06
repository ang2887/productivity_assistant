# test_environment.py 1

import os
from dotenv import load_dotenv

load_dotenv()

# test environment-specific variables
print('*** Environment check ***')
print(f"IS_DOCKER: {os.getenv('IS_DOCKER')}")
print(f"DATABASE_URL: {os.getenv('DATABASE_URL')}")
print(f"DATABASE_URL_DOCKER: {os.getenv('DATABASE_URL_DOCKER')}")
print(f"DATABASE_URL_LOCAL: {os.getenv('DATABASE_URL_LOCAL')}")
print(f"MODEL_PATH_DOCKER: {os.getenv('MODEL_PATH_DOCKER')}")
print(f"MODEL_PATH_LOCAL: {os.getenv('MODEL_PATH_LOCAL')}")

# which values being used
database_url = (
    os.getenv('DATABASE_URL') or
    os.getenv('DATABASE_URL_DOCKER') if os.getenv('IS_DOCKER') == '1' else
    os.getenv('DATABASE_URL_LOCAL')
)
model_path = (
    os.getenv('MODEL_PATH_DOCKER') if os.getenv('IS_DOCKER') == '1' else
    os.getenv('MODEL_PATH_LOCAL')
)

print('*** Finalised values ***')
print(f'Finalised DATABASE_URL: {database_url}')
print(f'Finalised MODEL_PATH: {model_path}')

# validate the paths and connections
if not database_url:
    print('Error: No valid DATABASE_URL found. Please check your .env or .env.docker file')
else:
    print('Database URL is valid.')

if not model_path:
    print('Error: No valid MODEL_PATH found. Please check your .env or .env.docker file')
elif not os.path.exists(model_path):
    print(f'Error: Model path does not exist: {model_path}')
else:
    print('Model path is valid.')

print('\nEnvironment check completed')
