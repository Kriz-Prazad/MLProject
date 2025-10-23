from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->list[str]:
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name="MLProject",
    version="0.1",
    author="Kriz",
    author_email="krishnaprasad.r001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')   
)