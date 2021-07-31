import numpy as np
from random import random
from random import randint
from service import boostr
from service import init_signs

def sintes():
    # загрузка ранее сохраненных метрик
    rus_lett,rus_lett_z,eng_lett,eng_lett_z,digits,signs = init_signs()
    alphalist = list(rus_lett)

    f = open('text_metrics.txt', 'r')

    # Считываем частоты слов разной длины
    num_lett_per_word = int(f.readline())
    lett_per_word_freq = np.zeros((num_lett_per_word))

    for i in range(num_lett_per_word):
        lett_per_word_freq[i] = float(f.readline())

    # Считываем частоты предложений различной длины
    num_word_per_sent = int(f.readline())
    word_per_sent_freq = np.zeros((num_word_per_sent))

    for i in range(num_word_per_sent):
        word_per_sent_freq[i] = float(f.readline())

    # Считываем частоты параграфов с различным числом предложений
    num_sent_per_par = int(f.readline())
    sent_per_par_freq = np.zeros((num_sent_per_par))

    for i in range(num_sent_per_par):
        sent_per_par_freq[i] = float(f.readline())

    f.close()

    f = open('lett_metrics.txt', 'r')

    first_lett_freq = np.zeros((33))

    for i in range(33):
        first_lett_freq[i] = float(f.readline())

    sec_lett_freq = np.zeros((33,33))

    for i in range(33):
        for j in range(33):
            sec_lett_freq[i][j] = float(f.readline())

    third_lett_freq = np.zeros((33,33,33))

    for i in range(33):
        for j in range(33):
            for k in range(33):
                third_lett_freq[i][j][k] = float(f.readline())

    fourth_lett_freq = np.zeros((33,33,33,33))

    for i in range(33):
        for j in range(33):
            for k in range(33):
                for l in range(33):
                    fourth_lett_freq[i][j][k][l] = float(f.readline())

    f.close()
    print('All freqiencies are loaded!')

    # Все частоты загружены - начинаетcя веселье!
    # Последовательность следующая
    # Сначала разыгрываем количество абзацев

    curr_num_par = randint(2,10)

    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""

    for npar in range(curr_num_par):
        curr_num_sent = boostr(num_sent_per_par,sent_per_par_freq)
        for nsent in range(curr_num_sent):
            curr_num_words = boostr(num_word_per_sent,word_per_sent_freq)
            for numw in range(curr_num_words):  # Генерируем слова
                curr_num_lett = boostr(num_lett_per_word,lett_per_word_freq)
                l1 = boostr(33,first_lett_freq)
                s1 = s1 + alphalist[l1]
                if curr_num_lett > 1 :
                    l2 = boostr(33,sec_lett_freq[l1])
                    s1 = s1 + alphalist[l2]
                    if curr_num_lett > 2 :
                        l3 = boostr(33,third_lett_freq[l1][l2])
                        s1 = s1 + alphalist[l3]
                        if curr_num_lett > 3 :
                            for j in range(curr_num_lett - 3):
                                l4 = boostr(33,fourth_lett_freq[l1][l2][l3])
                                l1 = l2
                                l2 = l3
                                l3 = l4
                                s1 = s1 + alphalist[l4]
                s2 = s2 + s1 + " "
                s1 = ""
            s3 = s3 + s2.capitalize().strip() + '. '
            s2 = ""
        s4 = s4 + s3 + '\n'
        s3 = ""

    f = open('sintext.txt', 'w')
    f.write(s4)
    f.close()
