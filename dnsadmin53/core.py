import boto
import json


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

    def does_zone_exist(self, dns_zone):
        """
        Check to see if a zone exists, return True if exists and False missing.
        """
        try:
            dns_zone = dottify(dns_zone)
            self.zone = self.r53.get_zone(dns_zone)
            return True
        except boto.route53.exception.DNSServerError as e:
            print e
        else:
            return False


class IAM:
    """
    dnsadmin for AWS IAM Core Methods
    """
    def __init__(self):
        self.iam = boto.connect_iam()

    def get_all_groups(self):
        """
        List all Groups
        """
        self.groups_l = []
        try:
            self.groups = self.iam.get_all_groups()
            self.groups = self.groups['list_groups_response']['list_groups_result']['groups']
            for group in self.groups:
                self.groups_l.append(group['group_name'])
        except:
            print 'Error Getting Groups from IAM'
        return self.groups_l

    def list_policies(self):
        """
        List All Policies for a DNS Domain
        """
        self.policy_names = []
        self.policies = []
        try:
            self.groups = self.iam.get_all_groups()
            self.groups = self.groups['list_groups_response']['list_groups_result']['groups']
            for group in self.groups:
                self.policy_names.append(group['group_name'])
            for policy in self.policy_names:
                self.policies.append(self.iam.get_all_group_policies(policy))
        except TypeError as e:
            print e
        return self.policies
