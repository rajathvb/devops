from datetime import datetime, timedelta, timezone
import boto3
import os
ec2 = boto3.resource('ec2')
snapshots = ec2.snapshots.filter(OwnerIds=['self'])
print(snapshots)
for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days = 300)
    if delete_time > start_time:
        snapshot.delete()
        print('snapshot with ID = {} is deleted'.format(snapshot.snapshot_id))
