from service import text_metrix

# Открываем текст
f = open('first.txt', 'r')
g = f.read()
f.close()

# Снимаем различные метрики текста

text_metrix(g)

print('That s all!')



