corpus_path = "python_corpus.txt"

# Read the entire file
with open(corpus_path, "r", encoding="utf-8") as f:
    python_corpus = f.read()

print("Loaded Python corpus successfully!")
print(f"Corpus size: {len(python_corpus):,} characters")


# now we do the magic and perform tokenization 

