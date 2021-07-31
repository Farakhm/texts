from lett_metr import lett_metrix
from word_metr import word_metrix
from sintext import sintes

# Открываем текст
f = open('first.txt', 'r')
g = f.read()
f.close()

# Снимаем различные метрики текста

#lett_metrix(g)
#word_metrix(g)

sintes()

print('That s all!')



