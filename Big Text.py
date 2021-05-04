import requests
print('''
  ____  _         _______        _   
 |  _ \(_)       |__   __|      | |  
 | |_) |_  __ _     | | _____  __ |_ 
 |  _ <| |/ _` |    | |/ _ \ \/ / __|
 | |_) | | (_| |    | |  __/>  <| |_ 
 |____/|_|\__, |    |_|\___/_/\_\\__|
           __/ |                     
          |___/              IG:@127.1.0.0.1

''')
user=input('enter the text:')
url = f'http://artii.herokuapp.com/make?text={user}'
req=requests.get(url).text
print(req)
print('''

i found the api from some tools uplodet py: tellegram:@filza2

''')