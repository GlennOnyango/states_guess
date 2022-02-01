import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv");
print(df.to_dict())
nato_dict = {value.letter: value.code for (key, value) in df.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter your name")


name_list = [nato_dict.get(n)  for n in name.upper()]

print(name_list)


