from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
   # this function wil return all the requirements
   requirements=[]
   with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.strip() for req in requirements]
    
    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)

   return requirements   




setup(
name='mlproject',
version='0.0.1',
author='Simriti',
author_email='Simritit@gmail.com',
packages=find_packages(), # consider src as a pacakge itselg find init file always 

#parameterz that are required are automatically installed
install_requires=get_requirements('requirements.txt')
)