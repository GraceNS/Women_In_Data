def mark_grade(mark):
    if mark > 90:
        return "A*"
    elif mark > 80:
        return "A"
    elif mark > 70:
        return "B"
    elif mark > 60:
        return "C"
    else:
        return "F"
    
mark = input("Enter your mark: ")
target_grade = input("Enter your target grade: ")
grade = mark_grade(int(mark))
print("Your grade is " + grade + " and your target grade was " + target_grade)

if target_grade == grade:
    print("Well done on achieving your target grade!")

elif target_grade == "A*" and grade != "A*":
    print("Unfortunately you did not achieve your target grade.")

elif grade == "A*" and target_grade != "A*":
    print("Well done! You did better than your target grade!")

#elif target_grade == "A":
 #   if grade == "B" or "C" or "F":
  #      print("Unfortunately you did not achieve your target grade.")
   # elif grade == "A*":
    #    print("Well done! You did better than your target grade!")

#elif target_grade == "B":
 #   if grade == "A*" or "A":
  #      print("Well done! You did better than your target grade!")
   # elif grade == "C" or "F":
    #    print("Unfortunately you did not achieve your target grade.")

#elif target_grade == "C":
 #   if grade == "F":
  #      print("Unfortunately you did not achieve your target grade.")
   # else:
    #    print("Well done! You did better than your target grade!")

#elif target_grade == "F":
 #   print("Well done! You did better than your target grade!")