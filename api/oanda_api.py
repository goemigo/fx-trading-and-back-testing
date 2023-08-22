import requests
import constants.defs as defs


class OandaApi:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {defs.API_KEY}",
            "Content-Type": "application/json"
        }) 
    
    def make_request(self, url, verb='get', code=200, params=None, data=None, headers=None):
        full_url = f"{defs.OANDA_URL}/{url}"
        try:
            res = None
            if verb=='get':
                res = self.session.get(full_url,params=params,data=data,headers=headers)
            
            if res == None:
                return False, {'error':'verb not found'}
            
            if res.status_code == code:
                return True, res.json()
            else:
                return False, res.json()
        except Exception as error:
            return False, {'Exception': error}

    def get_account_endpoint(self,endpoint,data_key): #data_key is the key in res
        url=f'accounts/{defs.ACCOUNT_ID}/{endpoint}' #endpoint can be summary or instruments
        ok, data = self.make_request(url)

        if ok and data_key in data:
            return data[data_key]
        
        else:
            print('Error get_account_endpoint()', data)
            return
    
    def get_acc_summary(self):
        return self.get_account_endpoint("summary","account")
    
    def get_instruments(self):
        return self.get_account_endpoint("instruments","instruments")
