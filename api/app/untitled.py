import requests
from bs4 import BeautifulSoup
import urllib3
import typing

urllib3.disable_warnings()


url_poder_judicial = "http://www.poderjudicialvirtual.com/mn-banco-santander-mexico-s-a--banco-santander-mexico"
url_poder_judicial = "https://www.poderjudicialvirtual.com/df-tramontina-de-mexico-s-a-de-c-v--ideas-domesticas-s-a-de-c-v-oral-mercantil"
s = requests.Session()
res = s.get(url_poder_judicial, verify=False)

soup = BeautifulSoup(res.text)
t = soup.select('div#pcont div.content p')[0].text.split()
c = soup.select('div#pcont div.content p')[1].text.split()

text = " ".join(t)

juzgado_pos = text.find(" > ")
actor_pos = text.find("Actor:")
demandado_pos = text.find("Demandado:")

actor = text[actor_pos + 7:demandado_pos - 1]
demandado = text[demandado_pos + 11:]
juzgado = text[juzgado_pos + 3:actor_pos - 1]
estado = text[:juzgado_pos]

expediente = c[3]
notificaciones = c[-2]
c.pop(0)
resumen = " ".join(c)

data = {
    "actor": actor,
    "demandado": demandado,
    "juzgado": juzgado,
    "estado": estado,
    "expediente": expediente,
    "notificaciones": notificaciones,
    "resumen": resumen,
}






return data
