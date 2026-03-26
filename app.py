while True:
    print("\n===== Study Assistant =====")
    print("1. Take a quiz")
    print("2. View past scores")
    print("3. Exit")
    menu = input("What do you want to do (1/2/3): ")

    if menu == "1":
        name = input("Enter your name: ")
        topics = {
            "biology": {
                "what is the powerhouse of cell?": "mitochondria",
                "how many chambers does heart have?": "4",
                "what gas does plants absorb?": "carbon dioxide"
            },
            "physics": {
                "what is newton's first law?": "inertia",
                "what is the unit of force?": "newton",
                "what is the speed of light?": "3x10^8"
            },
            "history": {
                "who wrote the national anthem of india?": "rabindranath tagore",
                "in which year did india get independence?": "1947",
                "who is known as father of the nation?": "mahatma gandhi"
            }
        }
        print("Available topics:", list(topics.keys()))
        score = 0
        choice = input("Enter your choice: ").lower()
        if choice not in topics:
            print("Invalid topic! Please choose from available topics.")
        else:
            questions = topics[choice]
            for question, ans in questions.items():
                user_ans = input(question + " ").lower()
                if user_ans == ans:
                    print("Correct answer!\n")
                    score += 1
                else:
                    print(f"Wrong answer, correct answer was: {ans}\n")
            print(f"Your total score is {score}/{len(questions)}")
            percent = (score / len(questions)) * 100
            print(f"Your percentage: {percent:.1f}%")
            import datetime
            now=datetime.datetime.now()
            f = open("scores.txt", "a")
            f.write(f"{name} | {now.strftime('%d-%m-%Y %H %M')} |Topic: {choice} | Score: {score}/{len(questions)}\n")
            f.close()

    elif menu == "2":
        f = open("scores.txt", "r")
        print("\n--- Past Scores ---")
        print(f.read())
        f.close()

    elif menu == "3":
        print("Goodbye! Keep studying! 👋")
        break

    else:
        print("Invalid choice! Enter 1, 2 or 3.")