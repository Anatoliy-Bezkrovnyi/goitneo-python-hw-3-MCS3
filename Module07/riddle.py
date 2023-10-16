def solve_riddle(riddle, word_length, start_letter, reverse=False):
    
    start_position = ""
    
    for char in enumerate(riddle):
        if char[1] == start_letter:
            start_position = char[0]
            break
        
         
       
    if start_position and not reverse: 
        end_position = start_position + word_length
        word = riddle[start_position:end_position]
        return word
    elif start_position and reverse:
        end_position = start_position - word_length
        word = riddle[start_position:end_position:-1]
        return word
    else:
        return start_position






riddle = "mi1powerpret"
word_length = 5
start_letter = "p"

print(solve_riddle(riddle, word_length, start_letter, reverse=False))