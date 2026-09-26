#Python program to calculate percentage of 5 subjects

sub1 = float(input("Enter marks of subject 1 : "))
sub2 = float(input("Enter marks of subject 2 : "))
sub3 = float(input("Enter marks of subject 3 : "))
sub4 = float(input("Enter marks of subject 4 : "))
sub5 = float(input("Enter marks of subject 5 : "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percent = total / 5

print("Total Marks :", total)
print("Percentage :", percent,"%")

if percent >= 90:
    print("Grade Obtained : A")
elif percent >= 75:
    print("Grade Obtained : B")
elif percent >= 40:
    print("Grade Obtained : C")
elif percent >= 35:
    print("Grade Obtained : D")
else:
    print("You Failed")
