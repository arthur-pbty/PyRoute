def page_html(page):
   with open(f'resources/views/{page}.html', 'r', encoding='utf-8') as fichier_html:
      res = fichier_html.read()
   return res

def page_css_js(page, type):
   with open(f'resources/{type}/{page}.{type}', 'r', encoding='utf-8') as fichier_css_js:
      res = fichier_css_js.read()
   return res