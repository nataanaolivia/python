maths = int(input("maths scored: "))
eng = int(input("eng scored: "))
phy = int(input("phy scored: "))
chem = int(input("chem scored: "))
bio = int(input("bio scored: "))


print(f"the total sum {maths+eng+phy+chem+bio}")

print(f"average {(maths+eng+phy+chem+bio)/5}")


average = 80

if average > 80:
    print("A")
elif average < 69:
    print("B")
else:
    print("c")


# if maths > 70 and eng > 70:
#     print("success")
#
# elif maths > 70 or eng < 70:
#     print("you passed either maths or eng")
#
# else:
#     print("maths and eng equals to 70")








