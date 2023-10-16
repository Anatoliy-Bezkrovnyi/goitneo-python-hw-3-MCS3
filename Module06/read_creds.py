def get_credentials_users(path):

    creds = list()

    with open(path, "rb") as file_object:
        while True:
            cred_line = file_object.readline()
            if not cred_line: 
                break
            cred_line = cred_line.decode().rstrip("\n")
            creds.append(cred_line)
    return creds



path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\creds.bin"
print(get_credentials_users(path))