'''
Created on Jan 9, 2017

@author: root
'''
import boto3


def s3listing():
    client = boto3.client('s3')
    response = client.list_buckets()
    print(response)

#you create clients from the established session.  Helps speed things up a bit and can help prevent API call limits.
def get_aws_client(BotoSession, AWSService):
    boto_client = BotoSession.client(AWSService)
    return boto_client
def cfn_Stack(BotoSession, AWSService):
    return BotoSession.resource(AWSService)

def get_aws_session(AWSProfile, AWSRegion, AWSRemoteRoleARN=None):
    #Create AWS Session using local AWS Profile
    print('Creating boto session with AWS Profile: ' + AWSProfile + '\n')
    boto_session=boto3.session.Session(profile_name=AWSProfile)
    return boto_session
    
def main():  
    
    #create boto session
    boto_session=get_aws_session(AWSProfile= 'personal', AWSRegion='us-east-2')
    
    
    
    ############################## CREATE STACKS ##############################
    #create appropriate boto client for this transaction based on avaialble input from yaml file
    cfn_client=get_aws_client(BotoSession=boto_session, AWSService='cloudformation')
    cfn_resource = cfn_Stack(BotoSession=boto_session, AWSService='cloudformation')

    #client requires the template be a string, so read the input file and convert it to string
    with open ("generic-asg.json", "r") as myfile:
        templateAsString=myfile.read()
    
    
    ######## Create Stack ########
    
    print()
    print("Creating Generic ASG Stack: ")
    print()
    response=cfn_client.create_stack(StackName='hamed', TemplateBody=templateAsString, NotificationARNs=[], DisableRollback=False, TimeoutInMinutes=60)    
    print(response)

if __name__ == '__main__':
    main()
    
