pagina = open("index3.html","w")

pagina.write("<hmtl lang=\"pt-br\">\n")

pagina.write("<head>\n")
pagina.write("<title>Pagina HTTML com Python</title>")
pagina.write("</head>\n")

pagina.write("<body>\n")

aluno = "Luiz"
pagina.write("<h1>%s</h1>\n" % aluno)

pagina.write("</body>\n")

pagina.write("</html>\n")

pagina.close()
