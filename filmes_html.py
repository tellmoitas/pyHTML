pagina = open("index3.html","w")

pagina.write("""
<hmtl lang="pt-br">
<head>
<title>Pagina HTML com Python</title>
</head>
<body>
<h1>CONTADOR</h1>
""")
for n in range(6):
    pagina.write("<h3>%d</h3>\n" % n)

pagina.write("""
</body>
</html>
""")

pagina.close()
