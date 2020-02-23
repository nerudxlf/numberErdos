AVTOR = "Erdos, P"  # Константа
stringNameArticle = []
stringNameAvtor = []
stringNameAvtorOne = set()
stringNameAvtorTwo = set()
nameAvtorResult = []


def addArr(List):
    """Фунция обработки строки"""
    List = List.split("., ")
    lastElem = List[-1].split(".: ")
    del List[-1]
    List.append(lastElem[0])
    return List


def one(List):
    """Функция для получения числа один то есть
    людей которые непосредсвенно первыми печатались в статье"""
    List = addArr(List)
    cout = 0
    if AVTOR in List:
        List.remove(AVTOR)
        cout = 1
        return List, cout
    return List, 0


def two(ListSet, ListSetForOne):
    """функция для нахождения людей которые писали статью
    с людьми номер которых равен одному"""
    cout = 0
    for i in range(0, len(ListSet)):
        if ListSet[i] in ListSetForOne:
            ListSetForOne.remove(ListSet[i])
            cout = 1
    if cout:
        return ListSetForOne, cout
    return 0, 0


def result(name, number):
    """Конкатенация строк"""
    if number == 0:
        number = "Infinity"
    string = str(name) + " " + str(number)
    return string


def main():
    valueS = int(input())
    stringPN = str(input())
    stringPN = stringPN.split()
    arrStringPN = [int(elem) for elem in stringPN]
    for i in range(0, arrStringPN[0]):
        line = str(input())
        cout = 0
        line, cout = one(line)
        if cout:
            stringNameAvtorOne.update(set(line))
            cout = 0
        else:
            line, cout = two(list(stringNameAvtorOne), line)
            if cout:
                stringNameAvtorTwo.update(set(line))
    for i in range(0, arrStringPN[1]):
        line = str(input())
        stringNameAvtor.append(line)
        if stringNameAvtor[i] in stringNameAvtorOne:
            nameAvtorResult.append(result(stringNameAvtor[i], 1))
        elif stringNameAvtor[i] in stringNameAvtorTwo:
            nameAvtorResult.append(result(stringNameAvtor[i], 2))
        else:
            nameAvtorResult.append(result(stringNameAvtor[i], 0))

    for i in range(0, len(nameAvtorResult)):
        print(nameAvtorResult[i])


if __name__ == '__main__':
    main()
