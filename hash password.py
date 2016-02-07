alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def hash_password(password):
    hash_value = 0
    for x in password:
        hash_value = hash_value + len(password) + 6 * len(password) + 26
    return hash_value
print (hash_password("wassupmyhomiejkdjfkkjfkjdkfjkjkjkjkjajdkl"))
        
