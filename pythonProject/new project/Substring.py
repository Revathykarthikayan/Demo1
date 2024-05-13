string1 = input('Enter word  1. : ')
string2 = input('Enter word  2. : ')
answer = ""
len1, len2 = len(string1), len(string2)
#len1, len2 to store string1 ,string2 lenth respectively
for i in range(len1):
    for j in range(len2):
        lcs_temp=0
        match=''
        # 3 conditions checked in while loop
        while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and  string1[i+lcs_temp] == string2[j+lcs_temp]):
            # curent string is updated in match
            match += string2[j+lcs_temp]
            # current count is incremented
            lcs_temp+=1
        if (len(match) > len(answer)): #checks(match)length of the longest common substring found so far (answer).
            answer = match
print(answer)