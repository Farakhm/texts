from service import word_count_f
from service import init_signs
import numpy as np

def lett_metrix(g):
    # Сначала считаем частоты букв
    letters01 = list(g)
    num_lett = len(letters01)
    # Считываем файл не-букв
    rus_lett,rus_lett_z,eng_lett,eng_lett_z,digits,signs = init_signs()
    signs = list(signs)
    num_signs = len(signs)
    # В g остается считанный исходный текст, в g1 - текст в нижнем регистре
    g1 = g.lower()
    # Убираем разделители строк - "вытягиваем" файл в одну строку
    g1 = g1.replace("\n", " ")
    # Убираем все "технические" символы
    for i in range(num_signs):
        g1 = g1.replace(signs[i],"")
    # Задаем максимальную длину слова
    word_len = 25
    # Инициализируем массивы слов и уникальных слов
    words_num = np.zeros((word_len))
    words_unicum_num = np.zeros((word_len))
    # Прокатываем текст по всем возможным длинам слов
    for i in range(word_len):
        words_num[i], words_unicum_num[i] = word_count_f(g1,i+1)
    # Разделяем текст на отдельные слова
    words = g1.split()
    sum_words = np.sum(words_num)
    sum_unicum_words = np.sum(words_unicum_num)
    print('Всего - ', sum_words, ' слов', ' из них уникальных - ', sum_unicum_words)
    print('Всего - ', len(words), ' слов')
    num_words = len(words)
    f = open('serv.txt', 'w')
    for i in range(num_words):
        f.write(words[i]+'\n')
    f.close()
    # Считаем частоту первых букв
    # Сначала количество

    first_lett_num = np.zeros((33),int)

    for i in range(num_words):
        i1 = rus_lett.find((words[i][0]))
        first_lett_num[i1] = first_lett_num[i1] + 1
    
    # Потом частоту
    first_lett_freq = np.zeros((33))
    for i in range(33):
        first_lett_freq[i] = first_lett_num[i]/num_words

    print(np.sum(first_lett_freq))

    # Считаем частоту вторых букв

    sec_lett_num = np.zeros((33,33),int)
    num_per_two = np.zeros((33),int)

    for i in range(num_words):
        i1 = len(words[i])
        if i1 > 1:
            for j in range(i1-1):
                j1 = rus_lett.find((words[i][j]))
                j2 = rus_lett.find((words[i][j+1]))
                sec_lett_num[j1][j2] = sec_lett_num[j1][j2] + 1
                num_per_two[j1] = num_per_two[j1] + 1
    
    sec_lett_freq = np.zeros((33,33))
    for i in range(33):
        for j in range(33):
            if num_per_two[i] != 0:
                sec_lett_freq[i][j] = sec_lett_num[i][j]/num_per_two[i]

    print(np.sum(np.sum(sec_lett_freq)))

    # Считаем частоту третьих букв

    third_lett_num = np.zeros((33,33,33),int)
    num_per_three = np.zeros((33,33),int)

    for i in range(num_words):
        i1 = len(words[i])
        if i1 > 2:
            for j in range(i1-2):
                j1 = rus_lett.find((words[i][j]))
                j2 = rus_lett.find((words[i][j+1]))
                j3 = rus_lett.find((words[i][j+2]))
                third_lett_num[j1][j2][j3] = third_lett_num[j1][j2][j3] + 1
                num_per_three[j1][j2] = num_per_three[j1][j2] + 1

    third_lett_freq = np.zeros((33,33,33))

    for i in range(33):
        for j in range(33):
            for k in range(33):
                if num_per_three[i][j] != 0:
                    third_lett_freq[i][j][k] = third_lett_num[i][j][k]/num_per_three[i][j]

    print(np.sum(np.sum(np.sum(third_lett_freq))))

    # Считаем частоту четвертых букв

    fourth_lett_num = np.zeros((33,33,33,33),int)
    num_per_four = np.zeros((33,33,33),int)

    for i in range(num_words):
        i1 = len(words[i])
        if i1 > 3:
            for j in range(i1-3):
                j1 = rus_lett.find((words[i][j]))
                j2 = rus_lett.find((words[i][j+1]))
                j3 = rus_lett.find((words[i][j+2]))
                j4 = rus_lett.find((words[i][j+3]))
                fourth_lett_num[j1][j2][j3][j4] = fourth_lett_num[j1][j2][j3][j4] + 1
                num_per_four[j1][j2][j3] = num_per_four[j1][j2][j3] + 1

    fourth_lett_freq = np.zeros((33,33,33,33))

    for i in range(33):
        for j in range(33):
            for k in range(33):
                for l in range(33):
                    if num_per_four[i][j][k] != 0:
                        fourth_lett_freq[i][j][k][l] = fourth_lett_num[i][j][k][l]/num_per_four[i][j][k]

    print(np.sum(np.sum(np.sum(np.sum(fourth_lett_freq)))))

    # Сбрасываем частоты на диск

    f = open('lett_metrics.txt', 'w')

    for i in range(33):
        f.write(str(first_lett_freq[i])+'\n')

    for i in range(33):
        for j in range(33):
            f.write(str(sec_lett_freq[i][j])+'\n')

    for i in range(33):
        for j in range(33):
            for k in range(33):
                f.write(str(third_lett_freq[i][j][k]) + '\n')

    for i in range(33):
        for j in range(33):
            for k in range(33):
                for l in range(33):
                    f.write(str(fourth_lett_freq[i][j][k][l]) + '\n')
    f.close()

