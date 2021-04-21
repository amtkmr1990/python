
def save_to_file(content,file_path):
    with open(file_path,"w") as wf:
        wf.write(content)


def read_file(file_path):
    with open(file_path) as rf:
        return  rf.read()

