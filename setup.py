from setuptools import find_packages,setup
from typing import List

def get_packages(file_path:str)->List[str]:
    '''
    all the libraries install using this function.
    '''
    HYPHEN_E_DOT = "-e."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(

name='ML_Project',
version='0.0.1',
author='ShreeSapkal',
author_email='sapkalbusiness471@gmail.com',
packages=find_packages(),
install_requires=get_packages('requirements.txt')   # ['pandas','numpy','seaborn']

)