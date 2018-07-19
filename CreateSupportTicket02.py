import SoftLayer
client = SoftLayer.Client()
currentUser = client['Account'].getCurrentUser()
new_ticket = {
       'subjectId': 1021,
       'assignedUserId': currentUser['id']
}
created_ticket = client.call('SoftLayer_Ticket', 'createStandardTicket', new_ticket, "Content of the ticket goes here")