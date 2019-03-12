import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create a series (one dimensional array- like a vector)
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print(s[1])
type(s[1])


dates = pd.date_range('20130101', periods=6)



plt.rcParams['figure.figsize'] = (15,5)  # set figure size

