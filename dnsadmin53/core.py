import boto


def dottify(string):
    """
    Add a final period to DNS Name Strings.
    """
    if not string.endswith('.'):
        string = string + '.'
    return string


class Route53:
    """
    dnsadmin for AWS Route 53 Core Methods
    """
    def __init__(self):
        try:
            self.r53 = boto.connect_route53()
        except boto.route53.exception.DNSServerError as e:
            print e

    def list_zones(self):
        """
        List Zones in Route53
        """
        try:
            self.zones = self.r53.get_zones()
        except boto.route53.exception.DNSServerError as e:
            print e
        return self.zones

    def get_zone(self, dns_zone):
        """
        Get Zone Object. Valid Param is FQDN.
        """
        try:
            dns_zone = dottify(dns_zone)
            self.zone = self.r53.get_zone(dns_zone)
        except boto.route53.exception.DNSServerError as e:
            print e
        return self.zone
