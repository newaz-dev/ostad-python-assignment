print("Enter Student Name: ")
a = input()
print("Mark's of three subjects: ")
input1 = float(input("Subject 1: "))
input2 = float(input("Subject 2: "))
input3 = float(input("Subject 3: "))
total_marks = input1 + input2 + input3
average = round(total_marks/3, 2)

if average > 100:
    print("Average marks cannot be greater than 100")
    exit()

def getGrade():
    if 100 <=average and average >= 80:
        return 'A+'
    elif average >= 70:
        return 'A'
    elif average >= 60:
        return 'B'
    elif average >= 50:
        return 'C'  
    else:
        return "F"

print(f"Student Name: {a}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average}")
print(f"Grade: {getGrade()}")
