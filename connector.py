import requests
import yaml
import json


class Connector:
    def __init__(self, cfg):
        self.cfg = cfg
        self.ACCESS_TOKEN = self.get_access_token(cfg)
        
    def get_access_token(self):
        URL_BASE = self.cfg['URL_BASE']
        headers = {"content-type":"application/json"}
        body = {"grant_type":"client_credentials",
                "appkey": self.cfg['appkey'],
                "appsecret": self.cfg['appsecret'],
                }
        PATH = "oauth2/tokenP"
        URL = f"{URL_BASE}/{PATH}"
        res = requests.post(URL, headers=headers, data=json.dumps(body))
        ACCESS_TOKEN = res.json()["access_token"]
        return ACCESS_TOKEN
    
    def inquire_price(self, SRS_CD):
        PATH = "/uapi/overseas-futureoption/v1/quotations/inquire-price"
        URL = f"{self.cfg['URL_BASE']}/{PATH}"
        headers = {
            "Content-Type":"application/json", 
            "authorization": f"Bearer {self.ACCESS_TOKEN}",
            "appKey": self.cfg['appkey'],
            "appSecret": self.cfg['appsecret'],
            "tr_id":"HHDFC55010000",
            "custtype":"P",
            }
        params = {
            "SRS_CD": SRS_CD,
        }
        res = requests.get(URL, headers=headers, params=params)
        output1 = res.json()['output1']
        outdict = {
            "proc_date": output1['proc_date'],
            "proc_time": output1['proc_time'],
            "last_price": output1['last_price'],
            "bid_qntt": output1['bid_qntt'],
            "bid_price": output1['bid_price'],
            "ask_qntt": output1['ask_qntt'],
            "ask_price": output1['ask_price'],
        }
        return outdict