import json

import requests


class HttpMethod:

    def method(self, method, url, data=None, headers=None):
        try:
            if method == "get":
                resp = requests.get(url, params=data, headers=headers)
                resp_json = resp.json()
                return resp_json
            elif method == "post":
                resp = requests.post(url, data=json.dumps(data), headers=headers)
                resp_json = resp.json()
                return resp_json
            elif method == "put":
                resp = requests.put(url, json=json.dumps(data), headers=headers)
                resp_json = resp.json()
                return resp_json
            elif method == "delete":
                resp = requests.delete(url, json=json.dumps(data), headers=headers)
                resp_json = resp.json()
                return resp_json
        except Exception as e:
            print(f'{str(e)}')
