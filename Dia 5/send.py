import http.client

conn = http.client.HTTPSConnection("api.botmaker.com")

headers = {
    'Content-Type': "application/json",
    'access-token': "eyJhbGciOiJIUzUxMiJ9.eyJidXNpbmVzc0lkIjoidmlzaXRhcnNybCIsIm5hbWUiOiJUb21hcyBIaWVzZSIsImFwaSI6dHJ1ZSwiaWQiOiJHdXZzeVhKREpvYUVjUGFRSkpPa0JFUTlTamgxIiwiZXhwIjoxODQ4NzY1MzE2LCJqdGkiOiJHdXZzeVhKREpvYUVjUGFRSkpPa0JFUTlTamgxIn0.EJLVm8wzQMouMMV94Voq-CExBX6P6w6hosvhmDy06EZqC1UgAm9AMq4Pdb_CuzvbfE3tNLTgA06CLa6ezmSRjw"
    }

def saludar{

}

conn.request("GET", "/v2.0/whatsapp/templates/prueba01", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))