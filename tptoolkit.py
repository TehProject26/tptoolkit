# TehProject V1.0
import re, urllib2, requests, sys, hashlib, base64, time
from socket import *
from datetime import datetime


def linkgrabber():
     url = raw_input("Whats The URL To Crawl ?: ")
     website = urllib2.urlopen(url)
     html = website.read()
     links = re.findall('"((http|ftp)s?://.*?)"', html)
     for i in links:
      print(i)

def externalip():
     url = 'http://myexternalip.com/raw'
     req = requests.get(url)
     Cip = req.text
     print ('\n' + '\033[1m' + Cip)

def hashstring():
     print('\n' + 10 * '-' + " Hashing Menu " + 10 * '-' +'\n')
     print('\033[1m' + "1. MD5 ")
     print('\033[1m' + "2. SHA1 ")
     print('\033[1m' + "3. SHA512 ")
     print('\033[1m' + 20 * '-')
     print('\033[1m' + "4. Encode Base64 ")
     print('\033[1m' + "5. Decode Base64 ")
     whichone = input('\n' + '\033[1m' + 'Enter Your Choice [1-5] : ')
     if whichone == 1:
         tohash = raw_input('\033[1m' + '\n\n'"Whats The String : ")
         hash_object = hashlib.md5(tohash)
         hex_dig = hash_object.hexdigest()
         print('\033[1m' + '\n' + hex_dig)
     elif whichone == 2:
         tohash = raw_input('\n\n'"Whats The String : ")
         hash_object = hashlib.sha1(tohash)
         hex_dig = hash_object.hexdigest()
         print('\n' + hex_dig)
     elif whichone == 3:
         tohash = raw_input('\n\n'"Whats The String : ")
         hash_object = hashlib.sha512(tohash)
         hex_dig = hash_object.hexdigest()
         print('\n' + hex_dig)
     elif whichone == 4:
         toencode = raw_input('\033[1m' + '\n\n'"Whats The String : ")
         encode = base64.b64encode(toencode)
         print('\033[1m' + '\n' + encode)
     elif whichone == 5:
         todecode = raw_input('\033[1m' + '\n\n'"Whats The String : ")
         decode = base64.b64decode(todecode)
         print('\033[1m' + '\n' + decode)
     else:
         print('\033[1m' + "invaild")

def portscanner():

    if __name__ == '__main__':
     target = raw_input('\n' + "Enter host to scan: ")
     targetIP = gethostbyname(target)
     print('\n' + "Starting scan on host " + targetIP  + '\n\n')
     for i in range(1, 5000):
        sock= socket(AF_INET, SOCK_STREAM)
        result = sock.connect_ex((targetIP, i))
        if(result == 0) :
            print 'Port %d: OPEN' % (i,)
        sock.close()

def proxylist():
     website = urllib2.urlopen('http://tehproject26.x10host.com/proxylist')
     output = website.read()
     print(output)

def emaildump():
     website = urllib2.urlopen('http://tehproject26.x10host.com/emaildump')
     output = website.read()
     print(output)

def mainmenu():
      print ('\033[1m' + 30 * '-')
      print ('\033[1m' + "   M A I N - M E N U")
      print ('\033[1m' + 30 * '-')
      print ('\033[1m' + "1. Link Grabber ")
      print ('\033[1m' + "2. External IP ")
      print ('\033[1m' + "3. Hashing Tool")
      print ('\033[1m' + "4. Port Scanner")
      print ('\033[1m' + "5. Proxy List")
      print ('\033[1m' + "6. Email Dump List")
      print ('\033[1m' + "7. About ")
      print ('\n' + '\033[1m' + "8. Exit Tool Kit" )
      print ('\033[1m' + 30 * '-')

      choice = raw_input('\033[1m' + 'Enter your choice [1-8] : ')
      choice = int(choice)

      if choice == 1:
         linkgrabber()
      elif choice == 2:
           externalip()
      elif choice == 3:
           hashstring()
      elif choice == 4:
           portscanner()
      elif choice == 5:
           proxylist()
      elif choice == 6:
           emaildump()
      elif choice == 7:
           print('\n\n' + 19 * '#' + '\n' + "#  TP's Tool Kit  #" + '\n'+ "#  Version 1.0    #" + '\n' + 19 * '#' + '\n\n')
      elif choice == 8:
          print('\n\n' + "Thank You For Using TP's Tool Box." + '\n')
          sys.exit()
      else:
         print ("Invalid number. Try again...")





mainmenu()
