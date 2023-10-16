from pathlib import Path

def save_credentials_users(path, users_info):

     with open(path, "wb") as file_object:
         for key, value in users_info.items(): 
             string = f"{key}:{value}\n"  
             file_object.write(string.encode())

 



path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\creds.bin"
users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

save_credentials_users(path, users_info)