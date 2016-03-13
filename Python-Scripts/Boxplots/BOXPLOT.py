import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")
sns.set(style="ticks", palette='Set2', font='Roboto Condensed')
sns.set_context("paper", font_scale=1.1, rc={"lines.linewidth": 1.1})
g=sns.factorplot(x="time", y="total_bill", hue="smoker",
               col="day", data=tips, kind="box", size=4, aspect=0.5,
                 width=0.8,fliersize=2.5,linewidth=1.1, notch=False,orient="v")
sns.despine(trim=True)
g.savefig('test6.png', format='png', dpi=600)
