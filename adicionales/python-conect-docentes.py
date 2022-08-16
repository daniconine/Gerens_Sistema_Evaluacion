########### Python 3.2 #############
from base64 import encode
import encodings
import urllib.request, json

try:
    url = "https://api.q10.com/v1/docentes?Limit=30&Offset=1"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Api-Key': 'accbfd273dbb4915b44008869f5d8783',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    "print(response.getcode())"
    "print(response.read())"
    print("/n")
    
except Exception as e:
    print(e)

data= response.read()
data = data.decode("utf-8").replace("'", '"')
#print(data)
print(type(data))

diccionario = json.loads(data)
print(diccionario)

#creacion de archivo json
with open("docentes.json", 'w',encoding="utf-8") as archivo_nuevo:
    json.dump(diccionario, archivo_nuevo ,ensure_ascii= False, indent=4) 




####################################

