import boto3
region = 'ap-south-1'
instances = ['i-03b78cc30b6905c60','i-0ab5edfc6dc7a4aa9','i-04c9560a748cc0db5','i-0177ff99535ce5fac']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
