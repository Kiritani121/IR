from nltk.tokenize import wordpunct_tokenize
from preProcess import removeStopWord

if __name__ == "__main__":
    f1_Set = {}
    f2_Set = {}

    # Reading the files removing the stopwords and tokenizing them
    with open("document1.txt") as f1, open("document2.txt") as f2:
        f1_Set = set(wordpunct_tokenize(removeStopWord(f1.read())))
        f2_Set = set(wordpunct_tokenize(removeStopWord(f2.read())))

    # form a set containing keywords of both strings 
    rvector = f1_Set.union(f2_Set)

    # forming a vector for presence and absence of word in both files
    l1=[];l2=[]
    for w in rvector:
        if w in f1_Set: l1.append(1)
        else: l1.append(0)
        if w in f2_Set: l2.append(1)
        else: l2.append(0)
    
    # cosine formula 
    c = 0
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    print("Similarity: ", cosine)
