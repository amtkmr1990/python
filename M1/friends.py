"""
1. input 3 names
2. check input names are in people.txt
3. if found as user whether to add in nearby_pepople.txt file ?
4. if yes - add else pass
5. display your content of nearby_friends.txt file
"""


def get_friends():
    friend = input(" Enter any friend name : ")
    file = open("people.txt",'r')
    content = file.read()
    file.close()
    r = 0
    if friend in content:
        check = input(f"We found the {friend} in people.txt file ... Would you like t add him in nearby_friends.txt file : (Y/N)")
        if check == 'Y' or check == 'y':
            file = open("nearby_friends.txt",'a')
            file.write("\n")
            file.write(friend)
            file.close()

        elif check == 'N' or check == 'n':
            nearby_file  = open("nearby_friends.txt",'r')
            print(f"Here are your nearby friends {nearby_file.read()}")
            nearby_file.close()

        else:
            print("Enter y or n")
    else:
        print(f"{friend} is not present in people.txt")


n = 0
while n < 3:
    get_friends()
    n = n + 1



