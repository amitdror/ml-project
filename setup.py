from typing import List

from setuptools import find_packages, setup


def get_requirements(path) -> List[str]:
    """
    This function reads the requirements file and returns a list of requirements.
    """
    with open(path) as f:
        requirements = f.read().splitlines()
        requirements.remove('-e .')
        return requirements


setup(
    name='ml-project',
    version='0.0.1',
    author='Amit Dror',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
