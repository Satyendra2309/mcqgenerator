from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Satyendra Golla',
    author_email='satyendrag2309@gmail.com' ,
    install_requires=[
        'openai', 'langchain', 'python-dotenv', 'streamlit', 'PyPDF2'],
    packages=find_packages()
)