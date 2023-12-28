def add_int(arr):
    sum=0
    for i in arr:
        if type(i)==int:
            sum+=i
    print(sum)

add_int([1,'2','b',5,6])
add_int([10,20,'l'])
    