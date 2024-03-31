from setuptools import setup

with open("README.md", "r", encoding= 'utf-8') as fh:
    long_description=fh.read()
    
AUTHOR_NAME='NAVYA'
SRC_REPO='src'
LIST_OF_REQUIREMENTS=['numpy','pandas','streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='charankulal0241@gmail.com',
    description=('This is a collection of Python scripts for data analysis and visualization of movie recommendation system'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_version='>=3.9',
    install_requires=LIST_OF_REQUIREMENTS,
)