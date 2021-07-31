from name_metr import name_metrix
from lett_metr import lett_metrix
from word_metr import word_metrix
from sintext import sintes
from name_metr import name_metrix

# Открываем текст
f = open('first.txt', 'r')
g = f.read()
f.close()

# Снимаем различные метрики текста

#lett_metrix(g)
#word_metrix(g)

#sintes()

name_metrix(g)

print('That s all!')



