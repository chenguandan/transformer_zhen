
# data_file = r"D:\Users\guandan\Documents\ch_en\UM-Corpus\data\Testing\Testing-Data.txt"
# data_file_out = r'D:\Users\guandan\Documents\ch_en\parallel\casict2011\um_corpus_test_ch.txt'
# data_file_out_en = r'D:\Users\guandan\Documents\ch_en\parallel\casict2011\um_corpus_test_en.txt'
#
# line_num = 0
# with open(data_file, encoding='utf-8') as fin:
#     with open(data_file_out, 'w', encoding='utf-8') as fout,\
#             open(data_file_out_en, 'w', encoding='utf-8') as fout_en:
#         for line in fin:
#             if line_num %2 ==0:
#                 fout_en.write(line)
#             else:
#                 fout.write(line)
#             line_num += 1
# print('done.')

import jieba
raw_string = '我们中国人'
raw_string = ' '.join(jieba.cut(raw_string, cut_all=False))
print(raw_string)