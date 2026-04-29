import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fontTools.designspaceLib.types import locationInRegion

df = pd.read_csv('data.csv')
#1крупные динозавры обычно травоядные(угадал)
df['length'] = df['length'].str.replace('m', '').astype(float)
bigdino = df[df['length'] >= 15]
diet = bigdino['diet'].value_counts()
plt.figure()
diet.plot(kind='pie')
plt.title('отношение крупных травоядных динозавров и крупных хищных')
plt.show()
#2в основном динозавры в позднем меловом периоде были больше 15 метров(не угадал)
df['period_start'] = df['period'].str.extract(r'(\d{3})-').astype(float)
plt.figure()
plt.scatter(df['period_start'], df['length'])
plt.title('рост динозавров в поздний меловой период')
plt.show()
#3в северной америке динозавры были в основном травоядные(угадал)
usadino = df[df['lived_in'] == "USA"]
carndino = usadino[usadino['diet'] == 'carnivorous']
herbdino = usadino[usadino['diet'] == 'herbivorous']
cc = len(carndino)
hc = len(herbdino)
labels = ['carnivorous', 'herbivorous']
sizes = [cc, hc]
plt.figure()
plt.pie(sizes, labels=labels)
plt.title('отношение травоядных и плотоядных динозавров в америке')
plt.show()
#4динозары с окончанием saurus примерно жили в одно и то же время(угадал)
df['hz'] = df['period'].str.extract(r'(\d{3})-').astype(float)
aoaoao = df[df['name'].str.endswith('saurus')]
oaoaoa = df[~df['name'].str.endswith('saurus')]
plt.figure()
plt.hist([aoaoao['hz'], oaoaoa['hz']], label=['динозавры с saurus', 'динозавры с не saurus'])
plt.xlabel('время')
plt.ylabel('количество динозавров')
plt.legend()
plt.grid(True)
plt.title('период проживания динозавров с окончанием "saurus"')
plt.show()
#5меньше всего динозавров жило в казахстане
location = df['lived_in'].value_counts()
plt.figure(figsize=(100,50))
labels = location.index
sizes = location.values
plt.pie(sizes, labels=labels)
plt.grid(True)
plt.title('отношение количества динозавров во всех странах')
plt.show()
