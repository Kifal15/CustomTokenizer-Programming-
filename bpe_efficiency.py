from tokenizers import Tokenizer

# Load the trained tokenizer
tokenizer = Tokenizer.from_file("bpe_python_tokenizer.json")


vocab_size = tokenizer.get_vocab_size()


print(f"Vocabulary size is , {vocab_size}")
output_file = "bpe_metrics.txt"




sentences = [
    "def add(a, b): return a + b",
    "Machine learning is fascinating!",
    "print('My name is Kifal')"
    "def multiply(a,b): return a * b"
]
with open (output_file,'w',encoding="utf-8") as f: 
    for sentence in sentences:
        tokens = tokenizer.encode(sentence)
        
        print(f"Here is the actual sentence {sentence}")
        print(f"here is the tokenized output {tokens.tokens}")
        print(f"Length of the token :{len(tokens.tokens)}")
        
        result=(
              f"Here is the actual sentence {sentence}\n",
              f"here is the tokenized output {tokens.tokens}\n",
              f"Length of the token :{len(tokens.tokens)}\n"
        )
    f.write(result) 





print("OUT OF WORD VOCABULARY")


test_sentences = [""]