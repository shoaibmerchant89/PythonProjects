from dnacentersdk import api

dnac = api.DNACenterAPI(base_url='https://sandboxdnac.cisco.com/', username='devnetuser', password='Cisco123!')

token = dnac.access_token
print(token)

devices = dnac.devices.get_device_list()
print(devices.response)

for device in devices.response:
    # print('{:20}{}'.format(device.hostname, device.upTime))
    print(f"ID: {device['id']}  IP: {device['managementIpAddress']}")


