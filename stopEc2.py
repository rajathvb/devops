import boto3
region = 'ap-south-1'
instances = ['i-048fd258aa22b71c2']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
    
