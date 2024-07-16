from typing import List
from setuptools import setup,find_packages

hypen_e="-e ."
def get_packages(path)->List[str]:
    requirements=[]
    with open(path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements


setup(
    name="bank_churn_prediction",
    author="ehetsham",
    author_email="ehetsham.s@gmail.com",
    install_requires=get_packages("requirements.txt"),
    packages=find_packages()
)