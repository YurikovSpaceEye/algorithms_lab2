names = ["Святослав Юриков",
         "Саша Копытко",
         "Мария Улиткина",
         "Кирилл Волкович",
         "Анна Ивановна",
         "Настя Райнус",
         "Сергей Погорелов",
         "Андрей Горлов",
         "Катя Баклановна",
         "Артем Сергеев",
         "Артур Калинин",
         "Костя Долгов",
         "Настя Королева",
         "Сеня Максимов",
         "Яна Зорина",
         "Максим Теребов",
         "Михаил Панин",
         "Анлрей Гневашев",
         "Виталя Суслопаров",
         "Арсений Еремеев",
         "Зуад Фаед",
         "Елена Драчева",
         "Максим Ложкин",
         "Саина Николаева",
         "Иван Белоконь",
         "Наташа Таргович",
         "Дан Крылов",
         "Катя Гусаева",
         "Ката Ульянова",
         ]

print(len(names))

attributes = ["Высок(ий/ая)", "Любит гулять", "Общительн(ый/ая)", "Играет в Dota", "Играет в Minecraft", "Играет в карты"]

ruleset = {}

def convert_to(num, required_length):
    temp_str = bin(num)[2:]
    return ((required_length - len(temp_str)) * "0") + temp_str

for i in range(len(names)):
    ruleset[convert_to(i, len(attributes))] = names[i]

def fancy_output(ruleset):
    for rule, name in zip(ruleset.keys(), ruleset.values()):
        print(name, rule)

print(ruleset)
fancy_output(ruleset)