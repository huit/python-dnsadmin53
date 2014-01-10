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

    def get_zone_id(self, dns_zone):
        """
        Get Zone ID.
        """
        try:
            self.zone_id = self.r53.get_hosted_zone_by_name(dns_zone)
            self.zone_id = self.zone_id['GetHostedZoneResponse']['HostedZone']['Id']
            self.zone_id = self.zone_id.strip('/hostedzone/')
        except Exception, e:
            print e
            print 'Error Getting Zone ID'
        return self.zone_id

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
    trust_policy = {"Version": "2012-10-17", "Statement": [{"Sid": "", "Effect": "Allow", "Principal": {"AWS": []}, "Action": "sts:AssumeRole"}]}

#          "arn:aws:iam::219880708180:root",
#          "arn:aws:iam::691803950817:root"

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

    def list_roles(self):
        """
        List Roles
        """
        try:
            self.roles = self.iam.list_roles(path_prefix='/dnsadmin53/')
        except:
            print 'Error getting Role List from IAM'
        return self.roles

    def create_role(self, dns_zone, zone_id):
        """
        Create DNSADMIN Role for a hosted zone.
        """
        path_prefix = '/dnsadmin53/'
        role_name = 'UpdateZone-' + dns_zone
        permission_policy = {"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": ["route53:ChangeResourceRecordSets"], "Resource": "arn:aws:route53:::hostedzone/" + zone_id}, {"Effect": "Allow", "Action": ["route53:GetChange"], "Resource": "arn:aws:route53:::change/*"}]}
        permission_policy = json.dumps(permission_policy, indent=2, separators=(',', ': '))

        try:
            self.role = self.iam.create_role(role_name, path=path_prefix)
            self.instance_profile = self.iam.create_instance_profile(role_name, path=path_prefix)
            self.iam.add_role_to_instance_profile(role_name, role_name)
            self.iam.put_role_policy(role_name, 'UpdateZone', permission_policy)
            print json.dumps(IAM.trust_policy)
            print permission_policy
        except Exception, e:
            print 'Error Creating Role in IAM'
            print e
