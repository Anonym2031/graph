from networkx import *
import matplotlib.pyplot as plt
g = read_edgelist("G.txt")
print(attr_matrix(g))
print(info(g))
nx.draw(g, with_labels=True, font_weight='bold')
plt.savefig('graph.png')
plt.show()
plt.close()

