def new_format(string: str):
    """First solution
       плохое решение но выглядит сложно

       так же есть решение с reverse там где мы реверсем строку и расставляем точки, потом через format, 
       и через рекурсию (сводим до базового случая (в нашем случае когда длина string будет кратна 3) 
       после расставляем точки и добавляем base в начале)

       сложность этого алгоритма в худшем случае же составляет примерно O((n/3) + 3)
    """
    base = ""
    if len(string) <= 3:
        return string
    for i in string:
        if len(string) % 3 == 0:
            second_part = ".".join([string[i:i+3] for i in range(0, len(string), 3)])
            if len(base) == 0:
                return second_part
            return base + "."+ second_part
        base += i
        string = string[1:len(string)]


def new_format2(string: str):
    """
    решение с реверсом
    """
    string = string[::-1]
    return ".".join([string[i:i+3] for i in range(0, len(string), 3)])[::-1]


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")

assert (new_format2("1000000") == "1.000.000")
assert (new_format2("100") == "100")
assert (new_format2("1000") == "1.000")
assert (new_format2("100000") == "100.000")
assert (new_format2("10000") == "10.000")
assert (new_format2("0") == "0")
print("SUCCESS")
