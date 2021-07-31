import numpy as np
import re
from service import word_count_f
from service import init_signs

def word_metrix(g):
    rus_lett,rus_lett_z,eng_lett,eng_lett_z,digits,signs = init_signs()
    num_signs = len(signs)
    g1 = g.lower()
    g1 = g1.replace("\n", "")
    for i in range(num_signs):
        g1 = g.replace(signs[i],"")
    # Задаем максимальную длину слова
    word_len = 25

    words_num = np.zeros((word_len))
    words_unicum_num = np.zeros((word_len))

    for i in range(word_len):
        words_num[i], words_unicum_num[i] = word_count_f(g1,i+1)

    sum_words = np.sum(words_num)
    sum_unicum_words = np.sum(words_unicum_num)
    print('Всего - ', sum_words, ' слов', ' из них уникальных - ', sum_unicum_words)

    # Подсчет частот слов с различным количеством букв

    lett_per_word_freq = np.zeros((word_len))
    for i in range(word_len):
        lett_per_word_freq[i] = words_num[i]/sum_words

    print(np.sum(lett_per_word_freq))

    # Подсчет количества предложений и числа слов в них
    # Сейчас у нас есть текст в виде совокупности строк

    g1 = g.replace("\n", " ")
    g1 = g1.replace("...", ".")
    g1 = g1.replace("!", ".")
    g1 = g1.replace("?", ".")
    g1 = re.sub('\s+', ' ', g1)

    # Теперь он в виде одной строки

    sent01 = g1.split(". ")

    num_sent = len(sent01)
    word_sent = np.zeros((num_sent),int)
    wrd_max = 0

    f = open('sentences.txt', 'w')

    for i in range(num_sent):
        f.write(sent01[i]+".\n")
        sent01[i] = re.sub('[-]','',sent01[i])
        word_sent[i] = len(sent01[i].split())
        if word_sent[i] > wrd_max:
            wrd_max = word_sent[i]

    f.close()

    word_sent = list(word_sent)

    word_per_sent_freq = np.zeros((wrd_max))

    for i in range(wrd_max):
        word_per_sent_freq[i] = word_sent.count(i+1)/num_sent

    # Считаем количество абзацев и число предложений в них

    g1 = g.replace("...", ".")
    g1 = g1.replace("!", ".")
    g1 = g1.replace("?", ".")

    paragr = re.split('\.\n\s+',g1)

    num_paragr = len(paragr)
    print(num_paragr)

    sent_per_para = np.zeros((num_paragr),int)

    f = open('paragr.txt', 'w')

    for i in range(num_paragr):
        paragr[i] = paragr[i].replace('\n', ' ') + '.'
        f.write(paragr[i]+'\n')
        sent_per_para[i] = list(paragr[i]).count('.')
    f.close()

    max_sent_per_para = np.max(sent_per_para)
    print(max_sent_per_para)

    sent_per_par_freq = np.zeros((max_sent_per_para))

    for i in range(max_sent_per_para):
        sent_per_par_freq[i] = list(sent_per_para).count(i+1)/num_paragr

    f = open('text_metrics.txt', 'w')
    # Записываем в файл частоты слов разной длины
    f.write(str(len(lett_per_word_freq))+'\n')
    for i in range(len(lett_per_word_freq)):
        f.write(str(lett_per_word_freq[i])+'\n')

    # Записываем в файл частоты предложений различной длины
    f.write(str(len(word_per_sent_freq))+'\n')
    for i in range(len(word_per_sent_freq)):
        f.write(str(word_per_sent_freq[i])+'\n')

    # Записываем в файл частоты параграфов с различным числом предложений
    f.write(str(len(sent_per_par_freq))+'\n')
    for i in range(len(sent_per_par_freq)):
        f.write(str(sent_per_par_freq[i])+'\n')

    f.close()