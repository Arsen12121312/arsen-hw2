class SuperHero:
    def __init__(self, name, hp, people):
        self.name = name
        self.hp = hp
        self.people = people

    def fly(self):
        return False

    def attack(self):
        return self.hp * 2

    def true_phrase(self):
        return f"{self.name} is True!"


class AirHero(SuperHero):
    def __init__(self, name, hp, people, damage):
        super().__init__(name, hp, people)
        self.damage = damage
        self.fly = True

    def attack(self):
        return self.hp ** 2


class GroundHero(SuperHero):
    def __init__(self, name, hp, people, damage):
        super().__init__(name, hp, people)
        self.damage = damage

    def attack(self):
        return self.hp ** 2


class SpaceHero(SuperHero):
    def __init__(self, name, hp, people, damage):
        super().__init__(name, hp, people)
        self.damage = damage
        self.fly = True

    def attack(self):
        return self.hp ** 2


class Villain(SpaceHero):
    def __init__(self, name, hp, people, damage):
        super().__init__(name, hp, people, damage)
        self.people = "monster"

    def gen_x(self):
        pass

    def crit(self, target):
        return target.hp - (self.damage ** 2)


air_hero = AirHero("Airman", 100, "people", 20)
ground_hero = GroundHero("Earthman", 150, "people", 30)
space_hero = SpaceHero("Spaceman", 200, "people", 40)
villain = Villain("Villain", 300, "monster", 50)

print(air_hero.true)