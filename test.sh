fairseq-generate \
    data-bin/java_small \
    --gen-subset test \
    --task translation_lev \
    --path /content/drive/MyDrive/fairseq/checkpoints_lev/checkpoint_best.pt \
    --iter-decode-max-iter 9 \
    --iter-decode-eos-penalty 0 \
    --beam 1 --remove-bpe \
    --print-step \
    --batch-size 400 \
    --results-path /content/drive/MyDrive/fairseq/lev_results\
    --skip-invalid-size-inputs-valid-test \