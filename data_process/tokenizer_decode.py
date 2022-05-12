from transformers import AutoTokenizer
from tqdm import tqdm
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
max_length = 256
def tokenize_files(fin, fout):
    with open(fin, encoding='utf-8') as f1, open(fout, 'w', encoding='utf-8') as f2:
        for line in tqdm(f1):
            line = line.strip()
            tokens = tokenizer.tokenize(line)[:max_length]
            tokens = ' '.join(tokens)
            f2.write(tokens + '\n')

tokenize_files('./toy dataset/test.next_full_code', './toy_tokens/test.tokens_next')