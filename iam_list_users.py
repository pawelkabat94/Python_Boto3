#import modules and libraries

import boto3
from pprint import pprint

#open AWS Management Console
aws_management_console = boto3.session.Session(profile_name = "default")

#open IAM Console
iam_console = aws_management_console.client('iam')

#use boto3 documentation to get more info

for each in iam_console.list_users()['Users']:
    print(each["UserName"])



