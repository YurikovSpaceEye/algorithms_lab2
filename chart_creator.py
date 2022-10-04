from copy import deepcopy

# www.plantuml.com/plantuml
# https://plantuml.com/ru/activity-diagram-beta

ruleset = {'00000': 'Святослав Юриков', '00001': 'Саша Копытко', '00010': 'Мария Улиткина', '00011': 'Кирилл Волкович', '00100': 'Анна Ивановна', '00101': 'Настя Райнус', '00110': 'Сергей Погорелов', '00111': 'Андрей Горлов', '01000': 'Катя Баклановна', '01001': 'Артем Сергеев', '01010': 'Артур Калинин', '01011': 'Костя Долгов', '01100': 'Настя Королева', '01101': 'Сеня Максимов', '01110': 'Яна Зорина', '01111': 'Максим Теребов', '10000': 'Михаил Панин', '10001': 'Анлрей Гневашев', '10010': 'Виталя Суслопаров', '10011': 'Арсений Еремеев', '10100': 'Зуад Фаед', '10101': 'Елена Драчева', '10110': 'Максим Ложкин', '10111': 'Саина Николаева', '11000': 'Иван Белоконь', '11001': 'Наташа Таргович', '11010': 'Дан Крылов', '11011': 'Катя Гусаева', '11100': 'Ката Ульянова'}
attributes = ["Любит гулять", "Общительн(ый/ая)", "Играет в Dota", "Играет в Minecraft", "Играет в карты"]

stages = []
stages2 = []

for i in range(len(attributes)):
    stages = [deepcopy(stages), deepcopy(stages)]
    stages2 = [[0, deepcopy(stages2)], [0, deepcopy(stages2)]]

def to_arr(str):
    temp = []
    for char in str:
        temp.append(0 if char == "0" else 1)
    return temp

for key, value in zip(ruleset.keys(), ruleset.values()):
    k = to_arr(key)
    val = stages
    val2 = stages2
    for k_ in k:
        val = val[k_]

        #mark if path is used by any student
        val2[k_][0] += 1
        val2 = val2[k_][1]

    val.append(value)

code_str = ""

def recursive(attribute_val, val2):
    global code_str
    global stages2

    #check if path is used by any student
    sval = stages2
    for k_ in to_arr(val2):
        if (sval[k_][0] <= 0):
            return
        sval = sval[k_][1]

    # End condition
    if (attribute_val >= len(attributes)):
        name = "Нет студента"
        if val2 in ruleset.keys():
            name = ruleset[val2]

        code_str += " " * 2 * attribute_val + ":" + name + ";\n"
        return

    attribute = attributes[attribute_val]
    code_str += " " * 2 * attribute_val + f"if(Студент {attribute}?) then (да)" + "\n"
    attribute_val+=1
    recursive(attribute_val, val2+"1")
    code_str += " " * 2 * attribute_val + " else (нет)\n"
    recursive(attribute_val, val2+"0")
    code_str += " " * 2 * attribute_val + "endif\n"

code_str += "@startuml\nstart\n"
recursive(0, "")
code_str += "stop\n@enduml"

print(code_str)