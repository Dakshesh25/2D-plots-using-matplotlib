import matplotlib.pyplot as plt
# line plots

data = {
    'student 1' : [80, 75, 85, 90, 88],
    'student 2' : [70, 82, 78, 85, 80],
    'student 3' : [85, 80, 90, 87, 92]
}

subjects = ['Maths','Science','English','History','Geography']

for i,j in data.items():
  plt.plot(subjects,j,marker = 'o' ,label = i)

plt.grid()
plt.legend()
plt.show()

# subplots  : Subplots allow you to display multiple plots in the same figure, arranged in rows and columns.

# subplot(row,col,order)

x = [1,2,3,4,5]

# 2 rows 2 columns
y1 = [1,4,6,3,2]
y2 = [33,5,32,55,14]
y3 = [26,95,34,35,25]
y4 = [1,2,3,4,5]

plt.subplot(2,2,1)               #1st plot
plt.plot(x,y1)
plt.title("plot 1")


plt.subplot(2,2,2)               #2st plot
plt.plot(x,y2)
plt.title("plot 2")

plt.subplot(2,2,3)               #3st plot
plt.plot(x,y3)
plt.title("plot 3")

plt.subplot(2,2,4)               #4st plot
plt.plot(x,y4)
plt.title("plot 4")


plt.show()
