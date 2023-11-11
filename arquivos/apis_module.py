import urllib.request
import json
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask,request
import configparser

def open_notify_position():
    req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
    response = urllib.request.urlopen(req)
    obj = json.loads(response.read())
    print(obj)
    print(obj['timestamp'])
    print(obj['iss_position']['latitude'], obj['iss_position']['longitude'])

def open_notify_astros():
    url = 'http://api.open-notify.org/astros.json'
    payload = {}
    headers = {}
    response = requests.request("GET",url,headers=headers,data=payload)
    print(response.text)

def twillio():
    url = "LINK YOUR API"
    auth = HTTPBasicAuth("TOKEN","CODE")
    data = {"To":"number","From":"number","Body":"message"}
    r = requests.post(url,auth=auth,data=data)
    print(r.text)

def github():
    CLIENT_ID = ""
    CLIENT_SECRET = ""
    GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
    BASE_URL = "http://api.github.com"

    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"<a href='http://github.com/?client_id={CLIENT_ID}'>GITHUB</a>"

    @app.route("/authorize")
    def authorize():
        code = request.args.get("code")
        data = {"code":code,"client_id":CLIENT_ID,"client_secret":CLIENT_SECRET}
        headers = {"Accept":"application/json"}

        r = requests.post(GITHUB_TOKEN_URL,data=data,headers=headers)

        token = r.json()["access_token"]
        headers["Authorization",f"token {token}"]

        r_two = requests.get(BASE_URL + "/user/repos/",headers=headers)

        repos = r_two.json()
        print(json.dumps(repos,indent=2))

        list_of_repos = []
        for repo in repos:
            list_of_repos.append(repo["name"])

        return f"<h1>SUCESS CODE IS {code}</h1>"

    if __name__ == '__main__':
        app.run(debug=True)

def rest_countries():
    url = "https://restcountries.com/v3.1/"
    r = requests.get(url+"all")
    json_result = r.json()
    print(json_result[84])

    r = requests.get(url + "name/can")
    print(r.json())

    fields = {"fields":"name;currencies"}
    r = requests.get(url + "capital/tokyo",params=fields)
    print(r.json())

    post_params = {}
    post_params["fields"] = "None"

def beggining():
    url = "https://reqres.in/api/users?page=2"
    r = requests.get(url)
    print(r.text)
    print(r.json()["data"])
    for item in r.json()["data"]:
        print(item)
    
    url = "https://reqres.in/api/users?key1=ke1&key2=ke2"
    r = requests.get(url)

    headers = {"Content-Type": "application/json"}
    url = "https://reqres.in/wpo4xjwp"
    r = requests.get(url,headers)

    r = requests.post(url)
    r = requests.delete(url)
    r = requests.put(url)
    r = requests.patch(url)

    payload = {"name":"antony","job":"programmer"}
    r = requests.post("https://reqres.in/api/users",json=payload)
    print(r.text)

    r = requests.get("https://httpbin.org/basic-auth/arthur/morgan",auth=HTTPBasicAuth("user","password"))
    print(r)


def send_files():
    files = {"file":open("arquivo.jpg","rb")}
    r = requests.post("https://reqres.in/wpo4xjwp",files=files)

    files = {"file":("arquivo.jpg",open("arquivo.jpg","rb"),"image/jpeg")}
    r = requests.post("https://reqres.in/wpo4xjwp",files=files)

    r = requests.get("https://httpbin.org/image/jpeg")
    print(r.headers)
    with open("image.jpg","wb") as fd:
        for chunck in r.iter_content(chunk_size=500):
            fd.write(chunck)

    r = requests.get("https://httpbin.org/delay/0",timeout=10)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        pass

    try:
        r = requests.get("https://httpbin.org/delay/0",timeout=10)
    except requests.exceptions.ConnectionError:
        pass

def store_keys():
    config = configparser.ConfigParser()
    config["APIKeys"] = {"CHAVE","VALOR"}
    with open("secrets.ini","w") as configfile:
        config.write(configfile)
    
    config.read("secrets.ini")
    api_key = config["APIKeys"]["CHAVE"]

def store_keys_in_env():
    """NEED A VIRTUAL ENVIRONMENT AND A .env FILE"""
    from dotenv import load_dotenv
    import os
    print("store_keys in .env ",os.getenv("MY_VAR_ENVS"))