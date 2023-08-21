import pandas as pd

df_nato = pd.read_csv("nato_phonetic_alphabet.csv") # index_col=0
# nato = df_nato.to_dict()["code"]

# 1. Create a dictionary in this format:
nato = {alpha["letter"]:alpha["code"] for letter, alpha in df_nato.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Word: ").upper()
phonetic = [nato[letter] for letter in user if letter in nato]

print(phonetic)
