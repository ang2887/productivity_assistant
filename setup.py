from setuptools import setup, find_packages

setup(
    name='productivity_assistant',
    version='1.0',
    description='A productivity assistant using LLaMA and Streamlit',
    author='Alena Docherty',
    author_email='ang2887@gmail.com',
    packages=find_packages(),
    install_requires=[
        'streamlit>=1.39.0',
        'llama-cpp-python==0.3.1',
        'python-dotenv==1.0.1',
        'psycopg2-binary==2.9.10',  # precompiled version for easier installation
    ],
    python_requires='>=3.11',
)
