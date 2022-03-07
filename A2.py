import string
def uc_cal(str):
    uc=0
    lc=0
    list=str.split(" ")
    for i in range(len(list)):
        if list[i] in string.ascii_uppercase:
            uc=uc+1
        else:
            lc=lc+1
    print("\n No of Uppercase Letters:",uc,"\n No of Lowercase Letters:",lc)

s=input("Enter a string include space between each letter:")
uc_cal(s)