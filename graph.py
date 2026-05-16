import matplotlib.pyplot as plt

time = [0,1,2,3,4,5,6]
sea_level = [1.2,1.5,1.1,2.0,1.8,1.3,1.6]

plt.plot(time, sea_level, marker='o')

plt.title("Sea Level Variation")
plt.xlabel("Time (hours)")
plt.ylabel("Sea Level (m)")

plt.savefig("Sea_level_graph.png")

plt.show()

