from setuptools import setup, find_packages

setup(
    name='edsa-hackathon',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon model solution',
    long_description=open('README.md').read(),
    install_requires=[],
    url='https://github.com/jasonrobwebster/edsa-analyse-hackathon',
    author='Jason Webster',
    author_email='jason@explore-ai.net'
)