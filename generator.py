import urllib.request
import requests
import os

r = requests.post("http://targetsrl.ddns.net/gom/inc/dbcall/db_gestione.php", {"caso":"elenco_location"})
locations = r.json()
if(not os.path.exists("images")):
    os.mkdir("images")
    print("Create images Folder")

for i in range(0,len(locations)):
    nome = locations[i]["nome"]
    print("Request and download image for " + nome)
    urllib.request.urlretrieve("https://picsum.photos/500/500.jpg", "images/"+nome+".png")
    print(str(i) + " - Downloaded" )