class SimpleWeatherAgent:
    def __init__(self):
        pass

    def perceive(self, condition):
        """Receives environment condition."""
        print(f"\n👁️ sensed: {condition}")
        return self.decide(condition)

    def decide(self, condition):
        """Decides what to do based on condition."""
        if condition == "rainy":
            return self.act("Take an umbrella ☔")
        elif condition == "sunny":
            return self.act("Wear sunglasses 😎")
        elif condition == "cold":
            return self.act("Wear A Jacket 🧥")
        else:
            return self.act("Do nothing")

    def act(self, action):
        """Acts based on the decision"""
        print(f"🏃‍♂️ Action: {action}")
        return action

#main program using input 
if __name__== "__main__":
    agent = SimpleWeatherAgent()

    print("☁️ Simple Weather AI Agent")
    print("Type 'exit to stop.\n")

    while True:
        condition = input("Enter weather condition (sunny, rainy, cold,etc):").lower()
        if condition == "exit":
            print("Exiting agent.")
            break
        agent.perceive(condition)
