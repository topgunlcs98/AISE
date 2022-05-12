fairseq-preprocess --source-lang tokens_prev --target-lang tokens_next \
    --trainpref /content/drive/MyDrive/fairseq/java_token/train --validpref /content/drive/MyDrive/fairseq/java_token/eval --testpref /content/drive/MyDrive/fairseq/java_token/test \
    --destdir data-bin/java_small --joined-dictionary