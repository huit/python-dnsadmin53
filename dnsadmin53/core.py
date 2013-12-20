import boto


class Route53:
    """
    dnsadmin for AWS Route 53 Core Methods
    """
    def __init__(self):
        try:
            self.r53 = boto.connect_route53()
        except DNSServerError:
            print 'Error'

    def list_zones(self):
        """
        List Zones in Route53
        """
        self.zones = self.r53.get_zones()
        return self.zones

    def get_zone(self, dns_zone = 'devel.huit.harvard.edu'):
        """
        Get Zone. Valid Param is FQDN.
        """
        self.zone = self.r53.get_zone(dns_zone+'.')
        return self.zone
