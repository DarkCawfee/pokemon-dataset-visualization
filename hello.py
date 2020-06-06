import matplotlib.pyplot as plt
import pandas as pd

pokemon = pd.read_csv('Pokemon.csv', index_col)
poke_x = pokemon.loc[:, 'HP']
poke_y = pokemon.iloc[:, 0]

plt.scatter(poke_x, poke_y)

plt.xlabel('Health of Pokemon')
plt.ylabel('Defence')

plt.show()
