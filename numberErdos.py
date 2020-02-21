AVTOR = "Erdos, P"  # Константа


def chekAvtor(string):
    """Функция проверки"""
    if string != AVTOR:
        return string


def addArr(List):
    """Фунция обработки строки"""
    List = List.split("., " or ".: ")
    lastElem = List[-1].split(".: ")
    del List[-1]
    return List.append(lastElem[0])


def one(List):
    """Функция для получения числа один то есть
    людей которые непосредсвенно первыми печатались в статье"""
    List = addArr(List)
    arrName = []
    flag = 0
    for i in List:
        if i == AVTOR:
            flag = 1
    if flag:
        for i in range(0, len(List)):
            arrName[i] = chekAvtor(List[i])
    return arrName


def two(List):
    pass


valueS = int(input())
stringPN = str(input())

stringNameArticle = []
stringNameAvtor = []
stringNameAvtorOne = []


stringPN = stringPN.split()
arrStringPN = [int(elem) for elem in stringPN]

for i in range(0, arrStringPN[0]):
    line = str(input())
    stringNameArticle.append(line)
    stringNameAvtorOne += one(stringNameArticle[i])

for i in range(0, arrStringPN[1]):
    line = str(input())
    stringNameAvtor.append(line)

# def main():
    # pass

# if __name__ == '__main__':
    # main()
