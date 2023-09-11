from setuptools import setup, find_packages

def get_requirements(filepath):
    requirements = []
    with open(filepath,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements

setup(

    name = "DataScienceProject",
    version = '0.0.1',
    author = "Zahid Hussain",
    author_email = "zahid.dsu@gmail.com",
    packages = find_packages(),
    requirements = get_requirements("Requirements.txt") 
)
