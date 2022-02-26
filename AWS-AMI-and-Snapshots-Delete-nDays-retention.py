####################################################################################
#   AWS Lambda function which deletes Images which has creation date older than
#   retention date.
#
#
####################################################################################
import boto3
import os
from datetime import datetime, timedelta, timezone
retention = 120
region = "ap-south-1"
start_date = str(datetime.now(tz=timezone.utc) - timedelta(days = retention))[:10]
print(start_date)
EC2 =  boto3.client('ec2',region)

def delete_image(imageID):
    SnapDesc= "*"+imageID+"*"
    myAccount = "382086479110"
    print("myAccount" + myAccount)
    snapshots = EC2.describe_snapshots(Filters=[{'Name': 'description','Values': [SnapDesc,]},],MaxResults=10000, OwnerIds=[myAccount])['Snapshots']
    print("Deregistering image " + imageID)
    amiResponse = EC2.deregister_image(DryRun=False,ImageId=imageID,)
    for snapshot in snapshots:
        if snapshot['Description'].find(imageID) > 0:
            snapResonse = EC2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
            print("Deleting snapshot " + snapshot['SnapshotId'])
    print("------------------------------------------")

AMIsName= "AMI-for-*"
count=0
images = EC2.describe_images(Filters=[{'Name': 'name','Values': [AMIsName,]},],DryRun=False)['Images']
print("------------------------------------------")
for image in images:
    if start_date >= image['CreationDate'][:10]:
        print(image['CreationDate'])
        count = count + 1
        print(image['ImageId']+" "+image['State']+ " "+image['CreationDate'][:10])
        delete_image(image['ImageId'])
    
