found = int(input("How many fibonacci should be found: "))
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        fn = fib(num - 1) + fib(num - 2)
        return fn
for i in range(found):
    print(fib(i))
print("All done!")