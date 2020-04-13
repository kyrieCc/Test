'''
#从0到1亿之间随机取6千万个数放在lista中
#再从0到1亿之间随机取6千万个数放在listb中
#求lista和listb中重复的元素，放在listc中并打印，有几种解法，各自的时间复杂度和空间复杂度如何。
#python的set()和dict()的实现使用了什么算法，尝试使用set()和dict()求解上边的问题
'''
#从1亿里面取6千万个数
import random
lista = random.sample(range(0,100000000),60000000)
listb = random.sample(range(0,100000000),60000000)
#暴力O(n^2)
def Baoli(lista,listb):
    listc = []
    for i in lista:
        if i in listb:
            listc.append(i)
    return listc
#merge O(nlogn)
def merge(lista,listb):
    listc = []
    p1 = 0
    p2 = 0
    lista = sorted(lista)
    listb = sorted(listb)
    while p1<60000000 and p2 < 60000000:
        if lista[p1] < listb[p2]:
            p1+=1
        elif lista[p1] > listb[p2]:
            p2+=1
        else:
            listc.append(lista[p1])
            p1 += 1
            p2 += 1
    return listc
#Yu O(n)
def Set1(lista,listb):
    return (set(lista) & set(listb))
def dict1(lista,listb):
    a = dict(zip(lista, [1 for i in range(len(lista))]))
    b = dict(zip(listb, [1 for i in range(len(listb))]))
    listc = []
    for i in a:
        if i in b:
            listc.append(i)
    return listc
if __name__ == '__main__':
    a = Baoli(lista,listb)
    b = merge(lista, listb)
    c = Set1(lista,listb)
    d = dict1(lista,listb)


