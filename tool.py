import os
import requests
from bs4 import BeautifulSoup

# Hacemos una petición GET a la página web que queremos analizar
url = "https://www.ejemplo.com"
response = requests.get(url)

# Usamos BeautifulSoup para parsear el código HTML de la página
soup = BeautifulSoup(response.content, "html.parser")

# Creamos un directorio para guardar los archivos
if not os.path.exists("ejemplo"):
    os.makedirs("ejemplo")

# Guardamos el código HTML en un archivo
with open("ejemplo/index.html", "w") as file:
    file.write(str(soup))

# Extraemos los enlaces a los archivos CSS y JavaScript
css_links = [link["href"] for link in soup.find_all("link") if link.get("href") and "css" in link["href"]]
js_links = [script["src"] for script in soup.find_all("script") if script.get("src") and "js" in script["src"]]

# Descargamos y guardamos los archivos CSS y JavaScript
for link in css_links:
    css_response = requests.get(link)
    filename = "ejemplo/" + link.split("/")[-1]
    with open(filename, "w") as file:
        file.write(css_response.text)

for link in js_links:
    js_response = requests.get(link)
    filename = "ejemplo/" + link.split("/")[-1]
    with open(filename, "w") as file:
        file.write(js_response.text)