import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd 

x = [34,54,23]
y = [12321,12312,12412]

plt.plot(x,y)
plt.show()

df = pd.DataFrame(x,y)
df

print(df)