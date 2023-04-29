import requests
from bs4 import BeautilfulSoup as bs

#Peticion GET a la web
url =""

response = requuests.get(url)

#Utilizo Bs para parsear el codigo HTML de la pagina
soup = bs(response.content, "html.parser")

print(soup.prettify())