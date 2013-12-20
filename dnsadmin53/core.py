import boto

class Route53:
    """
    dnsadmin for AWS Route 53 Core Methods
    """ 
    def __init__(self):
        self.r53 = boto.connect_route53()


    def list_zones(self):
        """
        List Zones in Route53
        """
        self.zones = self.r53.get_zones()
        return self.zones

    def get_zone(name):
        """
        Get Zone. Valid Param is FQDN.
        """
        self.zone = self.r53.get_zone(devel.huit.harvard.edu+'.')
        return self.zone
