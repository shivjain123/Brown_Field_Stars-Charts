import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Stars/Stars_with_Gravity.csv')

mass_list = df["Mass"].tolist()
mass_list.sort()

radius_list = df["Radius"].tolist()
radius_list.sort()

gravity_list = df["Gravity"].tolist()
gravity_list.sort()

""" plt.plot(mass_list, radius_list)
plt.title("Mass Vs Radius")
plt.xlabel("Mass")
plt.ylabel("Radius")
plt.show() """

plt.plot(mass_list, gravity_list)
plt.title("Mass Vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()