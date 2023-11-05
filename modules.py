def page_html(page):
   with open(f'resources/views/{page}.html', 'r') as fichier_html:
      res = fichier_html.read()
   return res