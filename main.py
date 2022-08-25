def method_hw02Task01_v_00():
    print("Введите число")
    num = float(input())
    summ = 0
    while num > 0:
        rez = num % 10
        summ = summ + rez
        num = num // 10
    print(summ)
    # не работает дробное число просто выводит его в консоль.
#method_hw02Task01_v_00()
def method_hw02Task01_v_01():
    numBeforeClear = input("Введите число: ")
    numClearStepOne = numBeforeClear.replace('.', '')
    numAfterClear = numClearStepOne.replace(',', '')
    # print(numAfterClear)
    summ = 0
    for step in numAfterClear:
        summ += int(step)
    print(summ)
def method_hw02Task02_v_00():
   # print("введите число N")
    num = int(input("введите число N: "))
    # print(num)
    st = 1
    for step in range(num):
        st *= step + 1
        print(st)


method_hw02Task01_v_01()

method_hw02Task02_v_00()