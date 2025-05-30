import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "https://books.toscrape.com/"
pagina = "catalogue/page-1.html"
livros = []

while pagina:
    url = base_url + pagina
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    livros_elementos = soup.select(".product_pod")

    for artigo in livros_elementos:
        titulo = artigo.h3.a['title']
        preco_str = artigo.select_one(".price_color").text.strip().replace("£", "").replace("Â", "")
        estoque = artigo.select_one(".availability").text.strip()
        nota = artigo.p['class'][1]
        link_relativo = artigo.h3.a['href'].replace('../../../', '')
        link_livro = base_url + "catalogue/" + link_relativo

        # Requisição à página interna do livro
        detalhes = requests.get(link_livro)
        detalhes.encoding = detalhes.apparent_encoding
        soup_detalhes = BeautifulSoup(detalhes.text, 'html.parser')

        # Categoria do livro (segunda posição do breadcrumb)
        categoria = soup_detalhes.select("ul.breadcrumb li a")[2].text.strip()

        # Link da imagem
        img_rel = soup_detalhes.select_one(".item.active img")['src'].replace("../../", "")
        link_img = base_url + img_rel

        try:
            preco = float(preco_str)
        except ValueError:
            preco = None

        livros.append({
            "Título": titulo,
            "Preço": preco,
            "Estoque": estoque,
            "Nota": nota,
            "Categoria": categoria,
            "Link Imagem": link_img
        })

        time.sleep(0.3)  # Pausa entre cada livro

    # Próxima página
    proxima = soup.select_one("li.next > a")
    if proxima:
        pagina = "catalogue/" + proxima['href']
    else:
        pagina = None

    time.sleep(1.0)  # Pausa entre páginas

df = pd.DataFrame(livros)

# Transformar a nota de avaliação para número
notas_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Nota'] = df['Nota'].map(notas_dict)

# Coluna da situação estoque convertida para uma coluna binário
df['Em Estoque'] = df['Estoque'].str.contains("In stock").astype(int)
df = df.drop("Estoque", axis=1)

# Salvar arquivo Json
df.to_json('Dados.json', orient='records', indent=4, force_ascii=False)