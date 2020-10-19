for num in range(100, 401):
    flag = True
    for d in str(num):
        if int(d) % 2 != 0:
            flag = False
            break
    if flag == True:
        print(num, end=" , ")
