import random


class ForfeitGenerator:
    def __init__(self):
        self.forfeits = {
            "EASY": [
                "Do 5 jumping jacks at the school field.",
                "Wave and smile at the first person you see in the library.",
                "Email a lecturer saying, 'Hi! Hope you're doing well. Lovely weather today!'",
                "Take a selfie with a building on campus and share it with your friends.",
                "Compliment a staff member on their great work.",
                "Hum the SUTD anthem in front of your friends.",
                "Recite the SUTD motto while clapping your hands rhythmically.",
                "Find a friend and tell them a random fun fact about SUTD.",
                "Walk across the canteen while balancing a book on your head.",
                "Pretend to be a robot for 30 seconds in front of your group."
            ],
            "NORMAL": [
                "Sing a line from your favourite song while in the campus centre.",
                "Act like a tour guide and introduce the fried food vending machine to your group.",
                "Write a funny haiku about the school and share it with your friends.",
                "Give a 1-minute impromptu speech to anyone on why SUTD is awesome.",
                "Do 10 push-ups in the cafeteria while saying 'SUTD Rocks!'",
                "Spin around 5 times and then walk in a straight line.",
                "Talk to the vending machine as if it were your friend for 30 seconds.",
                "Say 'hello' in three different languages to three strangers on campus.",
                "Balance a pencil on your nose for 10 seconds without dropping it."
            ],
            "HARD": [
                "Do a dramatic reading of your last text message to your friends.",
                "Mimic your favourite lecturer's mannerisms for 1 minute.",
                "Do 10 star jumps in the busiest part of campus.",
                "Propose an SUTD-themed dance move and demonstrate it.",
                "Take an exaggerated slow-motion walk across the library.",
                "Call out 'Who wants to study?' in the library and see who responds.",
                "Create a handshake that represents SUTD's motto and teach it to your friends.",
                "Pretend you’re being interviewed for a TV show about SUTD for 1 minute.",
                "Balance three random items from your bag on top of your head."
            ]
        }

    # Returns a random forfeit based on the difficulty level.
    def get_forfeit(self, difficulty):
        if difficulty in self.forfeits:
            return random.choice(self.forfeits[difficulty])
        else:
            return "Invalid difficulty level. Please choose 'easy', 'normal', or 'hard'."


# Interfacte for interaction
def main():
    forfeit_gen = ForfeitGenerator()

    print("Welcome to the SUTD Tic Tac Toe Forfeit Generator!")
    print("Choose a difficulty level for your forfeit: easy, medium, hard")

    while True:
        difficulty = input(
            "Enter difficulty level (or type 'exit' to quit): ").lower()
        if difficulty == "exit":
            print("Goodbye! Have fun learning about SUTD!")
            break

        forfeit = forfeit_gen.get_forfeit(difficulty)
        print(f"Your forfeit: {forfeit}\n")


if __name__ == "main":
    main()
