FILE_NAME = input("FILE -> ")
CURL_CMD = input("cURL -> ").replace("'",'').split("curl ")[1].split("-H")

URL = CURL_CMD.pop(0)
LAST_HEADER = CURL_CMD[len(CURL_CMD)-1]

output = open(FILE_NAME, 'w')
output.write("""import requests

HEADERS = {
""")

for i in CURL_CMD:
    HEADER = i[1:].split(': ')
    KEY = HEADER[0]
    VALUE = HEADER[1]
    if i != LAST_HEADER:
        output.write(f"    '{KEY}': '{VALUE}',\n")
    else:
        output.write(f"    '{KEY}': '{VALUE}'\n")

output.write("}\n" + f"res = requests.get(\n    url = '{URL[:-1]}',\n    headers = HEADERS\n)")

print("SUCCESS !")
