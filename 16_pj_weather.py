import json
import requests

# get a json
res = requests.get(f'https://api.exchangeratesapi.io/latest')
res.raise_for_status()

# convert to dict
res_as_dict = json.loads(res.text)

# read out eg in this case the rate for CAD
print(res_as_dict['rates']['CAD'])
