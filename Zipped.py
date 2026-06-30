# Read N (number of students) and X (number of subjects)
N, X = map(int, input().split())

# Gather the scores for each subject into a nested list
subject_scores = []
for _ in range(X):
    subject_scores.append(list(map(float, input().split())))


for student_marks in zip(*subject_scores):
    # Calculate the average score for the student
    average = sum(student_marks) / X
    # Print formatted to 1 decimal place
    print(f"{average:.1f}")