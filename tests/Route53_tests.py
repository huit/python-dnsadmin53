import boto
from dnsadmin53 import core
from moto import mock_route53


@mock_route53
def test_get_zone():
    conn = boto.connect_route53()
    conn.create_hosted_zone('devel.huit.harvard.edu.')

    r53 = core.Route53()
    zone = r53.get_zone('devel.huit.harvard.edu')
    assert zone.name == 'devel.huit.harvard.edu.'
