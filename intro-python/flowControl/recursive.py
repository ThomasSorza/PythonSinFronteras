def recursive(i):
    if(i<1):
        return i
    print(i)
    recursive(i-1)

recursive(5)
