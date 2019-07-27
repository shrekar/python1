
input = {'ncet-ec001':'rajesh', 'ncet-cs001':'mahesh', 'ncet-is001':'suresh'}


def find_name (usn, name):

    if name in usn:
        return usn[name]
    else:
        return "Not found"

