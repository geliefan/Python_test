
# coding: utf-8
import MeCab
import codecs

def getNoun(text):
  tagger = MeCab.Tagger('-u user.dic')
  node=tagger.parseToNode(text.encode('utf-8'))
  nouns={}
  while node:
    noun=node.feature.split(",")[0]
    if noun==r'名詞':
      nouns.setdefault(node.surface.decode("utf-8"),0)
      nouns[node.surface.decode("utf-8")]+=1
    node=node.next
  return nouns

text=codecs.open('hanrei03.txt','r','utf-8').read()
nouns=getNoun(text)
for k,v in sorted(nouns.items(),key=lambda x:x[1]):
  print k,v
  
