import lxml.etree as ET
import codecs
import re
 
def main():
    pass
 
if __name__ == "__main__":
    iterparse = ET.iterparse
    f = codecs.open('abstract2.txt','w','utf_8')
    """消すもの:カッコ・wikiのタグ(|=)"""
    r1 = re.compile('[\[|(（].*?[|\]））]|[|].*?[=]')
    xml_iter = iterparse("jawiki-20140624-abstract1.xml",events =('end',) ,tag = 'abstract')
    for event,elm in xml_iter:
            abstract = elm.text
            while elm.getprevious() is not None:
                del elm.getparent()[0]
            elm.clear()
            if abstract is not None:
                abstract = r1.sub('', abstract)
                abstract = abstract.replace('。','\n')
                abstract = abstract.replace(' ','')
                f.writelines(abstract)
    f.close();
    print("finished")
