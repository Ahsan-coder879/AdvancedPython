import pandas as pd
import random as r
import os

# 1. Read Questions
# Make sure QuestionareDummy.csv has columns: 'Question' and 'Answer'
questionare = pd.read_csv("QuestionareDummy.csv")

# 2. Setup/Load Scores (Prevents losing data on restart)
score_file = "student_score.csv"
if os.path.exists(score_file):
    user_db = pd.read_csv(score_file)
else:
    user_db = pd.DataFrame(columns=["Names", "Score"])

while True:
    print("\n" + "=" * 20)
    print("1. New User Quiz")
    print("2. Exit")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Enter your name: ").strip().title()

        # Check for duplicate users
        if name in user_db["Names"].values:
            print(f"Access Denied: {name} has already taken this quiz.")
            continue

        # 3. Prepare 5-10 random questions safely
        # We use the actual length of the CSV to avoid "Index out of range" errors
        total_rows = len(questionare)
        num_questions = min(10, total_rows)
        random_indices = r.sample(range(total_rows), num_questions)

        score = 0

        print(f"\nWelcome {name}! Answer carefully. One mistake ends the game.")

        # 4. Quiz Loop
        for idx in random_indices:
            row = questionare.iloc[idx]
            print(f"\nQuestion: {row['Question']}")
            user_ans = input("Your Answer: ").strip()

            # FIX: Convert both to string and lower case to prevent comparison errors
            correct_ans = str(row['Answer']).strip()

            if user_ans.lower() == correct_ans.lower():
                print("Correct!")
                score += 1
            else:
                print(f"WRONG! The correct answer was: {correct_ans}")
                print("GAME OVER.")
                break  # Instant end as requested

        # 5. Save Results
        # Using concat because append is deprecated in newer pandas versions
        new_data = pd.DataFrame({"Names": [name], "Score": [score]})
        user_db = pd.concat([user_db, new_data], ignore_index=True)
        user_db.to_csv(score_file, index=False)

        print(f"\nQuiz Finished. {name}, your score: {score}/{num_questions}")

    elif choice == "2":
        print("Closing Program...")
        break
    else:
        print("Invalid input. Please enter 1 or 2.")