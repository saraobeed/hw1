num_str = input('Enter a number:')
num = int(num_str)

num_bin = []
while num > 0:
    num_bin.insert(0,num%2)
    num=num//2

for d in num_bin:
    print(d, end='')
