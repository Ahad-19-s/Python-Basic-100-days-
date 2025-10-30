questions = [
    ["Which language is used to create Android apps?", "Python", "Java", "C#", "C++", 2],
    ["Which company developed the C language?", "Microsoft", "Apple", "Bell Labs", "Google", 3],
    ["Who is known as the father of computers?", "Charles Babbage", "Alan Turing", "John von Neumann", "Tim Berners-Lee", 1],
    ["What does HTML stand for?", "HyperText Markup Language", "HyperText Markdown Language", "HighText Machine Language", "Hyper Transfer Markup Language", 1],
    ["Which of the following is a backend language?", "HTML", "CSS", "Python", "XML", 3],
    ["Which keyword is used to define a function in Python?", "func", "define", "def", "lambda", 3],
    ["Which language was used to create Facebook?", "Java", "PHP", "C#", "Python", 2],
    ["What is the extension of a Python file?", ".pyt", ".pt", ".py", ".p", 3],
    ["Which of the following is not an OOP concept?", "Encapsulation", "Polymorphism", "Compilation", "Inheritance", 3],
    ["Which of these is a Python web framework?", "Django", "React", "Angular", "Vue", 1]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0  # total prize money

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion for {levels[i]} taka:")
    print(question[0])
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")

    try:
        reply = int(input("Enter your answer (1-4) or 0 to quit: "))
    except ValueError:
        print("⚠️ Please enter a valid number between 0–4.")
        continue

    if reply == 0:
        print("🚪 You chose to quit the game.")
        break

    if reply == question[-1]:
        print(f"✅ Correct! You have won {levels[i]} taka.")
        money = levels[i]  # update current winning amount
    else:
        print("❌ Wrong answer! Game over.")
        # safe levels (like KBC checkpoints)
        if i >= 6:
            money = 10000000
        elif i >= 4:
            money = 100000
        elif i >= 2:
            money = 1000
        else:
            money = 0
        break

print(f"\n💰 Total money you won: {money} taka 🎉")
