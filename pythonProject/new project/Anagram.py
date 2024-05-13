str2=input("Enter string 1")
str1=input("Enter string 2")
def anagram(str1,str2):
    str1=str1.lower()         #using lower() method to convert into lower case
    str2=str2.lower()
    sorted(str1)              #sorted() method to sort in alphanumeric order
    sorted(str2)
    return sorted(str1) == sorted(str2)       #comparing both sting is in same order or not
result=anagram(str1,str2)                    #storeing the result of thae above method in a variable
print("Anagram :",result)