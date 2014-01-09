aws-dnsadmin53
==============
[![Build Status](https://travis-ci.org/huit/python-dnsadmin53.png?branch=master)](https://travis-ci.org/huit/python-dnsadmin53)

Manage access to zones in Route 53

There are a couple of limitations on IAM Objects
http://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html

Based on this it seems like roles will be the best way to go

Two types of cross account access both grant access by giving the external AWS account the ARN of the role and the user then makes api calls to AssumeRole with the ARN of the role to get temp credentials allowing access to the role. (in our case updating DNS entries within a zone) 

The first allows you to delegate access with just Account ID putting the trust on the repote account to create a group which has approriate access to the Role ARN

http://docs.aws.amazon.com/IAM/latest/UserGuide/cross-acct-access.html


The second type of delegation requires both an Account ID AND a External ID, which prevents the "Confused Deputy" problem ( http://en.wikipedia.org/wiki/Confused_deputy_problem) 

http://docs.aws.amazon.com/STS/latest/UsingSTS/sts-delegating-externalid.html

http://docs.aws.amazon.com/STS/latest/UsingSTS/Welcome.html
