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
