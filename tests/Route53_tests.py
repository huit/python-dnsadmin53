import boto
import sure
from nose import tools
from dnsadmin53 import core
from moto import mock_route53


@mock_route53
def test_get_zone():
    conn = boto.connect_route53()
    conn.create_hosted_zone('devel.huit.harvard.edu.')

    r53 = core.Route53()
    zone = r53.get_zone('devel.huit.harvard.edu')
    assert zone.name == 'devel.huit.harvard.edu.'


@mock_route53
def test_list_zone():
    conn = boto.connect_route53()
    conn.create_hosted_zone('devel1.huit.harvard.edu.')
    conn.create_hosted_zone('devel2.huit.harvard.edu.')

    r53 = core.Route53()
    zones = r53.list_zones()
    len(zones).should.equal(2)


@mock_route53
def test_does_zone_exist():
    conn = boto.connect_route53()
    conn.create_hosted_zone('devel.huit.harvard.edu.')

    r53 = core.Route53()
    result = r53.does_zone_exist('devel.huit.harvard.edu')
    print result
    tools.assert_true(result)


@mock_route53
def test_get_zone_id():
    conn = boto.connect_route53()
    conn.create_hosted_zone('devel.huit.harvard.edu.')

    r53 = core.Route53()
    zone_id = r53.get_zone_id('devel.huit.harvard.edu')
    tools.assert_true(zone_id)
