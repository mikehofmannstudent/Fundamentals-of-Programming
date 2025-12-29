import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style='dark')
rs = np.random.RandomState(50)
f, axes = plt.subplots(3, 3, figsize=(9, 9), sharex=True, sharey=True)
for ax, s in zip(axes.flat, np.linspace(0,3,10)):
    cmap = sns.cubehelix_palette(start=s, light=1, as_cmap=True)
    x,y = rs.randn(2, 50)
    sns.kdeplot(x=x, y=y, cmap=cmap, fill=True, cut=5, ax=ax)
    ax.set(xlim=(-3, 3), ylim=(-3, 3))
    f.tight_layout()
plt.show()
