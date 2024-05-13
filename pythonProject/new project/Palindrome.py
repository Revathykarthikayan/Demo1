str=input("Enter string: ")
def palindrome(str):
    str = str.lower()       #using lower() method to convert into lower cas
    return str== str[::-1]     #performing string reverse and comparing with original string
result=palindrome(str)
print("Palindrome :",result)