import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input('Enter a URL:') # προσδιορισμός του url
if not url.startswith("http://"):
    url = "http://" + url

with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #more(html)

    print(f"Website headers are {url} \n , {response.headers} \n\n")

    server = response.headers.get('Server')

    if server:
        print(f"The server is {server}")
    else:
        print("No server found")
    
    cookies = response.cookies.get_dict()

    print(cookies)
    cookie_header = response.headers.get('Set-cookie')

    if cookie_header:
        print(f"The cookie is{cookie_header}")
    else:
        print("This website does not use cookies.")

