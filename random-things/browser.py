from webbrowser import open

try:
    site=input('Digite a url do site que deseja visitar: ')
    open(site)
except:
    print('URL digitada inválida..')
    print()
