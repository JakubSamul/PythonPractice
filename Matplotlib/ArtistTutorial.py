# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(2, 1, 1)  # two rows, one column, first plot

# fig2 = plt.figure()
# ax2 = fig2.add_axes([0.15, 0.1, 0.7, 0.3])

# import numpy as np

# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2 * np.pi * t)
# (line,) = ax.plot(t, s, color="blue", lw=2)

# In [101]: ax.lines[0]
# Out[101]: <matplotlib.lines.Line2D at 0x19a95710>

# In [102]: line
# Out[102]: <matplotlib.lines.Line2D at 0x19a95710>

# line = ax.lines[0]
# line.remove()

# xtext = ax.set_xlabel('my xdata')  # returns a Text instance
# ytext = ax.set_ylabel('my ydata')

# import matplotlib.pyplot as plt
# import numpy as np

# fig = plt.figure()
# fig.subplots_adjust(top=0.8)
# ax1 = fig.add_subplot(211)
# ax1.set_ylabel("Voltage [V]")
# ax1.set_title("A sine wave")

# t = np.arange(0.0, 1.0, 0.01)
# s = np.sin(2 * np.pi * t)
# (line,) = ax1.plot(t, s, color="blue", lw=2)

# # Fixing random state for reproducibility
# np.random.seed(19680801)

# ax2 = fig.add_axes([0.15, 0.1, 0.7, 0.3])
# n, bins, patches = ax2.hist(np.random.randn(1000), 50, facecolor="yellow", edgecolor="yellow")
# ax2.set_xlabel("Time [s]")


# plt.show()

import matplotlib.lines as lines
import matplotlib.pyplot as plt

fig = plt.figure()

l1 = lines.Line2D([0, 1], [0, 1], transform=fig.transFigure, figure=fig)
l2 = lines.Line2D([0, 1], [1, 0], transform=fig.transFigure, figure=fig)
fig.lines.extend([l1, l2])

plt.show()
