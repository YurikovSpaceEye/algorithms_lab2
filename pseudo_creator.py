from copy import deepcopy

# www.plantuml.com/plantuml
# https://plantuml.com/ru/activity-diagram-beta

ruleset = {'000000': 'Святослав Юриков', '000001': 'Саша Копытко', '000010': 'Мария Улиткина', '000011': 'Кирилл Волкович', '000100': 'Анна Ивановна', '000101': 'Настя Райнус', '000110': 'Сергей Погорелов', '000111': 'Андрей Горлов', '001000': 'Катя Баклановна', '001001': 'Артем Сергеев', '001010': 'Артур Калинин', '001011': 'Костя Долгов', '001100': 'Настя Королева', '001101': 'Сеня Максимов', '001110': 'Яна Зорина', '001111': 'Максим Теребов', '010000': 'Михаил Панин', '010001': 'Анлрей Гневашев', '010010': 'Виталя Суслопаров', '010011': 'Арсений Еремеев', '010100': 'Зуад Фаед', '010101': 'Елена Драчева', '010110': 'Максим Ложкин', '010111': 'Саина Николаева', '011000': 'Иван Белоконь', '011001': 'Наташа Таргович', '011010': 'Дан Крылов', '011011': 'Катя Гусаева', '011100': 'Катя Ульянова'}
attributes = ["Высок(ий/ая)", "Любит гулять", "Общительн(ый/ая)", "Играет в Dota", "Играет в Minecraft", "Играет в карты"]

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
        val2[k_][0] += 1
        val2 = val2[k_][1]

    val.append(value)

code_str = ""

def recursive(attribute_val, val2):
    global code_str
    global stages2

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