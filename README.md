# Group Project for AI4SE
## Train a LEVENSHTEIN Transformer from Scratch
### prerequests:
PyTorch version >= 1.5.0  
Python version >= 3.6  
Transformers  
NVIDIA GPU
### Install Fairseq
Instructions can be found in this link.
https://github.com/pytorch/fairseq  
However, to train the LevT you may need more instructions:
https://github.com/pytorch/fairseq/issues/2010  
### Prepare the dataset
1. Download Java_small from this link: https://drive.google.com/drive/folders/119LINibZk3hS1dqGqtjuBxvEQtQ5hSTx?usp=sharing, or your dataset.  
2. Use `/data_process/tokenizer.py` to tokenize the data with CodeBert tokenizer
3. `sh process.sh` to preprocess input data so that they can be used by a fairseq model. Please set the prefix and suffix of the files.
### Train the model
Run `sh train.sh` to start training. You may need to change some configurations in this script. More details in this link: https://fairseq.readthedocs.io/en/latest/command_line_tools.html  

