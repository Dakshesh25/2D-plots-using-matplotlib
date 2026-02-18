import matplotlib.pyplot as plt

subjects = ["Python","Java","c++","Js"]
sizes = [30,24,55,8]
c = ["red","blue","purple","yellow"]

plt.pie(sizes,labels = subjects,autopct = "%1.2f%%",startangle = 90,colors = c)
plt.show()

# exploded piechart
subjects = ["Python","Java","c++","Js"]
sizes = [30,24,55,8]
c = ["red","blue","purple","yellow"]

ex = (0,0,0.2,0)

plt.pie(sizes,labels = subjects,autopct = "%1.2f%%",startangle = 90,colors = c, explode = ex)
plt.show()
