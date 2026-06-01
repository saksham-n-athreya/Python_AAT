# =========================================================
# SMART CAMPUS INFORMATION SYSTEM
# =========================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = []
student_ids = []


# =========================================================
# 1. STUDENT REGISTRATION AND GRADE EVALUATION
# =========================================================

def register_student():

    while True:

        print("\n===== Student Registration =====")

        student_id = int(input("Enter Student ID: "))

        if student_id in student_ids:

            print("Student ID Already Exists")

            continue

        name = input("Enter Student Name: ")

        age = int(input("Enter Age: "))

        score = float(input("Enter Exam Score: "))

        # Grade Evaluation
        if 90 <= score <= 100:

            grade = "A"

            remark = "Excellent"

        elif score >= 75:

            grade = "B"

            remark = "Very Good"

        elif score >= 60:

            grade = "C"

            remark = "Good"

        elif score >= 40:

            grade = "D"

            remark = "Average"

        else:

            grade = "F"

            remark = "Needs Improvement"

        student = {

            "id": student_id,

            "name": name,

            "age": age,

            "score": score,

            "grade": grade,

            "remark": remark,

            "courses": [],

            "marks": {}

        }

        students.append(student)

        student_ids.append(student_id)

        print("\nStudent Registered Successfully")

        print("Grade:", grade)

        print("Remark:", remark)

        choice = input(
            "\nDo you want to add another student? (yes/no): "
        )

        if choice.lower() != "yes":

            break


# =========================================================
# 2. COURSE ENROLLMENT MANAGEMENT
# =========================================================

def enroll_courses():

    if not students:

        print("No Students Registered")

        return

    while True:

        sid = int(input("\nEnter Student ID: "))

        found = False

        for student in students:

            if student["id"] == sid:

                found = True

                print("Student Name:",
                      student["name"])

                max_courses = 5

                while True:

                    if len(student["courses"]) >= max_courses:

                        print("Maximum Course Limit Reached")

                        break

                    course_name = input(
                        "Enter Course Name (or done): "
                    ).title()

                    if course_name.lower() == "Done".lower():

                        break

                    credits = input("Enter Credits: ")

                    if not credits.isdigit():

                        print("Invalid Credits")

                        continue

                    credits = int(credits)

                    if credits <= 0:

                        print("Credits Must Be Positive")

                        continue

                    student["courses"].append(
                        (course_name, credits)
                    )

                    print("Course Added Successfully")

                print("\n===== Enrollment Summary =====")

                total_credits = 0

                for course, credit in student["courses"]:

                    print(course,
                          "-",
                          credit,
                          "Credits")

                    total_credits += credit

                print("Total Courses:",
                      len(student["courses"]))

                print("Total Credits:",
                      total_credits)

        if not found:

            print("Student ID Not Found")

        choice = input(
            "\nDo you want to enroll courses for another student? (yes/no): "
        )

        if choice.lower() != "yes":

            break


# =========================================================
# 3. EVENT PARTICIPATION ANALYSIS
# =========================================================

def event_analysis():

    print("\n===== Event Participation Analysis =====")

    event_A = set(
        input(
            "Enter Event A Participants: "
        ).split()
    )

    event_B = set(
        input(
            "Enter Event B Participants: "
        ).split()
    )

    common = event_A & event_B

    all_students = event_A | event_B

    only_A = event_A - event_B

    print("\nCommon Participants:",
          common)

    print("All Participants:",
          all_students)

    print("Only Event A Participants:",
          only_A)


# =========================================================
# 4. SORT STUDENT IDS
# =========================================================

def sort_student_ids():

    if not student_ids:

        print("No Student IDs Available")

        return

    ids = student_ids.copy()

    n = len(ids)

    # Bubble Sort
    for i in range(n):

        for j in range(0, n - i - 1):

            if ids[j] > ids[j + 1]:

                ids[j], ids[j + 1] = (
                    ids[j + 1],
                    ids[j]
                )

    print("\nSorted Student IDs:")

    print(ids)


# =========================================================
# 5. SEARCH STUDENT ID
# =========================================================

def search_student_id():

    if not student_ids:

        print("No Student IDs Available")

        return

    target = int(
        input(
            "Enter Student ID to Search: "
        )
    )

    ids = sorted(student_ids)

    low = 0

    high = len(ids) - 1

    found = False

    while low <= high:

        mid = (low + high) // 2

        if ids[mid] == target:

            print(
                "Student ID Found at Position",
                mid
            )

            found = True

            break

        elif ids[mid] < target:

            low = mid + 1

        else:

            high = mid - 1

    if not found:

        print("Student ID Not Found")


# =========================================================
# 6. STUDENT FEE CALCULATION
# =========================================================

def calculate_fee(
    tuition_fee,
    hostel_fee=0,
    transport_fee=0
):

    return (
        tuition_fee +
        hostel_fee +
        transport_fee
    )


def fee_module():

    sid = int(input("Enter Student ID: "))

    found = False

    for student in students:

        if student["id"] == sid:

            found = True

            print("Student Name:",
                  student["name"])

            tuition = float(
                input("Enter Tuition Fee: ")
            )

            hostel = float(
                input("Enter Hostel Fee: ")
            )

            transport = float(
                input("Enter Transport Fee: ")
            )

            total = calculate_fee(
                tuition,
                hostel,
                transport
            )

            print("Total Fee =", total)

    if not found:

        print("Student ID Not Found")


# =========================================================
# 7. SAVE RECORDS TO TXT FILE
# =========================================================

def save_records():

    with open(
        "student_records.txt",
        "w"
    ) as file:

        for student in students:

            file.write(
                f"\nID: {student['id']}\n"
            )

            file.write(
                f"Name: {student['name']}\n"
            )

            file.write(
                f"Age: {student['age']}\n"
            )

            file.write(
                f"Score: {student['score']}\n"
            )

            file.write(
                f"Grade: {student['grade']}\n"
            )

            file.write(
                f"Remark: {student['remark']}\n"
            )

            file.write("\nCourses:\n")

            for course, credit in student["courses"]:

                file.write(
                    f"{course}"
                    f" - "
                    f"{credit} Credits\n"
                )

            file.write(
                "--------------------------\n"
            )

    print("\nRecords Saved Successfully")


# =========================================================
# 8. READ STUDENT RECORDS
# =========================================================

def read_records():

    try:

        with open(
            "student_records.txt",
            "r"
        ) as file:

            print(
                "\n===== Student Records ====="
            )

            print(file.read())

    except FileNotFoundError:

        print("File Not Found")


# =========================================================
# 9. DIRECTORY SCANNING
# =========================================================

class MissingFileOrFolderError(Exception):

    pass


def scan_directory(path):

    try:

        if not os.path.exists(path):

            raise FileNotFoundError(
                "Invalid Directory Path"
            )

        print(f"\nScanning Directory: {path}\n")

        for root, dirs, files in os.walk(path):

            level = (
                root.replace(path, "")
                .count(os.sep)
            )

            indent = " " * 4 * level

            print(
                f"{indent}"
                f"{os.path.basename(root)}/"
            )

            sub_indent = " " * 4 * (level + 1)

            for f in files:

                print(
                    f"{sub_indent}{f}"
                )

            if not files and not dirs:

                raise MissingFileOrFolderError(
                    f"Empty Folder: {root}"
                )

    except FileNotFoundError as e:

        print("Error:", e)

    except MissingFileOrFolderError as e:

        print("Custom Error:", e)

    except Exception as e:

        print("Unexpected Error:", e)


# =========================================================
# 10. ENTER STUDENT MARKS
# =========================================================

def enter_marks():

    if not students:

        print("No Students Registered")

        return

    for student in students:

        print(
            f"\nEnter Marks for "
            f"{student['name']} "
            f"(ID: {student['id']})"
        )

        if not student["courses"]:

            print("No Courses Enrolled")

            continue

        student["marks"] = {}

        for course, credit in student["courses"]:

            marks = int(
                input(
                    f"{course} Marks: "
                )
            )

            student["marks"][course] = marks

    print("\nAll Student Marks Added Successfully")


# =========================================================
# 11. SAVE PERFORMANCE CSV
# =========================================================

def save_performance_csv():

    performance_data = []

    for student in students:

        row = {

            "ID": student["id"],

            "Name": student["name"]

        }

        for subject, marks in student["marks"].items():

            row[subject] = marks

        performance_data.append(row)

    df = pd.DataFrame(performance_data)

    df.to_csv(
        "student_performance.csv",
        index=False
    )

    print(
        "\nPerformance CSV File Created Successfully"
    )


# =========================================================
# 12. STUDENT PERFORMANCE ANALYSIS
# =========================================================

def performance_analysis():

    try:

        df = pd.read_csv(
            "student_performance.csv"
        )

        print("\n===== Raw Data =====")

        print(df.head())

        # Exclude ID and Name
        numeric_columns = df.columns[2:]

        print(
            "\n===== Statistical Summary ====="
        )

        print(
            df[numeric_columns].describe()
        )

        scores = df[
            numeric_columns
        ].to_numpy()

        mean_scores = np.nanmean(
            scores,
            axis=0
        )

        print("\n===== Mean Scores =====")

        for i in range(
            len(numeric_columns)
        ):

            print(
                numeric_columns[i],
                ":",
                mean_scores[i]
            )

        print("\n===== Top Performers =====")

        for subject in numeric_columns:

            top_student = df.loc[
                df[subject].idxmax(),
                "Name"
            ]

            print(
                subject,
                ":",
                top_student
            )

        # GRAPH 1
        plt.figure()

        plt.bar(
            numeric_columns,
            mean_scores
        )

        plt.title(
            "Average Scores per Subject"
        )

        plt.xlabel("Subjects")

        plt.ylabel("Average Marks")

        # GRAPH 2
        plt.figure()

        df.plot(
            x="Name",
            y=numeric_columns,
            kind="bar"
        )

        plt.title(
            "Student Performance Comparison"
        )

        plt.xlabel("Students")

        plt.ylabel("Marks")

        plt.show()

    except FileNotFoundError:

        print("CSV File Not Found")

    except Exception as e:

        print("Unexpected Error:", e)


# =========================================================
# MAIN MENU
# =========================================================

while True:

    print("\n====================================")

    print(" SMART CAMPUS INFORMATION SYSTEM ")

    print("====================================")

    print("1. Register Student")

    print("2. Enroll Courses")

    print("3. Event Participation Analysis")

    print("4. Sort Student IDs")

    print("5. Search Student ID")

    print("6. Calculate Student Fee")

    print("7. Save Records to TXT File")

    print("8. Read Student Records")

    print("9. Scan Directory")

    print("10. Enter Student Marks")

    print("11. Save Performance CSV")

    print("12. Student Performance Analysis")

    print("13. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":

        register_student()

    elif choice == "2":

        enroll_courses()

    elif choice == "3":

        event_analysis()

    elif choice == "4":

        sort_student_ids()

    elif choice == "5":

        search_student_id()

    elif choice == "6":

        fee_module()

    elif choice == "7":

        save_records()

    elif choice == "8":

        read_records()

    elif choice == "9":

        path = input(
            "Enter Directory Path: "
        )

        scan_directory(path)

    elif choice == "10":

        enter_marks()

    elif choice == "11":

        save_performance_csv()

    elif choice == "12":

        performance_analysis()

    elif choice == "13":

        print("\nExiting Program...")

        break

    else:

        print("Invalid Choice")
