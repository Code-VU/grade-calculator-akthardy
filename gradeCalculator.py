def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    scr = float(input("Enter score: "))
    if scr >= 0.9 and scr < 1:
        grade = 'A'
    elif scr >= 0.8 and scr < 0.9:
        grade = 'B' 
    elif scr >= 0.7 and scr < 0.8:
        grade = 'C' 
    elif scr >= 0.6 and scr < 0.7:
        grade = 'D'  
    elif scr >= 0 and scr < 0.6:
        grade = 'F'         
    else:
        grade = 'Error'    
    print(grade)         

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateGrade()