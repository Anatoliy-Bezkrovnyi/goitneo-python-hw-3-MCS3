def format_ingredients(items):
   formatted_string = ""
   if len(items) == 0:
       return formatted_string
   elif len(items) == 1:
       formatted_string = formatted_string + items[0]
       return formatted_string
   elif len(items) == 2:
       items.insert(len(items) -1, " and ")
       for item in items:
           formatted_string = formatted_string + item
       return formatted_string
   else:
       items.insert(len(items) -1, " and ")
       counter = 0
       while counter < len(items) - 2:
           if counter % 2 == 1:
               items.insert(counter, ", ")
               counter = counter + 1
           else:
               counter = counter + 1   
       
       for item in items:
           formatted_string = formatted_string + item
       return formatted_string
       

list = ["sugar", "eggs", "tea", "vine", "crops", "garlic", "tomato", "pickles", "toasts", "chocolate"]

print(format_ingredients(list))
print(1%2)
