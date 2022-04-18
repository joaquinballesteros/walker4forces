#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas
import matplotlib
import matplotlib.pyplot as plt
data = pandas.read_csv("HS-I.csv")
data
data["data"]
plt.plot(data["data"])
plt.xlabel("Time(s)")
plt.ylabel("Force(N)")
plt.title("Force of Healthy Subject I")


# In[1]:


import pandas as pd
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
# Make a list of columns
columns = ['Time (s)', 'Force 1(N)', 'Force 2(N)', 'Force 3(N)', 'Force 4(N)']
df = pd.read_csv("HS-II.csv", usecols=columns)
# Plot the lines
df.plot()
plt.show()


# In[3]:


import pandas as pd
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
# Make a list of columns
columns = ['Time (s)', 'Force 1(N)', 'Force 2(N)', 'Force 3(N)', 'Force 4(N)']
df = pd.read_csv("HS-II.csv", usecols=columns)
# Plot the lines
df.plot()
plt.xlabel("Time(s)")
plt.ylabel("Force(N)")
plt.title("Force of Healthy Subject I")
plt.show()


# In[4]:


import pandas as pd
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
# Make a list of columns
columns = ['Time (s)', 'Force 1(N)', 'Force 2(N)', 'Force 3(N)', 'Force 4(N)']
df = pd.read_csv("HS-II.csv", usecols=columns)
# Plot the lines
df.plot()
df.set_index('Time (s)').plot()
plt.xlabel("Time(s)")
plt.ylabel("Force(N)")
plt.title("Force of Healthy Subject I")
plt.show()


# In[5]:


import pandas as pd
from matplotlib import pyplot as plt

# Set the figure size
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
# Make a list of columns
columns = ['Time (s)', 'Force 1(N)', 'Force 2(N)', 'Force 3(N)', 'Force 4(N)']
df = pd.read_csv("HS-II.csv", usecols=columns)
# Plot the lines
df.set_index('Time (s)').plot()
plt.xlabel("Time(s)")
plt.ylabel("Force(N)")
plt.title("Force of Healthy Subject I")
plt.show()


# In[ ]:




