<h1 align="center">cURL converter </h1>

**From :**
```bash
curl 'https://www.amazon.com/' 
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0' 
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' 
-H 'Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3' 
-H 'Accept-Encoding: gzip, deflate, br' 
-H 'DNT: 1' 
-H 'Connection: keep-alive' 
-H 'Upgrade-Insecure-Requests: 1' 
-H 'Sec-Fetch-Dest: document' 
-H 'Sec-Fetch-Mode: navigate' 
-H 'Sec-Fetch-Site: cross-site' 
-H 'Pragma: no-cache' 
-H 'Cache-Control: no-cache' 
-H 'TE: trailers'
```

**To :**
```python
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0 ',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8 ',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3 ',
    'Accept-Encoding': 'gzip, deflate, br ',
    'DNT': '1 ',
    'Connection': 'keep-alive ',
    'Upgrade-Insecure-Requests': '1 ',
    'Sec-Fetch-Dest': 'document ',
    'Sec-Fetch-Mode': 'navigate ',
    'Sec-Fetch-Site': 'cross-site ',
    'Pragma': 'no-cache ',
    'Cache-Control': 'no-cache ',
    'TE': 'trailers'
}
res = requests.get(
    url = 'https://www.amazon.com/',
    headers = HEADERS
)
```

### Usage:

- Run `main.py`
- Enter `output.py` ( your file )
- Enter your `cURL command` 