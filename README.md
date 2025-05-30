# Dashboard de Livraria Online – Web Scraping + Power BI

Este projeto realiza web scraping do site [Books to Scrape](https://books.toscrape.com/) para extrair informações sobre livros, trata os dados com Python e os visualiza em um dashboard interativo no Power BI.

## Tecnologias Utilizadas

- **Python**: Utilizado para fazer scraping e tratamento de dados.
- **BeautifulSoup 4**: Biblioteca para extrair dados de páginas HTML.
- **Pandas**: Manipulação e limpeza dos dados.
- **Power BI**: Criação de visualizações interativas.
- **JSON**: Formato intermediário dos dados tratados.

## Estrutura da base de dados
A base da Books to Scrape contém informações do livro:
- Título
- Categoria
- Preço
- Avaliação
- Link da Capa do livro
- Situação do Estoque

## Indicadores no dashboard
- Quantidade de livros na categoria selecionada
- Avaliação média da categoria
- Componente de filtro que exibe as capas dos livros; ao selecionar uma, detalhes como título, preço e avaliação são apresentados
- Quantidade de livros na Books to Scrape
- Preço médio de todos os livros
- Avaliação média de todos os livros por categoria
- Visualização combinada de colunas e linhas exibindo a quantidade de livros e a média de avaliações por categoria
- 
## Fonte dos dados
[Books to Scrape](https://books.toscrape.com/)
