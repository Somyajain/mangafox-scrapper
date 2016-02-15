import requests
import bs4
import os

manga_name=raw_input("Which manga do you wish to download:")
begin=input("Enter first chapter:")
number_chap=input("Enter how many chapters you want:")

#for creating url:
list_of_words=manga_name.split(" ")
m=''
for g in list_of_words:
    m=m+g+'_'
    
manga_name_url=m[:-1]

dir_name=os.getcwd()
# making folder

if not os.path.exists(dir_name+"\manga1"):
    os.mkdir('manga1')
os.chdir(dir_name+'\manga1')
if not os.path.exists(dir_name+"\manga1"+"\\"+manga_name):
    os.mkdir(manga_name)
os.chdir(dir_name+'\manga1'+"\\"+manga_name)




for k in range(begin,begin+number_chap):
    count=1
    

    url_page=requests.get('http://mangafox.me/manga/'+manga_name_url+'/c'+str(k)+'/'+str(count)+".html")
    print 'http://mangafox.me/manga/'+manga_name_url+'/c'+str(k)+'/'
    
    if not os.path.exists(dir_name+'\manga1'+"\\"+manga_name+'\chapter'+str(k)):
        os.mkdir('chapter'+str(k))
    os.chdir(dir_name+'\manga1'+"\\"+manga_name+'\chapter'+str(k))
    url_soup=bs4.BeautifulSoup(url_page.content)
    
    c=str(url_soup.find(onchange='change_page(this)'))
    f=c.count('option value')
    for e in range(1,f+1):
        url_page=requests.get('http://mangafox.me/manga/'+manga_name_url+'/c'+str(k)+'/'+str(e)+".html")

        url_soup=bs4.BeautifulSoup(url_page.content)
        img_div=url_soup.find(id='image')
        print img_div
        src=img_div.get('src')
        page=open('page'+str(e)+'.jpeg',"wb+")
        page2=requests.get(src)
        page.write(page2.content)
        page.close()

        
        
        print url_page.status_code, k ," : chapter .." , e, ": page"
        
    os.chdir(dir_name+'\manga1'+"\\"+manga_name)    

        
