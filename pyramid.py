num = 1   #initialising num as 1
for i in range(1, 7):  #setting range to form pyramid, loop runs till 6 lines
    for j in range(1, 7 - i + 1):  #setting range for spaceing
        print("  ", end=" ")
    for k in range(1, i + 1):#setting range ,every next line should print 1 number more than previous line
        print(num, end=" ,  ")
        num=num+1   #incrementing to next number
    print()
