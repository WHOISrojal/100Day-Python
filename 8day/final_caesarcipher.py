from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char 
    print(f"The {cipher_direction}d text is {end_text}")

should_end = False
while not should_end:
    direction = input("Enter 'encode' or 'decode' to be performed\n").lower()
    text = input("Enter text here\n").lower()
    shift = int(input("Enter shifting value\n"))

    shift = shift % 25
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    restart = input("Type 'yes' or 'no' if you want to continue or not")
    if restart == "no":
        should_end = True
        print("GoodBye")