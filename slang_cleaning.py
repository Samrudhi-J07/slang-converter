import pandas as pd

def load_slang_dictionary():
    df = pd.read_csv("slang_dictionary.csv")
    return dict(zip(df['slang'], df['meaning']))

def convert_slang(text, slang_dict):
    words = text.lower().split()
    cleaned_words = [slang_dict.get(w, w) for w in words]
    return " ".join(cleaned_words)

if __name__ == "__main__":
    slang_dict = load_slang_dictionary()
    user_input = input("Enter text with slang: ")
    cleaned_text = convert_slang(user_input, slang_dict)
    print("Converted Meaning:", cleaned_text)
