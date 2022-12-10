# Author: Fazle Rabbi
# Date: 10 Dec,2022
# https://github.com/fh-rabbi
# Don't change my credit!
# Changing credit dont made you a coder!

import os,json,requests,time

# Colors
bg_red = '\033[1;41m'
bg_blue = '\033[1;44m'
text_red = '\033[1;91m'
text_green = '\033[1;92m'
text_yellow = '\033[1;93m'
text_blue = '\033[1;94m'
text_purple = '\033[1;95m'
text_white = '\033[1;97m'

def clear():
   os.system('clear')

# Banner
def banner():
   print(f"""{text_white}
------------------------------------------
##########################################
## {text_red}░█▀▄▀█ █▀▀█ █▀▀ █─█ ── ░█─░█ █▀▀█ █── ##
## {text_green}░█░█░█ █▄▄█ ▀▀█ █▀▄ ▀▀ ░█─░█ █▄▄▀ █── ##
## {text_purple}░█──░█ ▀──▀ ▀▀▀ ▀─▀ ── ─▀▄▄▀ ▀─▀▀ ▀▀▀ ##
{text_white}##########################################
------------------------------------------

{text_white}>> {text_green}Coded By Fazle Rabbi
{text_white}>> {text_yellow}https://github.com/fh-rabbi
{text_white}>> {text_blue}Hide Your Phising Url !
   """)

# Main Menu
def menu():
   URL = input(f"{text_white}[*] {text_purple}Enter Your Url:{text_white}")
   if len(URL) == 0:
      print(f'{text_red}[!] Please enter a valid url')
      time.sleep(1)
      clear()
      # time.sleep(1)
      banner()
      menu()
      return
   wear_mask(URL)
   
# Main Logic To Mask An Url
def wear_mask(URL):
   try:
      res = requests.get(f'https://is.gd/create.php?format=simple&url={URL}')
      # print(res.status_code)
      if res.status_code == 400:
         print(f'{text_red}[!] Please enter a valid url')
         time.sleep(1)
         clear()
         # time.sleep(1)
         banner()
         menu()
         return
      else:
         new_url = res.text
         index = new_url.index('/')
         protocol = new_url[0:index+2]
         main_part = new_url[index+2:]
         mask_domain = input(f"{text_white}[*] {text_purple}Enter a domain (Ex:google.com):{text_white}")
         social_word = input(f"{text_white}[*] {text_purple}Enter social engineering word {text_red} Do not use space between two or more words just use [-] {text_purple}(Ex:earn-money,funney-video):{text_white}")
         mask_url = protocol+mask_domain+'-'+social_word+'@'+main_part
         print(f'{text_white}[*] {text_green}Generating mask-url...')
         time.sleep(2)
         print(f'{text_white}[*] {text_red}Your Mask Url is:{text_yellow}')
         print(mask_url)
         opt = input(f"{text_white}[*] {text_green}Press any key for mask another url:")
         print(opt)
         if opt or opt == '':
            clear()
            banner()
            menu()
   except:
      print(f'{text_red}[!] Please enter a valid url or Check your internet connection!')
      time.sleep(3)
      clear()
      # time.sleep(1)
      banner()
      menu()
      return


banner()
menu()
