'''
Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

    Score   Grade
    >= 0.9     A
    >= 0.8     B
    >= 0.7     C
    >= 0.6     D
    < 0.6     F

'''

score = input('Enter score: ')

def computegrade(score):

    try:
        score = float(score)
        if score >1 or score<0:
            return('Bad score')
        elif score >= 0.9:
            return('Grade A')
        elif score >= 0.8:
            return('Grade B')
        elif score >= 0.7:
            return('Grade C')
        elif score >= 0.6:
            return('Grade D')
        else:
            return('Grade F')

    except:
        return('Bad score')

print(computegrade(score))