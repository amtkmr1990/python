n = int(input('enter value'))
t = int(input('enter number of times'))

num_list = []
next_value = ''
if t > 1 :
    for i in range(t):
        next_value = next_value + str(n)
        num_list.append(next_value)

print(num_list)
counter = 0
for i in num_list:
    counter = counter + int(i)

print(counter)

