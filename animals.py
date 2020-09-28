class Animals:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        return 'животное накормлено'


class Birds(Animals):
    def do_smth(self):
        return 'несет яйца'


class Chicken(Birds):
    representative = 'Курица'

    def make_sounds(self):
        return 'Ко-ко-ко!'


class Goose(Birds):
    representative = 'Гусь'

    def make_sounds(self):
        return 'Га-га-га!'


class Duck(Birds):
    representative = 'Утка'

    def make_sounds(self):
        return 'Кря-кря-кря!'


class MilkAnimals(Animals):
    def do_smth(self):
        return 'доится'


class Cow(MilkAnimals):
    representative = 'Корова'

    def make_sounds(self):
        return 'Му-у-у!'


class Goat(MilkAnimals):
    representative = 'Коза'

    def make_sounds(self):
        return 'Ме-е-е!'


class SheerAnimals(Animals):
    def do_smth(self):
        return 'стрижется'


class Sheep(SheerAnimals):
    representative = 'Овца'

    def make_sounds(self):
        return 'Бе-е-е!'


farm = [
    Chicken('Ко-ко', 3),
    Chicken('Кукареку', 5),
    Goose('Серый', 7),
    Goose('Белый', 7),
    Duck('Кряква', 4),
    Sheep('Барашек', 75),
    Sheep('Кудрявый', 90),
    Cow('Манька', 350),
    Goat('Роза', 40),
    Goat('Копытце', 45)
]

max_weight = 0
sum_weight = 0
for animal in farm:
    print(
        f'{animal.representative}, {animal.name} говорит "{animal.make_sounds()}", '
        f'весит {animal.weight} кг, {animal.do_smth()}, {animal.feed()}.')

    sum_weight += animal.weight
    if animal.weight > max_weight:
        max_weight = animal.weight
        represent = animal.representative
        heavy_anim_name = animal.name

print(f'Вес всех животных - {sum_weight} кг')
print(f'Самое тяжелое животное это - {represent} {heavy_anim_name}, вес - {max_weight} кг.')
