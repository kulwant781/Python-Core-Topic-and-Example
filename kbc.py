def kbc_game():
    # List of questions, options, and correct answers
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Who wrote the Indian National Anthem?",
            "options": ["A. Rabindranath Tagore", "B. Sarojini Naidu", "C. Bankim Chandra Chatterjee", "D. Subhas Chandra Bose"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "What is the largest mammal?",
            "options": ["A. Elephant", "B. Blue Whale", "C. Great White Shark", "D. Giraffe"],
            "answer": "B"
        }
    ]

    # Prize money for each question
    prize_money = [1000, 5000, 10000, 50000]

    # Variables to keep track of progress
    total_prize = 0

    # Loop through each question
    for i, question in enumerate(questions):
        print(f"Question {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)
        
        # Take user's answer
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        # Check if the answer is correct
        if user_answer == question["answer"]:
            total_prize += prize_money[i]
            print(f"Correct! You have won ₹{prize_money[i]}.\n")
        else:
            print("Wrong answer! Game over.\n")
            break

    print(f"Game over! You are taking home ₹{total_prize}.")

# Run the KBC game
if __name__ == "__main__":
    kbc_game()
