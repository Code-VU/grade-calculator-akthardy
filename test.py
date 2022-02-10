def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    scr = float(input("Enter score:"))
    if scr >= 0 and scr <.6:
        grade = 'F' 
    elif scr >= .6 and scr <.7:
        grade = 'D' 
    elif scr >= .7 and scr <.8:
        grade = 'C' 
    elif scr >= .8 and scr <.9:
        grade = 'B' 
    elif scr >= .9 and scr <=1:
        grade = 'A'
    else:
         grade = "error"
    print(grade)

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculateGrade()
