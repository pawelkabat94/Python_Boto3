import boto3

aws_management_console = boto3.session.Session(profile_name = "default")
#resource
iam_conosle_resource = aws_management_console.resource('iam')
#client
iam_conosle_client = aws_management_console.client('iam')


for each_user in iam_conosle_resource.users.all():
    print(each_user.name)

for each in iam_conosle_client.list_users()['Users']:
    print(each['UserName'])


#import boto3
#dir(aws_management_console)
#print(aws_management_console.get...())