from tokenizers import Tokenizer

# Load the trained tokenizer
tokenizer = Tokenizer.from_file("python_bpe_tokenizer.json")
output_file = "bpe_metrics.txt"
# Get vocabulary size
vocab_size = tokenizer.get_vocab_size()
print(f"Vocabulary size is , {vocab_size}")

# Output file
with open(output_file, 'w', encoding="utf-8") as f:
    f.write(f"Vocabulary size is , {vocab_size}\n")
    print("im here ")
# Code examples
code_lines = [
    "def add(a, b): return a + b",
    "import numpy as np",
    "for i in range(10): print(i)",
    "print('Hello, World!')",
    "if x > 0: print('Positive') else: print('Negative')",
    "with open('file.txt', 'r') as f: data = f.read()",
    "class Car: def __init__(self, brand): self.brand = brand",
    "def factorial(n): return 1 if n == 0 else n * factorial(n-1)",
    "try: x = int(input()) except ValueError: print('Invalid input')",
    "import torch.nn as nn",
    "class Model(nn.Module): def __init__(self): super().__init__()",
    "lambda_func = lambda x: x**2 + 2*x + 1",
    "def greet(name): return f'Hello, {name}!'",
    "numbers = [x**2 for x in range(10) if x % 2 == 0]",
    "assert sum([1, 2, 3]) == 6, 'Sum is incorrect'",
    "from collections import Counter",
    "Counter(['apple', 'banana', 'apple', 'orange'])",
    "def reverse_string(s): return s[::-1]",
    "while True: break",
    "for key, value in {'a': 1, 'b': 2}.items(): print(key, value)",
]

# Write tokenized results
with open(output_file, 'a', encoding="utf-8") as f:
    for sentence in code_lines:
        tokens = tokenizer.encode(sentence)

        print(f"Here is the actual sentence {sentence}")
        print(f"here is the tokenized output {tokens.tokens}")
        print(f"Length of the token :{len(tokens.tokens)}")

        result = (
            f"Here is the actual sentence {sentence}\n"
            f"here is the tokenized output {tokens.tokens}\n"
            f"Length of the token :{len(tokens.tokens)}\n\n"
        )
        f.write(result)

print("OUT OF WORD VOCABULARY")

# OOV Calculation
test_sentences = code_lines
total_counts = 0
oov_counts = 0

for sentence in test_sentences:
    tokens = tokenizer.encode(sentence)
    oov_counts += tokens.tokens.count("[UNK]")  # Counting unknown tokens
    total_counts += len(tokens.tokens)

oov_rate = oov_counts / total_counts * 100 if total_counts > 0 else 0

# Append OOV results
with open(output_file, 'a', encoding="utf-8") as f:
    f.write(f"\nTotal Tokens: {total_counts}\nOOV Tokens: {oov_counts}\nOOV Rate: {oov_rate:.2f}%\n")

print(f"OOV RATE IS {oov_rate:.2f}%")
