import requests
from lxml import html
import sys
def lyrics(global_href,filename):
    web_page_1 = requests.get(global_href)
    tree = html.fromstring(web_page_1.text)

    songs = tree.xpath('//*[@id="content-body"]/div/div/table/tbody/tr/td[1]/strong/a/@href')
    list_of_href=[]
    for a in songs:
        a = "https://www.lyrics.com/" + a
        list_of_href.append(a)
    print(list_of_href)
    for href in list_of_href:
        web_page_2 = requests.get(href)
        tree = html.fromstring(web_page_2.text)
        lyrics = tree.xpath('//*[@id="lyric-body-text"]//text()')
        perfect_lyrics="".join(lyrics)
        # print(perfect_lyrics,"\n\n\n")
        with open(filename,"a") as f:
            f.write(perfect_lyrics + "\n\n****\n\n")

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " \"<lyrics>\"")
    else:
        if lyrics(sys.argv[1],sys.argv[2]):
            lyrics(sys.argv[1], sys.argv[2])

