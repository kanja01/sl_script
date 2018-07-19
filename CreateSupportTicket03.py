import SoftLayer
client = SoftLayer.Client()
def createTicket(self):
    current_user = client.call('SoftLayer_Account', 'getCurrentUser')
    body = "I'm testing API ticket creation. Please close this ticket if you see it. Thanks."
    serverId = 1317535
    serverPass = '12345'
    # http://sldn.softlayer.com/reference/datatypes/SoftLayer_Ticket
    new_ticket = {
        'subjectId': 1021,
        'assignedUserId': current_user['id'],
        'title': 'TESTING TICKET 003',
        'priority': 4
    }
    # parameter list is from, need to be in order http://sldn.softlayer.com/reference/services/softlayer_ticket/createStandardTicket
    created_ticket = client.call('SoftLayer_Ticket', 'createStandardTicket', 
        new_ticket, body, serverId, serverPass, None, None, None, 'HARDWARE')
    pp(created_ticket)