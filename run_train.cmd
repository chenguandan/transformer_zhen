set VOCAB_FILE=./data/tfrecords/vocab.zh.32768
set VOCAB_FILE_EN=./data/tfrecords/vocab.en.32768
set DATA_DIR=./data/tfrecords
set MODEL_DIR=./model_zhen
set PARAM_SET=base
python transformer_main.py --data_dir=%DATA_DIR% --model_dir=%MODEL_DIR% ^
    --vocab_file=%VOCAB_FILE% --vocab_file_en=%VOCAB_FILE_EN% --param_set=%PARAM_SET% ^
    --bleu_source=./data/translate_zhen_raw/um_corpus_test_ch.txt --bleu_ref=./data/translate_zhen_raw/um_corpus_test_en.txt