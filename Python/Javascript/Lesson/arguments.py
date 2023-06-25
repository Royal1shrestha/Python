def sum(*args):
    sum = 0
    # args[0] = 0 doesn't work as it isn't supported in tuple.So, we convert it to list.
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum
    
print(sum(1,2,3,4,5))       
    