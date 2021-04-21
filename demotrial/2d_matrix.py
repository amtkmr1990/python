row = int(input('Enter the rows'))
col = int(input('Entr the col'))

row_list = []

for i in range(row):
    col_list = []
    for j in range(col):
        col_list.append(i*j)
    row_list.append(col_list)

print(row_list)
