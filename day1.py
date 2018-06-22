import json, os

filepath = os.path.join(os.getcwd(),"bob.json")
d = json.load(open(filepath,"r"))
# single line comment

filepath = os.path.join(os.getcwd(),"kelso.json")
d2 = json.load(open(filepath,"r"))
# single line comment

employees = ["Homer Simpson"]
managers = ["C. Montgomery Burns"]

manager_aliases = {"Charles Burns":"C. Montgomery Burns"}

def format_employee_name(unformatted_name_as_dict):
    #return '%s %s'%(unformatted_name_as_dict["firstname"].capitalize(),
    #                unformatted_name_as_dict["lastname"].capitalize())

    return '{:s} {:s}'.format(unformatted_name_as_dict["firstname"].capitalize(),
                    unformatted_name_as_dict["lastname"].capitalize())
employee_count = 0
manager_count = 0

for item in d2:
    tmp_name = item["name"]
    #not if tmp_nam e in employees:
    if tmp_name in employees:
        employee_count += 1 
    elif format_employee_name(tmp_name) in employees:
        employee_count += 1 
    elif tmp_name in managers:
        manager_count += 1 
    elif format_employee_name(tmp_name) in managers:
        manager_count += 1 
    elif manager_aliases[format_employee_name(tmp_name)] in managers:
        manager_count += 1 
    '''
    if type(tmp_name) == dict:
        if format_employee_name(tmp_name) in employees:
            employee_count += 1
    elif type(tmp_name) == str:
        if tmp_name in employees
            employee_count += 1
            
    if (tmp_name in employees) or (format_employee_name(tmp_name) in employees):
        employee_count += 1
    '''
