# checking the average of a query name 
# getting the average name of the students and in 2 decimal format
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks.keys():
        if key == query_name:
            score = student_marks[key]
            sums = sum(score)/len(score)
            print(format(sums,".2f"))
