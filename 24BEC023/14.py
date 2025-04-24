def calculategrade(marks):
    if marks == "Absent":
        return "NA"
    elif marks <= 39:
        return "F"
    elif 40 <= marks <= 44:
        return "P"
    elif 45 <= marks <= 49:
        return "C"
    elif 50 <= marks <= 54:
        return "B"
    elif 55 <= marks <= 59:
        return "B+"
    elif 60 <= marks <= 69:
        return "A"
    elif 70 <= marks <= 79:
        return "A+"
    elif 80 <= marks <= 100:
        return "O"
    else:
        return "Invalid Marks"

def main():
    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    markslist = []
    fail = False

    for subject in subjects:
        marksinput = input(f"Enter marks for {subject} (Enter 'Absent' if not appeared): ").strip()
        if marksinput.lower() == "absent":
            markslist.append("Absent")
            fail = True
        else:
            marks = int(marksinput)
            markslist.append(marks)
            if marks <= 39:
                fail = True

    total = sum([marks if isinstance(marks, int) else 0 for marks in markslist])
    average = total / len(subjects)

    print("\nResults:")
    for i, marks in enumerate(markslist):
        grade = calculategrade(marks if isinstance(marks, int) else "Absent")
        print(f"{subjects[i]}: Marks = {marks}, Grade = {grade}")

    print(f"\nTotal Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print("Result:", "Fail" if fail else "Pass")
main ()
calculategrade(marks)
