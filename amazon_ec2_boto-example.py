# Author: James Campbell
# What: Amazon EC2 example
# Requirements: pip3 install boto3 awscli and run aws configure

try:
    import boto3
except:
    exit('do "pip3 install boto" and "pip3 install awscli" first')

ec2 = boto3.client("ec2")
response = ec2.describe_instances()
print(response)
