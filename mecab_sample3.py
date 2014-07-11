#coding:utf-8
import MeCab

def extractKeyword(text):
    """textを形態素解析して、名詞のみのリストを返す"""
    tagger = MeCab.Tagger('-Ochasen')
    node = tagger.parseToNode(text.encode('utf-8'))
    keywords = []
    while node:
        if node.feature.split(",")[0] == u"名詞":
            keywords.append(node.surface.decode('utf-8'))
        node = node.next
    return keywords

if __name__ == "__main__":
    keywords = extractKeyword(u"改竄されたサイトを特定の環境で閲覧するとIEがクラッシュし、その背後でコードが実行され、情報漏洩の原因となるマルウェアに感染する
")
    for w in keywords:
        print w,
    print
                              
    keywords = extractKeyword(u"菅直人首相は野党の出方や世論を見極めつつ判断する考えだ。")
    for w in keywords:
        print w,

