# criar dicionário de filmes com chave e valor,
# contendo as categorias e os filmes respectivamente
filmes ={
    "Drama":["D1 - ","D2 - ","D3 - "],
    "Comédia":["C1 - ","C2 - ","C3 - "],
    "Policial":["P1 - ","P2 - ","P3 - "],
    "Guerra":["G1 - ","G2 - ","G3 - "],
    }
# open(file, mode)
pagina = open("filmes.html","w")

# "w" - Write - sobrescreve conteúdo existente
# "a" - Append - adiciona no final do arquivo
pagina.write("""
<hmtl lang="pt-br">
<head>
<title>Pagina HTML com Python</title>
</head>
<body>
<h1>Catálogo de Filmes</h1>
""")

for c,v in filmes.items():
    pagina.write("<h1>%s</h1>" % c)
    for e in v:
        pagina.write("<p>%s</p>" % e)
pagina.write("""
</body>
</html>
""")

pagina.close()
