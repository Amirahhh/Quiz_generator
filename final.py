import random


print("-----Hello, Welcome! I have some questions for you!-----")
score = 0
questions = 0

quiz_data = [
    {
    "question": "What polygon shape is a stop sign?",
    "answer": "octagon"
    },
    {
    "question": "What is the opposite of up?",
    "answer": "down"
    },
    {
    "question": "What is the chemical formula for water?",
    "answer": "h2o"
    },
    {
    "question": "How many bones are there in an adult human body?",
    "answer": "206"
    },
    {
    "question": "Which U.S. state is known for peaches?",
    "answer": "georgia"
    },
    {
    "question": "Which country occupies half of South America’s western coast?",
    "answer": "chile"
    },
    {
    "question": "Which musical artist is known for her song 'Big Girls Don’t Cry'?",
    "answer": "fergie"
    },
    {
    "question": "If you freeze water, what do you get?",
    "answer": "ice"
    },
    {
    "question": "Which Disney movie is Elsa in?",
    "answer": "frozen"
    },
    {
    "question": "In which year was the hit “Juicy” by The Notorious B.I.G released?",
    "answer": "1994"
    },
    {
    "question": "How many continents are there in the world?",
    "answer": "7"
    },
    {
    "question": "What is the capital of Hawaii? ",
    "answer": "honolulu"
    },
    {
    "question": "What is the name of the toy cowboy in Toy Story?",
    "answer": "woody"
    },
    {
    "question": "What does the F stand for in FBI?",
    "answer": "federal"
    },
    {
    "question": "What Jedi Master spent 800 years training such pupils as Qui-Gon Jinn Obi-Wan Kenobi, Count Dooku and Luke Skywalker?",
    "answer": "yoda"
}
]

q = random.choice(quiz_data)

def continue_going():
    dy = input("Press any key to continue, otherwise, type 'n'   ")
    if dy.lower() == "n":
        total = int((score / questions) * 100)
        print(score, "/", questions)
        print(total, "%")
        if total > 60:
            print("Congratulations, you have a passing score!")
            exit()
        elif total < 60:
            print("Your score is below the passing grade of 60%")    
            exit()
    else:
        return True

while True:
        
    q = random.choice(quiz_data)
    print(q.get('question'))
    answer = input("Your answer:  ").lower()
    questions += 1
    if answer == q.get('answer'):
        print("You got it")
        score += 1
        continue_going()  
    else:
        print("Wrong")
        continue_going() 
    
      
   