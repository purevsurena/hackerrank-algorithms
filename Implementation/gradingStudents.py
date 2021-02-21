import os

def gradingStudents(grades):
  rounded_arr = []
  for grade in grades:
    if grade>=38:
      roundedGrade = round(grade / 5)*5
      if grade < roundedGrade:
        if roundedGrade-grade < 3:
          grade=roundedGrade
    rounded_arr.append(grade)
  return rounded_arr

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  grades_count = int(input().strip())

  grades = []

  for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

  result = gradingStudents(grades)

  fptr.write('\n'.join(map(str, result)))
  fptr.write('\n')

  fptr.close()
