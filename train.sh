!CUDA_VISIBLE_DEVICES=0 fairseq-train \
    data-bin/java_small \
    --save-dir /content/drive/MyDrive/fairseq/checkpoints_lev \
    --tensorboard-logdir /content/drive/MyDrive/fairseq/tb_lev \
    --ddp-backend=legacy_ddp \
    --task translation_lev \
    --criterion nat_loss \
    --arch levenshtein_transformer \
    --noise random_delete \
    --share-all-embeddings \
    --optimizer adam --adam-betas '(0.9,0.98)' \
    --lr 0.0005 --lr-scheduler inverse_sqrt \
    --stop-min-lr '1e-09' --warmup-updates 4000 \
    --warmup-init-lr '1e-07' --label-smoothing 0.1 \
    --dropout 0.3 --weight-decay 0.01 \
    --decoder-learned-pos \
    --encoder-learned-pos \
    --apply-bert-init \
    --log-format 'simple' --log-interval 100 \
    --fixed-validation-seed 7 \
    --batch-size 16 \
    --max-source-positions 256 \
    --max-target-positions 256 \
    --save-interval-updates 10000 \
    --max-update 300000 \
    --max-epoch 300\
    --validate-interval 3\
    --save-interval 10 \
    --skip-invalid-size-inputs-valid-test \
    --eval-bleu \
    --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \
    --eval-bleu-detok moses \
    --eval-bleu-remove-bpe \
    --eval-bleu-print-samples \