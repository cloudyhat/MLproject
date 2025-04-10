from setuptools import setup, find_packages
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    required = []
    with open(file_path) as file_obj:
        required = file_obj.readlines()
        required = [req.replace("\n", "")for req in required]
        if hyphen_e_dot in required:
            required.remove(hyphen_e_dot)
    return required

setup(
    name="MLproject",
    version="0.1.0",
    author="Cloudy",
    author_email="100142375+cloudyhat@users.noreply.github.com",
    description="A brief description of your ML project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="hhttps://github.com/cloudyhat/MLproject",
    packages=find_packages(),
    install_requires=[get_requirements("requirements.txt")],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)