score = input("Enter a score, or type 'done' to exit: ")
#list to store the score values
good_score_list = []
#variable to store the number of smart students
count = 0
#80 and above means you are a smart student
smart_score = 80
#max score is 100
max_score = 100
#min score is 0
min_score = 0
while True:
    try:
        #this block will check if the score is an integer and if it is then it will calculate if the score is good
        score = int(score)
        if max_score >= score >= smart_score:
            good_score_list.append(score)
            score = input("Enter a score, or type 'done' to exit: ")
        elif smart_score > score >= min_score:
            score = input("Enter a score, or type 'done' to exit: ")            
        elif score < min_score:
            print("Invalid score!")
            score = input("Enter a score, or type 'done' to exit: ")
        elif score > max_score:
            print("Invalid score!")
            score = input("Enter a score, or type 'done' to exit: ")
    except ValueError:
        #if the score isn't a integer
        if score == "done":
            break
        else:
            print("Invalid score!")
            score = input("Enter a score, or type 'done' to exit: ")

for item in good_score_list:
    count += 1

if count == 1:
    print(f"This class has {count} smart student!")
else:
    print(f"This class has {count} smart students!")
