MAXGRADE = 100
MINGRADE = 0

def finalMarkToPass(gradeWithWeights):
    currentGrade = 0
    finalWeight = 100
    
    # Iterate through each given grade and its weight to calculate the weighted sum
    for grade, weight in gradeWithWeights:
        currentGrade += grade * (weight / 100)
        finalWeight -= weight

    # Check all possible final exam scores
    for score in range(MINGRADE, MAXGRADE +1):
        if finalWeight > 0:
            grade = (score * (finalWeight / 100)) + currentGrade
            print(f"Final exam score: {score} | Grade {grade:.2f}")
        else:
            print(f"Final exam score: {score} | Grade {currentGrade:.2f}")

finalMarkToPass([
    (100, 5),
    (100, 5),
    (100, 5),
    (100, 20)])
