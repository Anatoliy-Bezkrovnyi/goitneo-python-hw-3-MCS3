from pathlib import Path


def get_recipe(path, search_id):
    file_location = Path(path)
    

    with open(file_location, "r") as file_object:
        while True: 
            line = file_object.readline().rstrip("\n")
            if not line: 
                break
            line_list = line.split(",")
            if search_id == line_list[0]:                
                ingredients_list = line_list[2:]
                receipt = {"id": line_list[0], "name": line_list[1] , "Ingredients": ingredients_list }
                return receipt
            else: 
                continue
        return None    
            



path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\list_receipts.txt"
search_id = "60b90c3b13067a15887e1ae8"

print(get_recipe(path, search_id))