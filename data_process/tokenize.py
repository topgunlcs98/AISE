from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("huggingface/CodeBERTa-small-v1")

# sentence = "void Ġset Ġ( Ġjava . lang . Object Ġvalue Ġ, Ġjava . lang . Object Ġobject Ġ) Ġ;".split()
# token_ids = tokenizer.convert_tokens_to_ids(sentence)
# print(token_ids)
# text = tokenizer.decode(token_ids,clean_up_tokenization_spaces=False)
# print(text)
def decode(fin, fout):
    i = 0
    with open(fin, 'r', encoding='utf-8') as f1, open(fout, 'w', encoding='utf-8') as f2:
        for line in f1:
            line = line.strip()
            if i < 5:
                print(line)
                i += 1
            token_ids = tokenizer.convert_tokens_to_ids(line.split())
            text = tokenizer.decode(token_ids, clean_up_tokenization_spaces=False)
            f2.write(text+'\n')
decode('gen.out.ref', 'ref.dec')


