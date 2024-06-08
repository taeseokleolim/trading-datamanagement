import yaml

from fastapi import FastAPI
from connector import Connector


cfg = yaml.safe_load(open("config.yaml"))
app = FastAPI()
conn = Connector()


@app.get("/update_ACCESS_TOKEN")
def update_ACCESS_TOKEN():
    conn.ACCESS_TOKEN = conn.get_access_token()

@app.get("/update_price")
def update_price():
    data = conn.inquire_price(cfg['nasdaq_SRS_CD'])
    