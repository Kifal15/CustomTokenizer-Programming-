import re

# now we do the magic and perform tokenization 
'''''
def preprocess_code(code):
    """Remove comments and normalize whitespace in the Python code."""
    # Remove single-line comments
    code = re.sub(r'#.*', '', code)

    # Remove empty lines and strip extra spaces
    code = "\n".join(line.strip() for line in code.split("\n") if line.strip())

    return code

# Define the corpus file path
corpus_path = "python_corpus.txt"

# Read and preprocess the Python corpus
with open(corpus_path, "r", encoding="utf-8") as f:
    raw_code = f.read()

# Apply preprocessing
cleaned_code = preprocess_code(raw_code)

print("Preprocessing complete!")
print(f"Processed corpus size: {len(cleaned_code):,} characters")

# Save the preprocessed corpus to a new file (optional)
preprocessed_corpus_path = "preprocessed_python_corpus.txt"
with open(preprocessed_corpus_path, "w", encoding="utf-8") as f:
    f.write(cleaned_code)

print(f"Saved preprocessed corpus to {preprocessed_corpus_path}")

'''''


from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.normalizers import NFKC


# Initialize a Byte Pair Encoding (BPE) tokenizer
tokenizer =Tokenizer(BPE())
# Add pre-tokenizer to split text at the byte level
tokenizer.pretokenizer = ByteLevel()


# Define the BPE trainer with special tokens
trainer = BpeTrainer(

    vocab_size = 32000,
    min_frequency = 2 ,
    special_tokens = ["PAD" , "UNK" , "MASK" , "SEP" , "CLS" ],


)

#add normalization too 
tokenizer.normalizer = NFKC()

# Read the dataset
data =[ "preprocessed_python_corpus.txt"]

# Train the tokenizer

tokenizer.train(data, trainer)  # Use 8 threads

# Add a post-processor for handling special tokens
from tokenizers.processors import TemplateProcessing  # ✅ Import this

tokenizer.post_processor =  TemplateProcessing(



    single = "[CLS] $A [SEP]",
    pair = "[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens= { 
        ('[CLS]',tokenizer.token_to_id("[CLS]") ),
        ('[SEP]',tokenizer.token_to_id("[SEP]"))
    })

# Save tokenizer model
tokenizer.save("bpe_tokenizer.json")
print("Tokenizer training complete!")



