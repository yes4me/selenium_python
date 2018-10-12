import os
import setuptools



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name='python_selenium_framework',
    version='1.0.0',
    author='Thomas Nguyen',
    author_email="thomas.ejob@gmail.com",
    url='https://github.com/yes4me',
    license='GNU GPLv3',
    description='Selenium framework for Python',
    long_description=read('README.MD'),
    platforms=['Raspberry Pi 3B+'],
    packages=setuptools.find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'behave',
        'selenium'
    ],
)
