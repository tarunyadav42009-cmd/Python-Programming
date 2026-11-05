#Older Version

"""# Marksheet for Students
print("Please Enter the marks as whole number!")

# Input marks for 5 subjects
Math = int(input("Enter the marks in Maths: "))
Eng = int(input("Enter the marks in English: "))
Hind = int(input("Enter the marks in Hindi: "))
Sci = int(input("Enter the marks in Science: "))
Sco_Sci = int(input("Enter the marks in Social Science: "))

# Calculations
Total = Math + Eng + Hind + Sci + Sco_Sci
Avg = Total / 5  # Python 3 automatically converts division to float

# Output results
print("\nTotal =", Total)
print("Avg =", Avg)
if(Math<35 or Hind<35 or Sci<35 or Sco_Sci<35 or Eng<35):
    print("Remark: Fail!")
else:
    print("Remark: Pass!")

# Grading Logic
if Avg < 33:
    print("Grade: Fail!")
elif 33 <= Avg <= 60:  
    print("Grade: Pass!")
elif 60 < Avg <= 75:
    print("Grade: First Class!")
else:  # Handles everything above 75
    print("Grade: First Class with Distinction!")

"""
#Improved Version of code 
"""
Marksheet Generator Application
-------------------------------
Author: Developer
Description: Accepts, validates, and processes student marks for five core subjects.
             Calculates totals, averages, passing status, and final grade classifications.
"""

print("--- Marksheet Generator ---")
print("Please enter the marks as whole numbers between 0 and 100.\n")

# Define the core curriculum subjects
subjects = ["Maths", "English", "Hindi", "Science", "Social Science"]
marks = {}

# Data Acquisition and Validation Loop
for sub in subjects:
    while True:
        try:
            score = int(input(f"Enter the marks in {sub}: "))
            
            # Ensure the score falls within the standard academic range
            if 0 <= score <= 100:
                marks[sub] = score
                break
            else:
                print("Invalid input! Marks must be between 0 and 100.")
                
        except ValueError:
            print("Invalid input! Please enter a valid whole number.")

# Academic Metrics Calculation
total_marks = sum(marks.values())
average_marks = total_marks / len(subjects)

# Output Results Generation
print("\n" + "="*30)
print(f"Total Marks : {total_marks}")
print(f"Average     : {average_marks:.2f}")

# Pass/Fail Threshold Verification
# A student is marked as 'Fail' if any single subject falls below the 35-mark threshold.
has_failed_subject = any(score < 35 for score in marks.values())

if has_failed_subject:
    print("Remark      : Fail!")
else:
    print("Remark      : Pass!")

# Final Grade Classification
# Determines academic standing based on the overall percentage/average.
if average_marks < 33:
    print("Grade       : Fail!")
elif average_marks < 60:
    print("Grade       : Pass!")
elif average_marks <= 75:
    print("Grade       : First Class!")
else:
    print("Grade       : First Class with Distinction!")

print("="*30)
