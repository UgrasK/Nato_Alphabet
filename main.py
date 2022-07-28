import pandas

# convert csv into dataframe with pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary from dataframe with dict comprehension
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    # take user input
    word = input("Enter a word: ").upper()

    # show user input as nato alphabet
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()