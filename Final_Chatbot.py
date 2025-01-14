import random
import re
import os

class Bot:
    # Lists of negative responses and exit commands
    negative_response = ("no", "nope", "never", "not a chance", "sorry")
    exit_cmd = ("exit", "bye", "goodbye", "quit", "pause")

    def __init__(self):
        # Dictionary mapping intents to regex patterns
        self.responses = {
            'Product_Information': r'.*\s*product.*',
            'technical_support': r'.*\b(technical|support)\b.*',
            'general_query': r'.*\b(help|done|okay)\b.*'
        }

    def greet(self):
        # Greeting and user interaction
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.name = input("\nHello! I'm your chatbot. What is your name? \n")
            if self.name.strip():
                break
            print("Before proceeding, you have to provide a name!\n")

            
        cb_res = input(f"\nHey {self.name}, how can I assist you today? \n")
        if cb_res.lower() in self.negative_response:
            print("Okay, have a great day!")
            return
        self.chat()

    def exit(self, reply):
        # Checking if user wants to exit
        for command in self.exit_cmd:
            if command in reply.lower():
                print("\nIf you have any more questions in the future, feel free to ask. Have a great day!")
                return True
        return False

    def chat(self):
        # Main chat loop
        reply = input("\nPlease tell me your query! \n").lower()
        while not self.exit(reply):
            reply = input(self.match_reply(reply))  # Pass reply to match_reply

    def match_reply(self, reply):
        # Matching user input to responses
        for intent, regex_pattern in self.responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match and intent == 'Product_Information':
                return self.product_info()
            elif found_match and intent == 'technical_support':
                return self.technical_support()
            elif found_match and intent == 'general_query':
                return self.general_query()
        return self.no_match()

    def product_info(self):
        # Responses related to product
        resp = (
            "\nWe are proud to offer a premium-quality product that has gained widespread acclaim,"
            "trusted by customers in over 10 countries worldwide."
            "Our commitment to excellence ensures that each product delivers exceptional performance and reliability,"
            "making it a preferred choice globally.\n",
            "\nYou can find all the products on the website.\n"
        )
        return random.choice(resp)

    def technical_support(self):
        # Responses related to technical support
        resp = (
            "\nOur technical support team is dedicated to ensuring your seamless experience with our products.\n",
            "\nPlease visit our website for technical support.\n"
        )
        return random.choice(resp)

    def general_query(self):
        # Responses to general queries
        resp = (
            "\nHow can I assist you further?\n",
            "\nIs there anything you'd like to know?\n"
        )
        return random.choice(resp)

    def no_match(self):
        # Responses for unmatched queries
        resp = (
            "Could you provide more details?\n",
            "I see. Could you elaborate?\n",
            "Why do you say that?\n",
            "I'd like to understand more about that.\n",
            "Could you expand on that?\n",
            "I'm curious to know more.\n",
            "Could you clarify your thoughts?\n",
        )
        return random.choice(resp)

# Instantiate and start the chatbot
b = Bot()
b.greet()
