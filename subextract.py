import requests,sys

domain = sys.argv[1]
headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Iron Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Ch-Ua-Platform":"Windows",
    "Accept-Language":"en-US;q=0.8,en;q=0.7"
}

res = requests.get(f"https://api.subdomain.center/?domain={domain}",headers=headers)

data = res.json()
for n in data:
    print(n)
