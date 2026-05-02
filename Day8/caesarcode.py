alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# def encrypt(original_text, shift_amount):
#     cipher_text = "" 
#     for letter in original_text:
#         shifted_position =alphabet.index(letter) + shift_amount
#         shifted_position = shifted_position  % len(alphabet)
#         cipher_text += alphabet[shifted_position]  
        
#     print(f"The encoded text is {cipher_text}")

# encrypt(text,shift)

# def decrypt(cipher_text, shift_amount):
#     original_text = ""
#     for letter in cipher_text:
#         shifted_position =alphabet.index(letter) - shift_amount
#         shifted_position = shifted_position  % len(alphabet)
#         original_text += alphabet[shifted_position]

#     print(f"The decoded text is {original_text}")

# decrypt(text,shift)

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = "" 

    if encode_or_decode == "decode":
                shift_amount *= -1
                
    for letter in original_text:
        
        if letter not in alphabet:
            output_text += letter
        
        else:   
            shifted_position =alphabet.index(letter) + shift_amount
            shifted_position = shifted_position  % len(alphabet)
            output_text += alphabet[shifted_position]  
            
    print(f"The {encode_or_decode} text is {output_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser(text, shift, direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")
        

