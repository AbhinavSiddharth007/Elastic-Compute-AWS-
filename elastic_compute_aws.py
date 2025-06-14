import boto3
import time
from datetime import datetime

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

AMI_ID = 'ami-0c02fb55956c7d316' #ireland
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'your-key-name'
SECURITY_GROUP_ID = 'sg-xxxxxxxx'
USER_DATA_FILE = 'user_data.sh'


with open(USER_DATA_FILE, 'r') as f:
    user_data_script = f.read()

# Launching EC2
print("Launching EC2 instance...")
start_time = datetime.now()

instance = ec2.create_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[SECURITY_GROUP_ID],
    UserData=user_data_script,
)[0]

instance.wait_until_running()
instance.load()

end_time = datetime.now()
boot_time = (end_time - start_time).total_seconds()
print(f"EC2 instance started in {boot_time} seconds: {instance.id}")

# Create AMI
print("Creating AMI snapshot...")
image = instance.create_image(Name='hw1-ami-snapshot', NoReboot=True)
image.wait_until_exists()
print(f"AMI created: {image.id}")

# Launching the new EC2 from AMI
print("Launching EC2 instance from AMI...")
start_time_ami = datetime.now()

new_instance = ec2.create_instances(
    ImageId=image.id,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[SECURITY_GROUP_ID],
)[0]

new_instance.wait_until_running()
new_instance.load()

end_time_ami = datetime.now()
boot_time_ami = (end_time_ami - start_time_ami).total_seconds()
print(f"AMI EC2 started in {boot_time_ami} seconds: {new_instance.id}")

# Cleaning it up lol
print("Terminating instances and deleting AMI...")
instance.terminate()
new_instance.terminate()
instance.wait_until_terminated()
new_instance.wait_until_terminated()

client.deregister_image(ImageId=image.id)
print("Cleaned up all resources.")
