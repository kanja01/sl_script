"""
Disable the email invoice after creation option.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getUsers
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/createNotificationSubscriber
http://sldn.softlayer.com/article/Object-Filters

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

USERNAME = 'set me'
API_KEY = 'set me'

userName = "set me"

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']
userService = client['SoftLayer_User_Customer']

objectFilterUser = {"users": {"username": {"operation": userName}}}

try:
    users = accountService.getUsers(filter=objectFilterUser)
    result = userService.deactivateNotificationSubscriber("BILLING_INVOICE_CREATED", users[0]['accountId'], id=users[0]['id'])
    print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

except SoftLayer.SoftLayerAPIError as e:
    print("Unable to disable the email invoice after creation option. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))