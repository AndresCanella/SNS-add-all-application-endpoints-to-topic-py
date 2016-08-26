import boto3
# setup
platformApplicationArn = 'your-PlatformApplicationArn'
topicArn = 'your-TopicArn'
# client
client = boto3.client('sns')

nextToken = None
batch = 0
while True:
    if nextToken:
        response = client.list_endpoints_by_platform_application(PlatformApplicationArn=platformApplicationArn, NextToken=nextToken)
    else:
        response = client.list_endpoints_by_platform_application(PlatformApplicationArn=platformApplicationArn)
    endpoints = response['Endpoints']
    batch += len(endpoints)
    print 'batch: %d nextToken: %s' % (batch, nextToken)

    # iterate elements
    print 'end point back size %d' % len(endpoints)
    for item in endpoints:
        endpointArn = item['EndpointArn']
        print endpointArn

        # subscribe
        subResponse = client.subscribe(
            TopicArn=topicArn,
            Protocol='application',
            Endpoint=endpointArn
        )
        print 'subResponse: %s' % subResponse

    # finished
    if response.get('NextToken', None) is None:
        break
    else:
        nextToken = response['NextToken']
