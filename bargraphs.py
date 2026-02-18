
import matplotlib.pyplot as plt

x = [1,2,3,4,5]

y = [19,24,8,20,17]

plt.bar(x,y)

plt.show()

#horizontal bargraphs

x = [1,2,3,4,5]

y = [10,20,30,40,50]

plt.barh(x,y,height = 0.4)
plt.xlabel('sales info')
plt.ylabel('product')

plt.barh(x,y,height = 0.4)
plt.show()
