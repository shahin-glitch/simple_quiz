# Quiz Game in python

def run_quiz():
    # list of questions, here we goooo
    questions = [
        {
            "question": "Which language in known for its simplicity and is beginner-friendly?🤔📍",
            "options": ["A. C++", "B. Rust", "C. Python", "D. none of the above"],
            "answer": "C"
        },
        {
            "question": "Which language is used for android development?🧩",
            "options": ["A. Swift", "B. Kotlin", "C. PHP", "D. Ruby"],
            "answer": "B"
        },{
            "question" : "Which language is used to interact with databases?📊",
            "options": ["A. Javascript", "B. Python", "C. SQL", "D. Option A and B"],
            "answer": "C"
        },{
            "question" : "Which language is mainly used for iPhone(iOS) apps?🔒🛡️",
            "options": ["A. Swift", "B. Java", "C. C#", "D. Go"],
            "answer" : "A"
        }
    ]
    
    
    # assume that score is 0
    score = 0
    print("\nWelcome to the the Quiz Game!🤓\n")
    print("Lets goooooo siuuuuuuuuu......📗📝\n")
    
    
    # loop through question
    
    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        
        for option in q["options"]:
            print(option)
        
        # taking user input
        user_answer = input("Enter your answer (A / B / C / D) ⏳⌛").upper()
        
        # Using if else loop 
        if user_answer == q["answer"]:
            print("Correct!✅\n")
            score += 1
        
        else:
            print(f"Wrong!❌ Correct answer is {q['answer']}\n☹️") 
            
            
    # Final score 
    
    print("Quiz completed!⏰")
    print(f"Your Score: {score} / {len(questions)}🤨") 
    
# Run the quiz
run_quiz()        
                      