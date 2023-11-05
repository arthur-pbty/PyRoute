from modules import page_html, page_css_js


def page_accueil():
   return page_html('welcome')

def page_accueil_css():
   return page_css_js('style','css')

def a_propos():
   return page_html('aboute')

def a_propos_css():
   return page_css_js('aboute','css')