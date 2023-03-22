from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

# Run these statements only once
import nltk
nltk.download("stopwords")
nltk.download("punkt")

def removeStopWord(sentence: str):
    newText = ""
    tokens = wordpunct_tokenize(sentence)
    for token in tokens:
        if token not in set(stopwords.words("english")):
            newText += token+" "
    return newText


if __name__ == "__main__":
    with open("stopWord.txt") as file2:
        words = file2.read()
        newText = removeStopWord(words)

        print(f"Original text: {words}")
        print(f"Stop word removed text: {newText}")
