"""
open file
read total number of line
read line by line
split =
print question
compare input with answer
if correct increase count by 1

"""

with open('q&a.txt') as myfile:
    lines = [line for line in myfile.readlines()]

total_question = len(lines)
correct_answer = 0
for l in lines:
    q, a = l.strip().split('=')
    ans = input(f'{q}=')
    if ans == a:
        correct_answer += 1

with open('score_card.txt','w') as myfile:
    myfile.write(f'Your final score is {correct_answer}/{total_question}')
