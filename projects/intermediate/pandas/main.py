import pandas as pd

data = pd.read_csv("squirrel_data.csv")

primary_color = data["Primary Fur Color"].dropna()

colors = primary_color.unique()

colors_squirrel = {"Fur Color": colors}

list_count = []
for color in colors:
    list_count.append(len(data[data["Primary Fur Color"] == color]))

colors_squirrel["Count"] = list_count
df_squirrels = pd.DataFrame(colors_squirrel)

df_squirrels.to_csv("count_color_squirrels.csv")

