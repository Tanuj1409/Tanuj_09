import random
import string

def generate_password (length = 12):
    """ Create a safe password of the given length. """ 
    if  length < 4:
        print ("The length of the password should be at least 4 characters.")
        return None
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
 
    
    return password

if __name__ == "__main__":
    try:
        length = int (input ("Password Length:"))
        Password = generate_password (length)
        if Password:
            print ( "generated password:",Password)
    except ValueError:
        print ("Please enter a valid number.")