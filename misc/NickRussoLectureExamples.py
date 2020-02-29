import json
import yaml
import xmltodict

with open('file1.json') as f:
    file = json.load(f)
    print(type(file))
    print(file)
with open ('file1.yaml') as f:
    file = yaml.safe_load(f)
    print(type(file))
    print(file)
with open('file1.xml') as f:
    file = xmltodict.parse(f.read(), process_namespaces=True)
    print(type(file))
    print(file)
with open('file1.xml') as f:
    file = xmltodict.parse(f.read(), process_namespaces=True, dict_constructor=dict)
    print(type(file))
    print(file)
with open('file1.xml') as f:
    file = json.dumps(xmltodict.parse(f.read()))
    print(type(file))
    print(file)


print('-------')


import requests
headers = {"Authorization": "Bearer OLqiO0NrX8wr8l-3wFGcL0N1x--9AgwkNdSn", "Content-Type":"application/json"}

print(type(headers))
response = requests.get('https://gorest.co.in/public-api/users', headers=headers)
print(type(response))
response = response.text
print(type(response))
response = json.dumps(response)
print(type(response))



class dnac:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

    def get_auth_token(self):
        import requests
        from requests.auth import HTTPBasicAuth
        # from dnac_config import DNAC_PORT, USERNAME, PASSWORD
        api = self.url + 'dna/system/api/v1/auth/token'
        resp = requests.post(api, auth=(self.username, self.password))
        token = resp.json()['Token']
        return(token)


    def get_devices(self):
        token = self.get_auth_token()
        api = self.url + 'dna/intent/api/v1/network-device'
        header = {'x-auth-token': token, 'content-type': 'application/json'}
        query = {'hostname': 'cat_9k_1.abc.inc'}
        resp = requests.get(api, headers=header, params=query)
        device_list = resp.json()
        device_list = json.dumps(device_list, indent=2)
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


if __name__ == "__main__":
    req1 = dnac('devnetuser', 'Cisco123!', 'https://sandboxdnac.cisco.com/')
    req1.get_auth_token()
    print(req1.get_devices())