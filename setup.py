from setuptools import setup,find_packages
from typing import List
# here we are declaring the variables for setup the functions



PROJECTNAME = "Housing Predictor"
VERSION = "0.0.1"
AUTHOR = "Shubham Mishra"
DESCRIPTION = "This is my machine learning project"
REQUIREMENT_FILE_NAME = "requirements.txt"

# this function is going to return 

def get_requirements_list()-> List[str]:
   with open(REQUIREMENT_FILE_NAME) as requirement_file:
      return requirement_file.readlines().remove("-e .")

setup(
    name= PROJECTNAME,
    version= VERSION,
    author= AUTHOR,
    description= DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()
)