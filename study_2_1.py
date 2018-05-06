import re
import numpy as np
from scipy import spatial

#Считываем файл 'sentences.txt',приводим каждую строку к нижнему регистру.

file_obj = open('sentences.txt')
data_list = file_obj.readlines()
a = []

#Производим токенизацию и удаляем пусты слова

for line in data_list:
    a.append(re.split('[^a-z]',line.strip().lower()))
for x in a:
    while ('') in x:
        x.remove('')

#Состаляем список всех слов, встречающихся в предложениях. 
#Сопоставляем каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях. 

d = {}
s = 1
for x in a:
    for lett in x:
        if lett not in d.values():
            d.update({s:lett})
            s=s+1

#Создаем матрицу размера n * d, где n — число предложений. 
#Заполняем ее: элемент с индексом (i, j) в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. 

m = np.zeros((22, 254),dtype=int)
for i in range(22):
    for j in range(254):
        m[i][j]=a[i].count(d[j+1])
#Находим косинусное расстояние от предложения в самой первой строке. И затем 
for i in range(21):
    c = spatial.distance.cosine(m[0],m[i+1])
    print(i+1,' ', c)   
    
# два предложений, ближайших к нему по этому расстоянию: 6,4
