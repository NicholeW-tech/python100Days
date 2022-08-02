import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

print(nato_dict)


def generate_phonetic():
    user_word = list(input("Type a word you would like coded: \n").upper())
    try:
        output_list = [nato_dict[letter] for letter in user_word]
    except KeyError:
        print("incorrect input")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
