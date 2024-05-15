class BeeElephant:

    def __init__(self, bee_part, elephant_part):
        self.bee_part = bee_part
        self.elephant_part = elephant_part
        self.initial_bee_part = bee_part
        self.initial_elephant_part = elephant_part
    def fly(self):
        return self.bee_part >= self.elephant_part

    def trumpet(self):
        if self.bee_part >= self.elephant_part:
            return 'tu-tu-doo-doo'
        else:
            'wzzz'

    def eat(self, meal, value):
        if meal not in ("nectar", "grass"):
            raise ValueError("Meal must be 'nectar' or 'grass'")

        if meal == "nectar":
            self.bee_part = min(100, self.bee_part + value)
            self.elephant_part = max(0, self.elephant_part - value)

        elif meal == 'grass':
            self.elephant_part = min(100, self.initial_elephant_part + value)
            self.bee_part = max(0, self.initial_bee_part - value)


bee_elephant = BeeElephant(50, 40)

print(f"Can fly: {bee_elephant.fly()}")
print(f"Sound: {bee_elephant.trumpet()}")

bee_elephant.eat("nectar", 20)
print(f"Bee part: {bee_elephant.bee_part}, Elephant part: {bee_elephant.elephant_part}")

bee_elephant.eat("grass", 20)
print(f"Bee part: {bee_elephant.bee_part}, Elephant part: {bee_elephant.elephant_part}")





