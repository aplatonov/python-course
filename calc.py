import sys

print(
    """Калькулятор выражений на основе Обратной польской записи
    @see https://habr.com/ru/post/282379/ 
Принимает выражения вида: (24 - 13) * 15 / (554 + 11)
Введите пустое выражение для завершения работы.
"""
)

def priority(oper):
    if oper == "+" or oper == "-":
        return 1
    elif oper == "*" or oper == "/":
        return 2
    elif oper == "(":
        return 0

run = True
opers = ["+", "-", "*", "/", "(", ")"] # допустимые операции
while run:
    formula = input("Введите выражение для вычисления: ")
    if not formula.strip():
        run = False
        print('Завершение работы...')
        sys.exit()

    # разобъем полученную строку на лексемы (операнды и операции)
    lexems = []
    tmp = ""
    for char in formula.replace(' ', ''):
        if char in opers:
            if tmp != "":
                lexems.append(tmp)
            lexems.append(char)
            tmp = ""
        else:
            tmp += char
    if tmp != "":
        lexems.append(tmp)

    # переведем лексемы в обратную польскую запись
    opstack = [] # стек операций
    rpn = [] # массив выхода
    for lexem in lexems:
        if lexem == "(":
            opstack = [lexem] + opstack
        elif lexem in opers:
            if opstack == []:
                opstack = [lexem]
            elif lexem == ")":
                while (True):
                    q = opstack[0]
                    opstack = opstack[1:]
                    if q == "(":
                        break
                    rpn.append(q)
            elif priority(opstack[0]) < priority(lexem):
                opstack = [lexem] + opstack
            else:
                while (True):
                    if opstack == []:
                        break
                    q = opstack[0]
                    rpn.append(q)
                    opstack = opstack[1:]
                    if priority(q) == priority(lexem):
                        break
                opstack = [lexem] + opstack
        else:
            rpn.append(lexem)
    while (opstack != []):
        q = opstack[0]
        rpn.append(q)
        opstack = opstack[1:]

    print("Обратная польская запись: ", end = ' ')
    print(" ".join(rpn))

    # вычисление результата по обратной польской записи
    res = []
    for item in rpn:
        if item in opers:
            b = res.pop()
            a = res.pop()
            if item == "+":
                res.append(float(a) + float(b))
            if item == "-":
                res.append(float(a) - float(b))
            if item == "*":
                res.append(float(a) * float(b))
            if item == "/":
                res.append(float(a) / float(b))
        else:
            res.append(float(item))

    print("Результат: " + str(res.pop()))
    print("-----------")