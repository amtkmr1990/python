
qa_file = open( "questions.txt", "r" )
content = qa_file.readlines()
qa_file.close()
total_ques = 0
total_right_ans = 0

for i in content:
    total_ques = total_ques + 1
    ip = input(f'{i.split("=")[0]} = ')
    if ip == i.split("=")[1].strip():
        total_right_ans = total_right_ans + 1
    else:
        print(f' Wrong - Answer is {i} ')

result_file = open("result.txt","a")
result_file.write("\n")
result_file.write(f"your final score is {total_right_ans}/{total_ques}")
result_file.close()