import pandas as pd

df = pd.read_csv('dwarf_stars.csv')
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]

df['Radius'] = 0.102763 * df['Radius']
df['Mass'] = 0.000954588 * df['Mass']

df.to_csv("Project129.csv")