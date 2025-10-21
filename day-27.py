# Simple Question Answer Project in Python
quiz=[
    {
        "question": "What year was Python first released?",
        "options": ["A. 1989", "B. 1991", "C. 2000", "D. 1995"],
        "answer": "B"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["A. Curly braces {}", "B. Parentheses ()", "C. Indentation", "D. Quotation marks"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used for function in Python?",
        "options": ["A. fun", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    }
]

score=0
print("🧠 Welcome to the Python Quiz!")
print("--------------------------------\n")

for i, q in enumerate(quiz,start=1):
    print(f"Q{i}: {q['question']}")
    for o in q['options']:
        print(o)

    answer=input("Enter your ans (A\B\C\D): ").upper()
    
    if answer == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}\n")

print("--------------------------------")
print(f"🎯 Your final score: {score}/{len(quiz)}")

if score == len(quiz):
    print("🏆 Excellent! You're a Python master!")
elif score >= len(quiz)//2:
    print("👍 Good job! Keep practicing.")
else:
    print("📚 Keep learning and try again!")


