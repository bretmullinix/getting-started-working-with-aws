# Working with AWS

Last updated: 06.13.2020

## Purpose

The purpose of this document is to show how to work with AWS.

## Prerequisites

### You must have an Amazon AWS Account

##### After you create your account, You must create a new IDM User

1. Click on **Services** menu
1. Click on **IAM** link
1. Click on the **Users** link on the left menu.
1. Click the **Add User** button
1. In the **User Name** text box, enter the user name
1. Under the **Access Type** section, select the checkbox **Progammatic Access**
1. Click the **Next: Permissions** button
1. Click the **Create Group** button
1. In the **Group Name** text box, enter **EC2Editor**
1. Give the group the **AmazonEC2FullAccess** policy
1. Click on the **Create Group** button
1. Click on the **Next: Tags** button
1. Click on the **Next: Review** button
1. Click on the **Create User** button
1. Click on the **Download .csv** button.

:warning: The downloaded .csv will be called **credentials.csv**.
Keep this file safe.  It contains your **AWS Access Key ID** and your
**AWS Secret Access Key**.  These keys can give any users access to your
environment and cost you money.

## Installation

### Installing Python 3 on Windows
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

## Instructions

#### Working with the AWS Command Line Interface (CLI)

1. Open up a terminal

1. export AWS_ACCESS_KEY_ID="<Your **Access Key Id** in your **credentials.csv**>"

1. export AWS_SECRET_ACCESS_KEY="Your **Secret Access Key Id** in your
**credentials.csv**>"

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

1. Run `pip install aws-shell==0.2.1`.  The command installs the **aws-shell** with
the version of **0.2.1** in the virtual environment.

1. Run `pip list` to confirm **aws-shell** is installed.

1. Configure the aws-shell environment:

      - Type **aws-shell**.  The **aws-shell** will launch.
      - Type **configure**.  You will be prompted for several values:
      
        - **AWS Access Key ID** = This is the **Access key ID** in your
        **credentials.csv** file. Do not enter any value as this is provided
        by your **AWS_ACCESS_KEY_ID** environment variable.
        
        - **AWS Secret Access Key** = This is the **Secret access key** in your
        **credentials.csv** file.  Do not enter any value as this is provided
        by your **AWS_SECRET_ACCESS_KEY** environment variable.
        
        - **Default region name** = This is the AWS Region the **aws-shell** will
        use by default. A listing of AWS regions are
        [described here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).
        
          Here are a couple of examples:
        
          1. **us-east-1** = Located in the US East Region in the state of Ohio.
          1. **us-west-1** = Located in the US West Region in the state of California.
          1. **eu-central-1** = Located in Frankfurt, Germany.
        
        - **Default output format** = This is the output format when running
        commands on the shell.  You do not have to enter a value here.

    You are now ready to start working with the **aws-shell**.

1. Run `ec2 describe-regions`

    The output provides all the details of the listed AWS Regions.
    
1. Run `.exit` to exit the **aws shell**
1. Run the following by replacing **us-east-1** with the AWS region you want to use:

    `aws ec2 describe-images --region "us-east-1" > images_in_my_region.txt` 
1. Open the file **images_in_my_region.txt** and search for an image.
1. Once you find the image you want to use, copy the **ImageId** to a safe location.
The **ImageId** can be used in Terraform to launch an AWS instance. The **ImageId** is
the same as the **ami**.Take a look at the
[terraform-for-beginners](../terraform-for-beginners) repo to start working
with Terraform and use the **ImageId** you found.