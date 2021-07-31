import numpy as np
import re
from random import random
from random import seed
from random import randint

def word_count(text, num_of_lett):
    reg_var = r'\b\w{%d}\b' % num_of_lett
    wrd = re.findall(reg_var, text)
    m = len(wrd)
#    print('Всего ',m,' слов из ', num_of_lett, ' букв')
    wrdsl = set(wrd)
    wrd = list(wrdsl)
    m = len(wrd)
    wrd.sort()
#    print('Из них ',m, ' уникальных')
    return wrd,m

def word_count_f(text, num_of_lett):
    reg_var = r'\b\w{%d}\b' % num_of_lett
    wrd = re.findall(reg_var, text)
    m = len(wrd)
    wrdsl = set(wrd)
    wrd = list(wrdsl)
    n = len(wrd)
    wrd.sort()
    return m,n

def word_count_p(text, num_of_lett):
    reg_var = r'\b\w{%d}\b' % num_of_lett
    wrd = re.findall(reg_var, text)
    return wrd

def index_lett(lett1):
    a = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
    res = a.find(lett1)
    return res

def boostr(nums, freqs):
    seed()
    r = random()
    l = 0
    res = randint(0,32)
    for i in range(nums):
        l = l + freqs[i]
        if l >= r :
            res = i
            break
    return res

def init_signs():
    f = open('format.mod','r')
    r = f.read()
    f.close()
    r1 = r.split('\n')
    return r1[0],r1[1],r1[2],r1[3],r1[4],r1[5]


def fdiff(tx1,tx2):
    res = True
    m = min(len(tx1), len(tx2))
    if (abs(len(tx1) - len(tx2)) > 4):
        res = False
    else:
        for i in range(m):
            if tx1[i] != tx2[i]:
                res = False
                break
    return res

def fsquar(tx1,tx2):
    res = True
    m1 = len(tx1)
    m2 = len(tx2)
    if m1 <= m2:
        rx1 = tx1
        rx2 = tx2
    else:
        rx1 = tx2
        rx2 = tx1
#  rx1 всегда самая короткая
#  не рассчитываем для коротких слов
    if (max(m1,m2) < 5):
        res = False
    else:
        rx1 = tx1[:-2]
        res = fdiff(rx1,rx2)
    return res

def differen(tx1,tx2):
    res = False
    m = min(len(tx1), len(tx2))
    i = 0
    n = 1
    while tx1[i] == tx2[i]:
        i = i + 1
        if i == m:
            break
    n = i
    if m - n < 3 and n > 2:
        res = True
    return res

