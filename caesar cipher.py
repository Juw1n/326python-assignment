# program to implement a ceaser cipher
          
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

for char in message:
    if char.lower() in alphabet:
        is_upper = char.isupper()
        index = alphabet.index(char.lower())
        new_index = (index + shift) % 26
        new_char = alphabet[new_index]
        if is_upper:
            new_char = new_char.upper()
        result += new_char
    else:
        result += char 

print("Encrypted message:", result)
