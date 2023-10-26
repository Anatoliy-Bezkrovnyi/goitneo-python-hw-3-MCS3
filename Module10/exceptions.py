class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    id_list = []
    if employee_id.startswith("01"):
        id_list.append(employee_id)
    else:
        raise IDException
    return id_list