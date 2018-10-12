# Python Framework

## Preface
---

* Purpose: API testing on Windows
* Author: Thomas Nguyen
* Date started: 2018/09/29

## Table of contents
---

This document will show you how to:

0. [Introduction](#Introduction)
1. [Prerequisites](#Prerequisites)
2. [Setup](#Setup)
3. [Running the program](#Running-the-program)
4. [Lexicon](#Lexicon)
5. [Sources](#Sources)

## Introduction
---

Hello,

This is a short API framework written in Python for Raspberry Pi.
Feel free to comment. Thank you in advance.

Sincerely,

Thomas Nguyen, thomas.ejob@gmail.com
https://www.linkedin.com/in/thomasquang
Personal projects code: https://github.com/yes4me

## Prerequisites
---

* Raspberry Pi B+
* Python 3.5.3
* install any needed module using pip

## Setup
---

Required:

* [Get ARM version](https://launchpad.net/ubuntu/xenial/armhf/chromium-chromedriver/65.0.3325.181-0ubuntu0.16.04.1)
e.g.: chromium-chromedriver_65.0.3325.181-0ubuntu0.16.04.1_armhf
* cmd: sudo python3 -m pip install --upgrade pip
* cmd: sudo python setup install

Files:
* .gitgnore: Git ignore patterns
* behave.ini: behave (~cucumber) configuration files
* README.MD: This readme file
* setup.cfg: linter "flake8" configuration
* setup.py: Python setup. run it using "python setup.py --help"

Fix git:
- nano .git/hooks/pre-commit
    ```
    #!/bin/sh
    flake8 .
    ```
- chmod +x .git/hooks/pre-commit

## Running the program
---

* Run all features - cmd: behave
* Run a specific feature - cmd: behave example.feature
* Run a specific scenario - cmd: behave --tags @basic-test
* Run a specific scenario and see print - cmd: behave --tags @basic-test --no-color
* Run the lint - cmd: flake8

## Lexicon
---

## Sources
---

* References:

    * [Python packages](https://pypi.org/)
    * [Python behave](https://behave.readthedocs.io/en/latest/)
    * [how to print with behave](https://stackoverflow.com/questions/25150404/how-can-i-see-print-statements-in-behave-bdd)
    * [Python lint flake8](http://flake8.pycqa.org/en/latest/user/configuration.html)
    * [Python Selenium](https://selenium-python.readthedocs.io/locating-elements.html)
    * [Open source license](https://choosealicense.com/)
