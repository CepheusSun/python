#coding=utf-8
def get_new_str_sort(s):
    l = list(s)
    l.sort()
    s = "".join(l)
    return s
stopword = ''
str = ''
dict={}
for line in iter(raw_input, stopword):
  sort_s=get_new_str_sort(line)
  if sort_s in dict:
      dict[sort_s ].append(line)
  else:
      dict[sort_s ]=[ line ]
lst=[]
len_lst=[]
new_dic={};

for (k,v) in  dict.items():
    #v.sort()
    one_len=len(v)
    if  one_len not in len_lst:
        len_lst.append(one_len)
    if one_len in new_dic:
        new_dic[one_len].append( v[0] )
    else:
        new_dic[one_len]=[  v[0] ]
len_lst.sort(reverse=True)

all_word=[]
for word_num in len_lst:
    for keys in new_dic[word_num]:
        new_keys=get_new_str_sort(keys);
        print ' '.join(dict[new_keys])
