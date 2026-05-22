import random
alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_chars = ['!','@','#','$','%','^','&','*']

char = int(input("How many characters do you want in your password?\n"))
num = int(input("How many numbers do you want in your password?\n"))
spec = int(input("How many special characters do you want in your password?\n"))

# password = ""
# for i in range(1,char+1):
#     password += random.choice(alphabets)

# for i in range(1,num+1):
#     password += random.choice(numbers)

# for i in range(1,spec+1):
#     password += random.choice(special_chars)

# print("Your password is: " , password)

passw = []
for i in range(1,char+1):
    passw.append(random.choice(alphabets))

for i in range(1,num+1):
    passw.append(random.choice(numbers))

for i in range(1,spec+1):
    passw.append(random.choice(special_chars))

random.shuffle(passw)
print(f"Your password is: {''.join(passw)}")










