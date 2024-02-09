maths = int(input("maths scored: "))
if maths < 0 or maths > 100:
    print("Invalid input")

eng = int(input("eng scored: "))
if eng < 0 or eng > 100:
    print("invalid input")

phy = int(input("phy scored: "))
if phy < 0 or phy > 100:
    print("invalid input")

chem = int(input("chem scored: "))
if chem < 0 or chem > 100:
    print("invalid input")

bio = int(input("bio scored: "))
if bio < 0 or bio > 100:
    print("invalid input")


#------Computation-----#
# total = [maths+eng+phy+chem+bio]
#
#
# average = total / 5



print(f"the total sum {maths+eng+phy+chem+bio}")

print(f"average {(maths+eng+phy+chem+bio)/5}")





if (maths+eng+phy+chem+bio)/5 > 0 < 39:
    print("E")


if (maths+eng+phy+chem+bio)/5 > 40 < 50:
    print("D")

if (maths+eng+phy+chem+bio)/5 > 50 < 60:
    print("C")

if (maths+eng+phy+chem+bio)/5 > 60 < 80:
    print("B")

if (maths+eng+phy+chem+bio)/5 > 80 < 99:
    print("A")














# print(f"the total sum {maths+eng+phy+chem+bio}")
#
# print(f"average {(maths+eng+phy+chem+bio)/5}")
















