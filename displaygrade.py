sub1 = int(input("enter mark of the first subject : "))
sub2 = int(input("enter mark of the second subject : "))
sub3 = int(input("enter mak of the third subject : "))
sub4 = int(input("enter mark of the forth subject : "))
sub5 = int(input("enter mark of the fifth subject : "))
avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
if avg >= 90:
    print("grade: A ")
elif avg >= 80 and avg < 90:
    print("grade: B ")
elif avg >= 70 and avg < 80:
    print("grade: C ")
elif avg >= 60 and avg < 70:
    print("grade: D ")
else:
    print("grade: F ")