import pandas as pd

def load_slang_dictionary():
    df = pd.read_csv("slang_dictionary.csv")
    return dict(zip(df['slang'], df['meaning']))

slang_dict = load_slang_dictionary()

def convert_slang(text):
    words = text.split()
    output = []
    for w in words:
        output.append(slang_dict.get(w.lower(), w))
    return " ".join(output)
