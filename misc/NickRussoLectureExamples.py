import json
import yaml
import xmltodict

# with open('file1.json') as f:
#     file = json.load(f)
#     print(type(file))
#     print(file)
# with open ('file1.yaml') as f:
#     file = yaml.safe_load(f)
#     print(type(file))
#     print(file)
# with open('file1.xml') as f:
#     file = xmltodict.parse(f.read(), process_namespaces=True)
#     print(type(file))
#     print(file)
# with open('file1.xml') as f:
#     file = xmltodict.parse(f.read(), process_namespaces=True, dict_constructor=dict)
#     print(type(file))
#     print(file)
# with open('file1.xml') as f:
#     file = json.dumps(xmltodict.parse(f.read()))
#     print(type(file))
#     print(file)


print('-------')


# import requests
# headers = {"Authorization": "Bearer OLqiO0NrX8wr8l-3wFGcL0N1x--9AgwkNdSn", "Content-Type":"application/json"}
#
# print(type(headers))
# response = requests.get('https://gorest.co.in/public-api/users', headers=headers)
# print(type(response))
# response = response.text
# print(type(response))
# response = json.dumps(response)
# print(type(response))

class credentials:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class dnac(credentials):

    def __init__(self, username, password):
        # self.username = username
        # self.password = password
        credentials.__init__(self, username, password)
        self.url = 'https://sandboxdnac.cisco.com/'

    def get_auth_token(self):
        from requests.auth import HTTPBasicAuth
        # from dnac_config import DNAC_PORT, USERNAME, PASSWORD
        try:
            api = self.url + 'dna/system/api/v1/auth/token'
            resp = requests.post(api, auth=(self.username, self.password))
            resp.raise_for_status()
            token = resp.json()['Token']
            return(token)
        except requests.HTTPError as e:
            print(e)
            print(e.response.text)

    def get_devices(self):
        token = self.get_auth_token()
        api = self.url + 'dna/intent/api/v1/network-device'
        header = {'x-auth-token': token, 'content-type': 'application/json'}
        query = {'hostname': 'cat_9k_1.abc.inc'}
        resp = requests.get(api, headers=header)#, params=query)
        device_list = resp.json()
        # device_list = json.dumps(device_list, indent=2)
        return(device_list)


    # def print_device_list(self):
    #     device_json = self.get_devices()
    #     print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
    #           format("hostname", "mgmt IP", "serial", "platformId", "SW Version", "role", "Uptime"))
    #     for device in device_json['response']:
    #         uptime = "N/A" if device['upTime'] is None else device['upTime']
    #         if device['serialNumber'] is not None and "," in device['serialNumber']:
    #             serialPlatformList = zip(device['serialNumber'].split(","), device['platformId'].split(","))
    #         else:
    #             serialPlatformList = [(device['serialNumber'], device['platformId'])]
    #         for (serialNumber, platformId) in serialPlatformList:
    #             print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
    #                   format(device['hostname'],
    #                          device['managementIpAddress'],
    #                          serialNumber,
    #                          platformId,
    #                          device['softwareVersion'],
    #                          device['role'], uptime))


class meraki:

    def __init__(self):
        self.url = 'https://api.meraki.com/api/v0'
        self.token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

    def get_organizations_api(self):
        header = {'X-Cisco-Meraki-API-Key': self.token, 'content-type': 'application/json'}
        api = self.url + '/organizations'
        try:
            resp = requests.get(api, headers=header)
            resp.raise_for_status()
            organizations = resp.json()
        # organizations = json.dumps(organizations, indent=2)
            return(organizations)
        except requests.HTTPError as e:
            # print(e)
            print(e.response.text)


    def get_device_statuses(self):

        org_ids = []
        for item in self.get_organizations_api():
            org_ids.append(item['id'])
        header = {'X-Cisco-Meraki-API-Key': self.token, 'content-type': 'application/json'}

        apis = []
        for item in org_ids:
            apis.append(self.url + '/organizations/' + item + '/deviceStatuses')

        for item in apis:
            resp = requests.get(item, headers=header)
            device_statuses = resp.json()
            device_statuses = json.dumps(device_statuses, indent=2)

        return(device_statuses)


class sdwan:

    def __init__(self, username, password):
        credentials.__init__(self, username, password)
        self.url = 'http://10.10.20.90:8443'

    def get_auth_session(self):
        import sys
        uri = '/j_security_check'
        login_api = self.url + uri
        login_creds = {'j_username': 'admin','j_password': 'admin'}
        try:
            sess = requests.session()
            login_response = sess.post(login_api, data=login_creds, verify=False, timeout=(2,1))
            login_response.raise_for_status()
            return(login_response)
        except requests.ConnectionError as e:
            print(e)
    #
    # def get_device(self):
    #     api = self.url + 'dataservice/device'
    #     header = {'content-type': 'application/json'}
    #     resp = requests.get(api, auth=(self.username, self.password), headers=header)
    #     devices = resp.json()
    #     return devices


class aci:

    def __init__(self, username, password):
        credentials.__init__(self, username, password)
        self.url = 'https://sandboxapicdc.cisco.com'

    def get_token(self):
        headers = {'content-type': 'application/json'}
        body = {
            "aaaUser": {
                "attributes": {
                    "name": "admin",
                    "pwd": "ciscopsdt"
                }
            }
        }
        api = self.url + '/api/aaaLogin.json'
        try:
            sess = requests.session()
            resp = sess.post(api, json=body, verify=False, headers=headers)
            resp.raise_for_status()
            token = resp.json()['imdata'][0]['aaaLogin']['attributes']['token']
            return(token)
        except requests.ConnectionError as e:
            print(e.text)

    def get_epg(self):
        token = self.get_token()
        api = self.url + '/api/class/fvAEPg.json'
        headers = {"cookie": f"APIC-Cookie={token}"}
        try:
            resp = requests.get(api, headers=headers, verify=False)
            resp.raise_for_status()
            epgs = resp.json()
            # epgs = json.loads(epgs)

            for item in epgs['imdata']:
                print(item['fvAEPg']['attributes']['dn'])
        except requests.ConnectionError as e:
            print(e.text)

import requests
import json
if __name__ == "__main__":
    # req1 = dnac('devnetuser', 'Cisco123!')
    # print(req1.get_auth_token())
    # req1.get_devices()
    # print(req1.get_device_id())
    # req1.print_device_list()
    # print(req1.get_device_id())
    # print(req1.get_device_interface())
    # req1.print_device_interface_list()

    # req2 = meraki()
    # # print(req2.get_organizations_api())
    # print(req2.get_device_statuses())

    # req3 = sdwan('admin', 'admin')
    # req3.get_auth_session()


    req4 = aci('admin', 'ciscopsdt')
    req4.get_token()
    req4.get_epg()
