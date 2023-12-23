from setuptools import find_packages,setup

setup(
    name ="MCQ Generator",
    version = "0.0.1",
    author = "Soumalla Tarafder",
    author_email = "spumallatarafder@gmail.com",
    install_requires = ["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages = find_packages()
)