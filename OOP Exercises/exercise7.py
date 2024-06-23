# Write a program to remove characters from a string
# starting from zero up to n and return a new string.

def remove_chars(word,n):
    x = word[n:]
    return x

print("Remove character from a string")
print(remove_chars(word = input("Enter a string :"),
                      n =int(input("Enter slice :"))))
print(remove_chars(word = input("Enter a sec string :"),
                      n = int(input("Enter slice :"))))
