import setuptools


with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python_selenium_framework',
    version='1.0.0',
    author='Thomas Nguyen',
    author_email="thomas.ejob@gmail.com",
    description='Selenium framework for Python',
    long_description=long_description,
    packages=setuptools.find_packages(),
)
