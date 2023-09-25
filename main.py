print("Hello World!")
print("Hello GIT!")

message = input("Enter a message: ")
offset = int(input("Enter the offset: "))

encoded_message = ""

for ch in message:
    existing_position = ord(ch)
    if (existing_position >= 65 and existing_position <= 90):
        new_position = existing_position - ord("A")
        new_position = (new_position + offset) % 26
        encoded_char = chr(new_position + ord("A"))
    elif (existing_position >= 97 and existing_position <= 122):
        new_position = existing_position - ord("a")
        new_position = (new_position + offset) % 26
        encoded_char = chr(new_position + ord("a"))
    else:
        encoded_char = chr(existing_position)
    
    encoded_message = encoded_message + encoded_char

print(encoded_message)
    