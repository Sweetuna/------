#실습 1
import matplotlib.pyplot as plt
year=[2014,2015,2016,2017,2018,2019,2020,2021,2022]
gdp=[3079.9, 3250.1, 3398.8, 3574, 3678.2, 3721.8, 3744, 4003.6, 4165.5]
plt.plot(year,gdp)
plt.show()

#실습 2
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
year=[2014,2015,2016,2017,2018,2019,2020,2021,2022]
gdp=[3079.9,3250.1,3398.8,3574,3678.2,3721.8,3744,4003.6,4165.5]
plt.figure(figsize=(5,3))
#plt.plot(year,gdp, 'g.-')
plt.plot(year,gdp, color='#008080',marker='h',linestyle='--')
plt.title('GDP per capita')
plt.xlabel('years')
plt.ylabel('ten thoudsand won')
plt.ylim(2500,4500)
plt.show()

#실습 3
year=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
seoul=[12.1,12,12.2,12.5,13.4,13.6,13.6,13,12.9,13.5,13.2,13.7,13.2]
jeju=[15.6,15.6,15.7,16.5,16.2,16.7,17,16.8,16.6,16.8,16.7,17.5,17]

import matplotlib.pyplot as plt
plt.plot(year,seoul)
plt.plot(year,jeju)
plt.show()

#실습 4
year = [2000, 2005, 2010, 2015, 2020]
single_person = [15.5, 20.0, 23.9, 27.2, 31.7]
baby_born = [640089, 438707, 470171, 438420, 272337]

plt.figure(figsize=(5,3))
plt.scatter(single_person, baby_born)
plt.xlabel('single-person household ratio')
plt.ylabel('the number of babies born')
plt.show()

#실습 5
height = [156.9,159.9,153.5,151.2,154.6,168.3,165,154.7,146,152.4]
weight = [48.7,58.5,48.4,39,58.9,80.8,59.3,49.4,35.3,51.8]
gender = ['f','f','f','f','f','m','m','m','m','m']

plt.figure(figsize=(5,3))
plt.scatter(height, weight)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()

#실습 6
name = ['Jessica', 'Liam', 'Sophia']
x = [75, 92, 83]
y = [79, 89, 90]

plt.figure(figsize=(5,3))
plt.scatter(x, y)
plt.annotate(name[0],(x[0],y[0]),xytext=(5,-10),textcoords='offset points')
plt.annotate(name[1],(x[1],y[1]),xytext=(5,-10),textcoords='offset points')
plt.annotate(name[2],(x[2],y[2]),xytext=(5,-10),textcoords='offset points')
plt.xlim(73, 95)
plt.ylim(75, 93)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#실습 7
temperature = [6,2.2,4.6,7.7,8,9.2,11.7,12.5,10.3,13.5,
               15.2,5.9,2.9,9.2,8.6,4.6,7.2,7.7,8.3,9.5,
               13,17,17.4,12.5,12.5,9.4,7.3,9.2,11.8,13.3,15]

plt.figure(figsize=(5,3))
plt.hist(temperature, bins=15, alpha=0.5)
plt.xlabel('temperature')
plt.ylabel('frequency')
plt.show()

#실습 8
blood = {'A':0,'B':0,'O':0,'AB':0}

while True:
  s = input('혈액형(A, B, O, AB) 또는 종료: ')
  if s=='종료':
    break
  elif s in blood:
    blood[s] += 1
  else:
    print('잘못 입력했습니다.')

plt.figure(figsize=(5,3))
plt.bar(blood.keys(), blood.values(), width=0.6)
plt.xlabel('blood type')
plt.ylabel('frequency')
plt.show()

#실습 9
import random

x = [random.normalvariate(0,1) for _ in range(1000)]

plt.figure(figsize=(5,3))
plt.hist(x, bins=20, alpha=0.5)
plt.ylabel('frequency')
plt.show()

#실습 10
cat = plt.imread('C:/Users/danie/Desktop/cat.1.jpg')
plt.imshow(cat)
plt.show()

#실습 11
plt.figure(figsize=(3,3))
plt.imshow(cat)
plt.axis('off')
plt.savefig('result.png')
plt.show()

#실습 12
cat = plt.imread('C:/Users/danie/Desktop/cat.1.jpg')
dog = plt.imread('C:/Users/danie/Desktop/dog.1.jpg')

plt.figure(figsize=(5,3))

plt.subplot(1, 2, 1)
plt.imshow(cat)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dog)
plt.axis('off')

plt.show()

#실습 13
cat = plt.imread('C:/Users/danie/Desktop/cat.1.jpg')
dog = plt.imread('C:/Users/danie/Desktop/dog.1.jpg')
imgs = [cat, dog]

plt.figure(figsize=(5,3))
for i in range(len(imgs)):
  plt.subplot(1, 2, i+1)
  plt.imshow(imgs[i])
  plt.axis('off')
plt.show()

#실습 14
cat = plt.imread('C:/Users/danie/Desktop/cat.1.jpg')
dog = plt.imread('C:/Users/danie/Desktop/dog.1.jpg')
imgs = [cat, dog]
labels = ['cat', 'dog']

plt.figure(figsize=(5,3))
for i in range(len(imgs)):
  plt.subplot(1, 2, i+1)
  plt.imshow(imgs[i])
  plt.xticks([])
  plt.yticks([])
  plt.xlabel(labels[i])
plt.show()

#실습 15
import os

imgs = os.listdir('C:\Users\danie\Desktop\dog')

plt.figure(figsize=(5,5))
for i in range(len(imgs)):
  plt.subplot(2,2,i+1)
  img = plt.imread(os.path.join('C:/Users/danie/Desktop/dog', imgs[i]))
  plt.imshow(img)
  plt.axis('off')
plt.show()

#실습 16
import random

dice1 = plt.imread('dice1.png')
dice2 = plt.imread('dice2.png')
dice3 = plt.imread('dice3.png')
dice4 = plt.imread('dice4.png')
dice5 = plt.imread('dice5.png')
dice6 = plt.imread('dice6.png')
dices = [dice1,dice2,dice3,dice4,dice5,dice6]

plt.figure(figsize=(4.5,2))
for i in range(2):
  plt.subplot(1, 2, i+1)
  select = random.randint(0,len(dices)-1)
  plt.imshow(dices[select])
  plt.axis('off')
  plt.show()