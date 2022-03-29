# import all the relevant Libraries to our project
import requests
from bs4 import*
import os
import urllib.request

###--Create a function that takes a URL from the user And takes out of it:
## 1. All the pages that exist on the site
## 2. All the links that exist on the site
## 3. All the image and PDF files that exist on the site


def web_content(url):
    url = input(str('enter your website: '))

    ###--print all the pages in a website---####
    r = requests.get(url).text
    soup = BeautifulSoup(r, 'html.parser')
    tags = soup.find_all('a')
    pages = []
    print('all tabs: ')
    for tag in tags:
        if 'href' in tag.attrs:
            pages.append(str(tag.attrs['href']))
            print(str(tag.attrs['href']) + '\n')

    ######## export all the links from a website #######
    links = []
    web = urllib.request.urlopen(url)
    soup2 = BeautifulSoup(web, "html.parser")
    for link in soup2.findAll('a'):
        links.append(link.get('href'))
    print('all links: ')
    print(links)

    ####### Downkoad all the image from a website ########
    try:
        folder_name = 'web all img'
        os.mkdir(folder_name)
    except:
        print("Folder Exist with that name!")

    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    images = soup.find_all('img')
    count = 1

    for img in images:
        if ('.jpg' in img.get('src', [])):
            img_link = requests.get(img.get('src'))
            file = open(f"{folder_name}\\{count}.jpg" ,'wb')
            file.write(img_link.content)
            count += 1
            file.close()

    ####### Downkoad all the PDF from a website ########
    try:
        folder_name2 = 'web all pdf'
        os.mkdir(folder_name2)
    except:
        print("Folder Exist with that name!")

    all_pdf = soup.find_all('a')
    count2 = 1

    for pdf in all_pdf:
        if ('.pdf' in pdf.get('href', [])):
            r = requests.get(pdf.get('href'))
            pdf_file = open(f'{folder_name2}\\{count2}.pdf','wb')
            pdf_file.write(r.content)
            count2 += 1
            pdf_file.close()
web_content('url')

