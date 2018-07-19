import SoftLayer

client = SoftLayer.Client()

def getSubjects(self):
    mask = "mask[group]"
    subjects = client.call('SoftLayer_Ticket_Subject', 'getAllObjects', mask=mask)
    print("|Subject Id | Subject Name | Group Name |")
    print("| --- | --- | --- |")
    for subject in subjects:
        print("|%s| %s| %s|" % (subject['id'], subject['name'], subject['group']['name']))