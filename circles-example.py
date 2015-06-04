import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]
r=[100,80, 60, 40, 20] # in points, not data units
fig, ax = plt.subplots(1,1)
ax.scatter(x, y, s=r)
fig.show()