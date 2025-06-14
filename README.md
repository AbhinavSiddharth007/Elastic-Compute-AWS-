# EC2 Auto Deployment and Snapshot Project

This project automates the deployment of an application (HW1) on AWS EC2, creates an AMI snapshot, launches a second EC2 instance from the AMI, measures boot times, and cleans up all created resources. The automation is implemented using the AWS SDK for Python (boto3).

## Project Contents

- `elastci_compute_aws.py`: Python script that performs the following steps:
  - Launch an EC2 instance using the Amazon Linux 2 base image.
  - Deploy the HW1 application using a user-data script.
  - Measure the EC2 instance startup time.
  - Create an AMI snapshot of the running instance.
  - Launch a new EC2 instance from the created AMI.
  - Measure the startup time of the new instance.
  - Terminate all created resources to avoid incurring charges.
- `user_data.sh`: Shell script executed automatically on EC2 instance startup to install dependencies and deploy the HW1 application.
- `README.md`: This file.

## Prerequisites

- AWS account with permissions to manage EC2 resources.
- AWS CLI configured on your local machine or environment variables set for authentication.
- Python 3.7 or higher installed.
- Boto3 installed (`pip install boto3`).

## Manual Setup (One-time)

Before running the script, perform the following setup in the AWS Management Console:

- Create an EC2 Key Pair for SSH access.
- Create a Security Group allowing inbound traffic on ports 22 (SSH) and 80 (HTTP).
- Note the Key Pair name and Security Group ID for use in the script.

## Usage

1. Update the variables in `ec2_hw1_deploy.py`:
   - Replace `KEY_NAME` with your EC2 Key Pair name.
   - Replace `SECURITY_GROUP_ID` with your Security Group ID.
   - Update the `user_data.sh` script if necessary to point to your HW1 application repository or deployment instructions.

2. Run the deployment script:

```bash
python elastci_compute_aws.py
