# Working with AWS

Last updated: 06.13.2020

## Purpose

The purpose of this document is to show how to work with AWS.

## Prerequisites

None

### Installation

#### Installing Python 3 on Windows
1. Download the executable for Python 3.8.0
[here](https://www.python.org/ftp/python/3.8.0/python-3.8.0-amd64.exe).
1. Run the executable.
1. Open up a terminal
1. Type `python3.8 --version`
1. The output should show you are running Python 3.8.0.
1. If you see a different version, you might have to set the **PATH** variable

#### Installing Python 3 on Fedora
1. Open up a terminal
4. sudo dnf install python3.8
1. Type `python3.8 --version`
1. The output should show you are running Python 3.8.0

### Instructions

#### Working with the AWS Command Line Interface (CLI)

1. Open up a terminal
1. Navigate to a directory where you plan on putting your
python virtual environments.

    :warning: You must always work out of a virtual environment.
    Virtual environments prevent you from corrupting
    your default system virtual environment and allow users to install different
    software for each virtual environment.

1. Run `python3.8 -m venv venv_aws`
1. To activate your virtual environment on **Windows**, you run
`./venv_aws/Scripts/activate`
1. To activate your virtual environment on **Fedora**, you run
`source ./venv_aws/bin/activate`
1. Run `python --version`.  This is the version of Python running in your
virtual environment.
1. Run `pip install --upgrade pip`
1. Run `pip list`.  This should list the modules currently installed in your
environment.  Notice how aws-shell is not present.
1. Run `pip install aws-shell`.  The command installs the latest **aws-shell** in the
virtual environment.
1. Run `pip list` to confirm **aws-shell** is installed.

:construction: Under Construction....
