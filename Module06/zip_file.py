import shutil


def create_backup(path, file_name, employee_residence):
     
    
    with open(f"{path}\{file_name}", "wb") as file_object:
        for key, value in employee_residence.items():
            file_string = f"{key} {value}\n"
            file_object.write(file_string.encode())

    archive_name = shutil.make_archive("backup_folder", "zip", path)
    return archive_name
       

employee_residence = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\\backup_folder"
file_name = "backup.bin"

print(create_backup(path, file_name, employee_residence))