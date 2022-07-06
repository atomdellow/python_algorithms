def gen_fibonnacci(n):
       
    a = 1
    b = 1
    #yield
    output = []
    for i in range(n):
        yield a
        a,b = b,a+b
    for number in gen_fibonnacci(10):
        print(num)
#next 

# def simple_gen():
#    for x in range(3)
#        yield x
# for number in simple_gen():
#    print(number)
# g =  simple_gen()
# g
# print(next(g))
# print(next(g)) # yield adds values but doesn't add it to memory