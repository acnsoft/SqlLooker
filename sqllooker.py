import requests
from colorama import Fore
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text






banner = """

    
[[red]] (                    (                                   [[white]]  
[[red]] )\ )          (      )\ )                  )             [[white]]  
[[red]](()/(     (    )\    (()/(               ( /(     (    (  [[white]]  
[[red]] /(_))  ( )\  ((_)    /(_))   (     (    )\())   ))\   )( [[white]]  
[[red]](_))    )(( )         (_))     )\    )\  ((_)\   /((_) (()\[[white]]  
[[blue]]/ __|[[red]]  ((_)_) |_|    | |     ((_)  ((_) | |(_) (_))    ((_)[[white]]
[[blue]]\__ \  / _` | | |    | |__  / _ \ / _ \ | / /  / -_)  | '_|[[white]] 
[[blue]]|___/  \__, | |_|    |____| \___/ \___/ |_\_\  \___|  |_|  [[white]] 
 [[blue]]         |_|                                       [[white]]    

                                                         [[green]] -v1.0.2       [[white]]                               
"""

bn = colorText(banner)


print(bn)




dorkch = input("Your dork type: ")


def get_source(url):
   try:
     session = HTMLSession()
     response = session.get(url)
     return response
   except requests.exceptions.RequestException as e:
      print(e)

target = input(Fore.GREEN+"Enter your target url : ")
query = urllib.parse.quote_plus(f"{dorkch} site:{target}")
response = get_source("https://www.google.co.uk/search?q="+query)
links = list(response.html.absolute_links)
google_domains = ('https://www.google.',
 'https://google.',
 'https://webcache.googleusercontent.',
 'http://webcache.googleusercontent.',
 'https://policies.google.',
 'https://support.google.',
 'https://maps.google.',
 'https://translate.google.co.uk')
for url in links[:]:
 if url.startswith(google_domains):
  links.remove(url)
for i in links:
 print(i)
with open("result.txt","w") as f:
 for lines in links:
    f.write(lines)
    f.write("\n")
