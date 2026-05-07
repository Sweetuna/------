#9-1
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

#9-2
import numpy as np

arr = np.array([1,2,3,4,5])
print(arr[1])
print(arr[1:4])

#9-3
import numpy as np

arr = np.array([[1,2,3], [4,5,6]])
print(arr)

#9-4
import numpy as np

arr = np.array([[1,2,3], [4,5,6]])
print(arr[0,1], arr[1,2])

#9-5
import numpy as np

arr = np.array([[1,2,3], [4,5,6]])
print(arr.shape)

#9-6
import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = arr1.reshape(3,2)
print(arr1)
print(arr2)

#9-7
import numpy as np

arr = np.array([2,3,4])
result = arr*2
print(result)

#9-8
import numpy as np

arr1 = np.array([2,3,4])
arr2 = np.array([5,6,7])
result = arr1+arr2
print(result)

#9-9
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 100)
y = x**2

plt.figure(figsize= (5,3))
plt.plot(x, y, label='y=x^2')
plt.legend()
plt.show()

#9-10
import matplotlib.pyplot as plt

year = [2006, 2009, 2012, 2015, 2018]
kor = [547, 546, 554, 524, 526]

plt.figure(figsize=(5,3))
plt.plot(year, kor)
plt.ylim(500,580)
plt.xlabel('year')
plt.ylabel('score')
plt.show()

#9-11
import numpy as np
import matplotlib.pyplot as plt

year = [2006, 2009, 2012, 2015, 2018]
kor = [547, 546, 554, 524, 526]

ind = np.arange(len(year))

plt.figure(figsize=(5,3))
plt.plot(ind, kor)
plt.xticks(ind, year)
plt.ylim(500,580)
plt.xlabel('year')
plt.ylabel('score')
plt.show()

#9-12
import numpy as np
import matplotlib.pyplot as plt

nation = ['Korea', 'USA', 'Japan', 'France']
men = [175.5, 176.9, 172.1, 178.6]
women = [163.2, 163.3, 158.5, 164.5]
ind = np.arange(len(nation))

plt.figure(figsize=(5,3))
plt.bar(ind, men, color='b', label='men')
plt.bar(ind, women, color='r', label='women')
plt.ylim(130,190)
plt.xticks(ind, nation)
plt.legend()
plt.show()

#9-13
import numpy as np
import matplotlib.pyplot as plt

nation = ['Korea', 'USA', 'Japan', 'France']
men = [175.5, 176.9, 172.1, 178.6]
women = [163.2, 163.3, 158.5, 164.5]
ind = np.arange(len(nation))

plt.figure(figsize=(5,3))
plt.bar(ind-0.2, men, color='b', width=0.4, label='men')
plt.bar(ind+0.2, women, color='r', width=0.4, label='women')
plt.ylim(130,190)
plt.title('Height')
plt.ylabel('cm')
plt.xticks(ind, nation)
plt.legend()
plt.show()

#9-14
import numpy as np
import matplotlib.pyplot as plt

year = [2017,2018,2019,2020,2021]
spring = np.array([124.9, 383.5, 175.0, 173.7, 330.5])
summer = np.array([612.7, 620.6, 508.2, 1037.6, 612.8])
autumn = np.array([177.9, 351.3, 440.8, 270.4, 256.4])
winter = np.array([75.2, 68.7, 168.8, 47.8, 13.3])

plt.bar(year, spring, label='spring')
plt.bar(year, summer, label='summer')
plt.bar(year, autumn, label='autumn')
plt.bar(year, winter, label='winter')
plt.legend()
plt.show()

#9-15
import numpy as np
import matplotlib.pyplot as plt

year = [2017,2018,2019,2020,2021]
spring = np.array([124.9, 383.5, 175.0, 173.7, 330.5])
summer = np.array([612.7, 620.6, 508.2, 1037.6, 612.8])
autumn = np.array([177.9, 351.3, 440.8, 270.4, 256.4])
winter = np.array([75.2, 68.7, 168.8, 47.8, 13.3])

plt.bar(year, spring, label='spring')
plt.bar(year, summer, bottom=spring, label='summer')
plt.bar(year, autumn, bottom=spring+summer, label='autumn')
plt.bar(year, winter, bottom=spring+summer+autumn, label='winter')
plt.title('precipitation')
plt.xlabel('year')
plt.ylabel('mm')
plt.legend()
plt.show()

#9-16
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi*2, 100)

plt.subplot(2,1,1)
plt.plot(x, np.sin(x), label='sin')
plt.legend()
plt.subplot(2,1,2)
plt.plot(x,np.cos(x), label='cos')
plt.legend()
plt.show()

#9-17
import numpy as np
import matplotlib.pyplot as plt

math = np.array([75, 89, 75, 65, 79])
english = np.array([85, 80, 90, 75, 88])
korean = np.array([72, 90, 70, 88, 93])
x = ['math', 'english', 'korean']

plt.figure(figsize=(5,3))
plt.bar(x, [np.mean(math), np.mean(english), np.mean(korean)])
plt.ylabel('score')
plt.show()

#9-18
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(1000)

plt.figure(figsize=(5,3))
plt.hist(x, bins=40, alpha=0.5)
plt.ylabel('frequency')
plt.show()

#9-19
import numpy as np

score = np.array([71, 80, 60, 90, 65])
result = np.where(score>=90, 'A',
                  np.where(score>=80, 'B',
                           np.where(score>=70, 'C', 'D')))
print(result)

#9-20
import numpy as np
import matplotlib.pyplot as plt

months = np.arange(1,13)
num_cases = [11, 2920, 6636, 750, 615, 1141, 1044, 5473, 3707, 2444, 7324, 26198]
cum_cases = np.cumsum(num_cases)

plt.figure(figsize=(5,3))
plt.plot(months, num_cases, label='number of cases')
plt.plot(months, cum_cases, label='accumulated number of cases')
plt.xlabel('month')
plt.legend()
plt.show()

#9-21
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(5,3))
for i in range(3):
    coin = np.random.randint(0,2,5000)
    ind = np.arange(1, len(coin)+1)
    p_c = np.cumsum(coin)/ind*100
    plt.plot(ind, p_c)
plt.ylim(0,100)
plt.ylabel('%')
plt.show()

#플러스 예제 - 막대그래프
import numpy as np
import matplotlib.pyplot as plt

year = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
boy = [248958,223883,223356,224906,208064,184308,167686,155416,139362,133516]
girl = [235592,212572,212079,213514,198179,173463,159136,147260,132975,127046]

ind = np.arange(len(year))

w = 0.4
plt.figure(figsize=(6,3.5))
plt.bar(ind-w/2, boy, color='b', width=w, label='boy')
plt.bar(ind+w/2, girl, color='r', width=w, label='girl')
plt.xticks(ind, year)
plt.legend()
plt.xlabel('year')
plt.ylabel('number of births')
plt.show()

#플러스 예제 - 누적 막대 그래프
import numpy as np
import matplotlib.pyplot as plt

year = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
boy = np.array([248958,223883,223356,224906,208064,184308,167686,155416,139362,133516])
girl = np.array([235592,212572,212079,213514,198179,173463,159136,147260,132975,127046])

ind = np.arange(len(year))

plt.figure(figsize=(6,3.5))
plt.bar(ind, boy, color='b', label='boy')
plt.bar(ind, girl, bottom = boy, color='r', label='girl')
plt.xticks(ind, year)
plt.legend()
plt.xlabel('year')
plt.ylabel('number of births')
plt.show()