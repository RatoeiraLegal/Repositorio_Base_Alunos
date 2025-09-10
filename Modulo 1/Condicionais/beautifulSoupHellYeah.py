import requests
from bs4 import BeautifulSoup


patchs = []
url1 = 'https://www.guiltygear.com/ggst/en/news/post-category/patch/'
url2 = 'https://www.guiltygear.com/ggst/en/news/post-category/patch/page/2/'
url3 = 'https://www.guiltygear.com/ggst/en/news/post-category/patch/page/3/'
url4 = 'https://www.guiltygear.com/ggst/en/news/post-category/patch/page/4/'

#1
response = requests.get(url1)

print("Status: ", response.status_code)

if response.status_code == 200:
    print('Carregado com sucesso!')
else:
    print('Erro ao carregar a página')

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", class_="entry")

for link in links[:12]:
    href = link.get("href")
    if href:
        # print(href)
        patchs.append(href)

#2
response = requests.get(url2)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", class_="entry")

for link in links[:50]:
    href = link.get("href")
    if href:
        # print(href)
        patchs.append(href)

#3
response = requests.get(url3)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", class_="entry")

for link in links[:50]:
    href = link.get("href")
    if href:
        # print(href)
        patchs.append(href)

#4
response = requests.get(url4)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("a", class_="entry")

for link in links[:50]:
    href = link.get("href")
    if href:
        # print(href)
        patchs.append(href)


#dados
repetidor = 0
quantidade = len(patchs)
quantidade2 = []

#patchs
while repetidor < quantidade:
    print(f"{patchs[repetidor]}\n")
    repetidor += 1

repetidor = 0
while repetidor <= quantidade:
    quantidade2.append(repetidor)
    repetidor += 1


#seletor
while True:
    seletor = (input("Digite o número do patch que você deseja: "))
    if seletor in str(quantidade2):
        break
    else:
        print("Digite algo válido!")

#o bagulho
response = requests.get(patchs[int(seletor)])
soup = BeautifulSoup(response.text, 'html.parser')
conteudo = soup.select(".entrybody p")
print(conteudo)
    
