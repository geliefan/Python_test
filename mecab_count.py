# coding: utf-8
import MeCab
import codecs

def getNoun(text):
  tagger=MeCab.Tagger("-Ochasen")
  node=tagger.parseToNode(text.encode('utf-8'))
  nouns={}
  while node:
    noun=node.feature.split(",")[0]
    if noun==r'動詞':
      nn = node.surface.decode("utf-8") # デコードする
      nouns.setdefault(nn,0)
      nouns[nn]+=1
    node=node.next
  return nouns

text=codecs.open('hanrei.txt','r','utf-8').read()
nouns=getNoun(text)
for k,v in sorted(nouns.items(),key=lambda x:x[1]):
  #if v>40:
  print k,v
