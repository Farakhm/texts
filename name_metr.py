import re
from service import differen

def name_metrix(g1):
    g = re.sub(r"\b[А-ЯЁ]+\b", '', g1)
    g = g.replace('\'','')

    # Удаляем все предлоги и местоимения

    prepos = ['За','От',"Против","На", "Где","Почему","Здесь",'Но','Если','Не',
            "Да","По","Все",'Когда','Так', 'Вот','Или','Из','Ну','Вдруг',
            'Там', 'Ни',"До","Через","Хотя","Ага","То","Еще","Лишь","Один",
            "Для","Во","При",'Тут','Едва','Раз','Ай',"Без","Ба","Ко"]
    pronoun = ["Я","Ты","Он", "Она","Они", "Тебе", "Твой","Мы","Вы",
            'Это','Что','Как','Нет','Мне','Его','Теперь',"Ему","Ему",
            "Того","Ее","Вам","Ту", 'Авось']

    n1 = len(prepos)
    for i in range(n1):
        g = g.replace(prepos[i],'')

    n1 = len(pronoun)
    for i in range(n1):
        g = g.replace(pronoun[i],'')

    names = re.findall(r"\b[А-ЯЁ][а-яё]*\b", g)

    names_single = set(names)
    names_single = list(names_single)

    n = len(names_single)
    names_count = []
    for i in range(n):
        k = names.count(names_single[i])
        names_count.append([k, names_single[i]])

    names_count.sort(reverse=True)

    f = open('word_g_list.txt', 'w')
    for i in range(n):
        f.write(str(names_count[i][0]) + ' : ' + names_count[i][1] + '\n')
    f.close()

    names_single.sort()
    names_sort = list(names_single)
    names_form = []

    f = open('sort_names.txt', 'w')
    for i in range(len(names_sort)):
        f.write(names_sort[i]+'\n')
    f.close()

    unic_nam = []

#    while 5 > 3:
#        m = len(names_sort)
#        unic_n = []
#        num_ind = []
#        num_ind.append(0)

#        for i in range(m - 1):
#            if fdiff(names_sort[0],names_sort[i + 1]):
#                num_ind.append(i + 1)
#        m1 = len(num_ind)
#        for i in range(m1):
#            unic_n.append(names_sort[num_ind[i]])
#        j = 0
#        for i in range(m1):
#            names_sort.pop(num_ind[i] - j)
#            j = j + 1
#        unic_nam.append(unic_n)

#        if len(names_sort) == 0:
#            break
    
    while 5 > 3:
        m = len(names_sort)
        unic_n = []
        num_ind = []
        num_ind.append(0)
        for i in range(m - 1):
            if differen(names_sort[0],names_sort[i + 1]):
                num_ind.append(i + 1)
#        if fdiff(nam[0],nam[i + 1]):
#            num_ind.append(i + 1)
#        elif fsquar(nam[0],nam[i + 1]):
#            num_ind.append(i + 1)
        m1 = len(num_ind)
        for i in range(m1):
            unic_n.append(names_sort[num_ind[i]])
        j = 0
        for i in range(m1):
            names_sort.pop(num_ind[i] - j)
            j = j + 1
        unic_nam.append(unic_n)

        if len(names_sort) == 0:
            break

    f = open('text_names_forms.txt', 'w')
    m = len(unic_nam)
    for i in range(m):
        m1 = len(unic_nam[i])
        for j in range(m1):
            f.write(unic_nam[i][j] + '  ')
        f.write('\n')
    f.close()

    f = open('name_singles.txt', 'w')
    m = len(names_single)
    for i in range(m):
        f.write(names_single[i] + '\n')
    f.close()