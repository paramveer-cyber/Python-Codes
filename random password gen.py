import random
import string

    
try:

    print("Minimum Password length should be 3")
        
    val = int(input("Please Enter the Length of the Password: "))

    char = string.ascii_uppercase + string.ascii_lowercase + string.digits

    password = ''.join(random.choice(char) for _ in range(val))

    print("Password =", password)

except:
    print("Error :/")
