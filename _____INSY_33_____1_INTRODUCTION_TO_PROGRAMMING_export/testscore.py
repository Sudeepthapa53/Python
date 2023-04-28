def average_score(score1,score2,score3,score4,score5): #defines average score
    return (score1+score2+score3+score4+score5)/5 #returns average from the sum

def letter_grade(score): 
    if score>=90:
        return "A" 
    elif score>=80:
        return "B" 
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
#returns score from the given percentage
def main():
    score1=float(input("Enter test score1:"))
    score2=float(input("Enter test score2:"))
    score3=float(input("Enter test score3:"))
    score4=float(input("Enter test score4:"))
    score5=float(input("Enter test score5:")) #inputting test scores from test 1 to 5 respectively
    print("score","\t\t", "numeric Grade","\t\t", "letter grade") #\t\t is used to create space using tab
    print("----------------------------------------------------")
    print("score 1 :\t\t{:.1f}".format(score1),"\t\t",letter_grade(score1)) 
    print("score 2 :\t\t{:.1f}".format(score2), "\t\t", letter_grade(score2))  
    print("score 3 :\t\t{:.1f}".format(score3), "\t\t", letter_grade(score3))
    print("score 4 :\t\t{:.1f}".format(score4), "\t\t", letter_grade(score4))  
    print("score 5 :\t\t{:.1f}".format(score5), "\t\t", letter_grade(score5))  
    print("----------------------------------------------------")
    avg= average_score(score1,score2,score3,score4,score5) 
    print("Average score : ",avg,"\t\t\t",letter_grade(avg))

main()
