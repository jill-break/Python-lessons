prev_num = 0
next_num = 1

# print(prev_num)
# print(next_num)
# for i in range(18):
#     fib = prev_num + next_num
#     print(fib)
#     next_num = prev_num
#     prev_num = fib

print(0)
print(1)
count = 2
def fib(prev1, prev2):
    global count
    if count <= 19:
        nfib = prev1 + prev2
        print(nfib)
        prev2 = prev1
        prev1 = nfib
        count += 1
        fib(prev1, prev2)
    else:
        return 
fib(1,0)