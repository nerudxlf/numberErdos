AVTOR = "Erdos, P"  # Константа


def addArr(List):
    """Фунция обработки строки"""
    List = List.split("., " or ".: ")
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
    return 0, 0


def two(List):
    pass


valueS = int(input())
stringPN = str(input())

stringNameArticle = []
stringNameAvtor = []
stringNameAvtorOne = set()


stringPN = stringPN.split()
arrStringPN = [int(elem) for elem in stringPN]

for i in range(0, arrStringPN[0]):
    line = str(input())
    print(one(line))
    line, cout = one(line)
    if line:
        stringNameAvtorOne.update(set(line))
    print(stringNameAvtorOne)

for i in range(0, arrStringPN[1]):
    line = str(input())
    stringNameAvtor.append(line)

# def main():
    # pass

# if __name__ == '__main__':
    # main()
