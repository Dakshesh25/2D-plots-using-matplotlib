# min ----> 10

# max -------> 50

# bins = 4
# [10, 20, 20, 30, 30, 30, 40, 40, 50]

# 10 - 20    ----> 3
# 21 - 30    -----> 3
# 31 - 40    ----> 2
# 41 - 50    ---> 1

# bins grouping the values into small ranges
# fitting the values into those groups

import  matplotlib.pyplot as plt

data = [10,20,20,30,30,30,40,40,50]

plt.hist(data,bins = 4)

plt.show()
