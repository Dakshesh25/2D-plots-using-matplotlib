import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y1 = [-33,-4,-65,-14,-72,-31,-45,-8,-42,-91]

y2 = [4,5,72,87,25,75,1,25,21,36]

plt.scatter(x,y1,color = "blue",label = "Blue",marker = "x")
plt.scatter(x,y2,color = "green",label = "Green",marker = "o")

plt.legend()
plt.show()
