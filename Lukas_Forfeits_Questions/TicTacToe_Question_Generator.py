import random

questions_dict = {
    "EASY": [
        "Share an interesting fact about the antique Chinese structures donated by Jackie Chan.",
        "Describe what 'Fifth Row' activities are at SUTD.",
        "Identify the nearest MRT station to SUTD's campus.",
        "Mention one of the co-curricular activities available at SUTD.",
        "Describe the location of the SUTD campus.",
        "Name one of the academic pillars at SUTD.",
        "State the full form of SUTD.",
        "Mention one international university that collaborates with SUTD.",
        "Identify the color associated with SUTD’s branding.",
        "Name one of the student residential blocks at SUTD.",
        "State the year SUTD moved to its permanent campus.",
        "Mention one of the languages in which courses are taught at SUTD.",
        "Name one of the facilities available on the SUTD campus.",
        "State the number of years in SUTD’s undergraduate programme.",
        "Identify the country where SUTD’s partner institution, Zhejiang University, is located.",
        "Name two of the dining options available on the SUTD campus.",
        "Mention one of the sports facilities available at SUTD.",
        "Identify the bus number that comes to SUTD bus stop.",
        "Name one of the annual events held at SUTD.",
        "State the number of academic terms in an SUTD academic year.",
        "Mention one of the support services available to SUTD students."
    ],
    "NORMAL": [
        "Explain the significance of the 400-year-old structures on SUTD's campus.",
        "Discuss the collaboration between SUTD and MIT.",
        "Describe the 'Freshmore' term at SUTD and its purpose.",
        "What is the primary focus of the SUTDio Club?",
        "Which Fifth Row club at SUTD is dedicated to promoting environmental sustainability?",
        "Describe the activities conducted by the SUTD Bands Club.",
        "Which Fifth Row group is responsible for organising drama and theatrical productions?",
        "What is the main objective of the SUTD Energy Club?",
        "Which Fifth Row club focuses on the appreciation and performance of Indian dance forms?",
        "Describe the initiatives undertaken by the SUTD Makerspace Club.",
        "Which Fifth Row group at SUTD is known for its involvement in autonomous robotics?",
        "What are the primary activities of the SUTD Photographic Circle?",
        "Which Fifth Row club is dedicated to the practice and promotion of archery?",
        "Describe the mission of the SUTD Greenprint Club.",
        "Which Fifth Row group focuses on the development and appreciation of modern visual media?",
        "Which Fifth Row club is dedicated to the practice of Muay Thai?",
        "Describe the activities of the SUTD Astronomy Interest Group.",
        "Which Fifth Row club at SUTD is dedicated to the game of Tchoukball?",
        "Describe the initiatives of the SUTD Rotaract Club.",
        "Which Fifth Row group focuses on the appreciation and performance of Chinese orchestral music?",
        "What are the main activities of the SUTD Mountaineering Club?",
        "Which Fifth Row club is dedicated to the practice and promotion of Systema, the Russian martial art?",
        "What is the primary focus of the SUTD Karate Club?",
        "Which Fifth Row club at SUTD is dedicated to the appreciation and performance of a cappella music?",
        "Describe the activities of the SUTD Ultimate Club.",
        "Which Fifth Row group is known for its involvement in the game of squash?",
        "Which Fifth Row club is dedicated to the practice and promotion of taekwondo?"
    ],
    "HARD": [
        "Recite SUTD's motto.",
        "Describe the architectural significance of the SUTD campus design.",
        "Discuss the role of the Lee Kuan Yew Centre for Innovative Cities at SUTD.",
        "Explain the importance of the 'Design Innovation' courses by SUTD.",
        "Name the founding president of SUTD.",
        "Discuss the significance of the collaboration between SUTD and Zhejiang University.",
        "Explain the purpose of the iTrust Research Centre at SUTD.",
        "Describe the focus of the Temasek Labs at SUTD.",
        "Discuss the objectives of the City Form Lab at SUTD.",
        "Explain the role of the O-Lab at SUTD.",
        "Describe the SUTD Gridshell Pavilion project.",
        "Explain the concept of the Urban Network Analysis Toolbox developed at SUTD.",
        "Describe the partnership between SUTD and the Singapore Hokkien Huay Kuan.",
        "Discuss the objectives of the SUTD Academy.",
        "Explain the significance of the SUTD Open House event.",
        "Describe the role of the Humanities, Arts, and Social Sciences cluster at SUTD.",
        "Discuss the importance of interdisciplinary learning at SUTD.",
        "Explain the concept of the Fifth Row activities at SUTD.",
        "Discuss the significance of the SUTD Technology Entrepreneurship Programme.",
        "Explain the role of the SUTD Venture, Innovation and Entrepreneurship Fifth Row.",
        "Describe the objectives of the SUTD Undergraduate Research Opportunities Programme.",
        "Explain the concept of the SUTD PhD Programme."
    ]
}


class QuestionGenerator:
    def __init__(self):
        # Returns a random question based on the difficulty level.
        self.questions = questions_dict.copy()

    def reset_questions(self):
        self.questions = questions_dict.copy()

    def get_question(self, difficulty):
        if difficulty == "2P":
            difficulty = random.choice(["EASY", "NORMAL", "HARD"])
        if difficulty in self.questions:
            difficulty_questions = self.questions[difficulty]
            return difficulty_questions.pop(random.randint(0, len(difficulty_questions)))
        else:
            return "Invalid difficulty level. Please choose 'easy', 'normal', or 'hard'."


# Interfacte for interaction
def main():
    question_gen = QuestionGenerator()

    print("Welcome to the SUTD Tic Tac Toe Question Generator!")
    print("Choose a difficulty level for your question: easy, medium, hard")

    while True:
        difficulty = input(
            "Enter difficulty level (or type 'exit' to quit): ").lower()
        if difficulty == "exit":
            print("Goodbye! Have fun learning about SUTD!")
            break

        question = question_gen.get_question(difficulty)
        print(f"Your Question to be answered: {question}\n")


if __name__ == "main":
    main()
