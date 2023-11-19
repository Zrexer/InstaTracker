#!/usr/bin/env python3
"""
[+] Instagram Tracker [+]

_< Use to get Information About Wich Account in Instagram >_

DEV#Host1let => R3D\|/R00m


License :

Copyright (c) 2023 R3D\|/R00m Host1let: instatracker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__version__ = '0.0.2'

import requests
import pystyle

class Banner:

    text1 = """----[+] Instagram Tracker [+]----"""
    text2 = """_< Use to get Information About Wich Account in Instagram >_"""
    text3 = """----{ DEV#Host1let => R3D\|/R00m }---"""



    b = """
 ___             __         _______                 __
|   .-----.-----|  |_.---.-|       .----.---.-.----|  |--.-----.----.
|.  |     |__ --|   _|  _  |.|   | |   _|  _  |  __|    <|  -__|   _|
|.  |__|__|_____|____|___._`-|.  |-|__| |___._|____|__|__|_____|__|
|:  |                        |:  |
|::.|                        |::.|
`---'                        `---'

"""

    def bx():
        pystyle.Write.Print(f"{Banner.b}\n               ", pystyle.Colors.purple_to_red, 0)
        print()
        pystyle.Write.Print("               "+Banner.text1, pystyle.Colors.green_to_yellow, 0.01)
        print()
        pystyle.Write.Print("               "+Banner.text2, pystyle.Colors.green_to_yellow, 0.01)
        print()
        pystyle.Write.Print("               "+Banner.text3, pystyle.Colors.green_to_yellow, 0.01)
        print()
        print()
        print()
        print()


class Tracker:

    def start(username: str):
        if username.startswith('@'):
            username = username.replace('@', '')

        pystyle.Write.Print("{:<20} {:<}".format("Header", "Status"), pystyle.Colors.yellow_to_red, 0.01)
        print()
        pystyle.Write.Print("-"*30, pystyle.Colors.yellow_to_red, 0)
        print()
        print()


        try:
            reqINFO = dict(requests.get(f'https://api2.haji-api.ir/instainfo/?text={username}').json()).get('result')[0]
        except Exception as EREQ:
            return EREQ
            
        for k, v in reqINFO.items():
            pystyle.Write.Print('{:<30} {:<}'.format(str(k), str(v)), pystyle.Colors.yellow_to_red, 0)
            print()

class Help:
    
    def usage():
        pystyle.Write.Print('{:<30} {:<}'.format("Command", 'Usage'), pystyle.Colors.green_to_yellow, 0.01)
        print()
        pystyle.Write.Print("-"*30, pystyle.Colors.green_to_yellow, 0)
        print()
        pystyle.Write.Print('{:<30} {:<}'.format('help', 'show this message'), pystyle.Colors.green_to_yellow, 0)
        print()
        pystyle.Write.Print('{:<30} {:<}'.format('track', 'Start Tracking: track ali || track @ali [you can use @ or not]'), pystyle.Colors.green_to_yellow, 0)
        print()
        pystyle.Write.Print("\nMore About Track: if you want to save results, just use this: [ track ali / @ali -s / --save :[you can set name for that after -s or --save command:[optional]]]", pystyle.Colors.purple_to_red, 0)
        print()

class MainACT:
    def Main():
        Banner.bx()
        
        while 1:
            u = pystyle.Write.Print("\nInstaTracker > ", pystyle.Colors.orange, 0)
            user = input("")
            text = user.split()
            
            if "help" in text:
                Help.usage()
                
            if "track" in text:
                if not "-s" in text or "--save" in text:
                    user = text[text.index('track')+1]
                    Tracker.start(user)
                    
                else:
                    if "-s" in text:
                        if "-s" == text[-1]:
                            with open('resultsTracker.txt', 'a') as ss:
                                user = text[text.index('track')+1]
                                res = Tracker.start(user)
                                ss.write(res)
                                ss.close()
                                
                            pystyle.Write.Print('File Saved in resultsTracker.txt', pystyle.Colors.purple_to_red, 0.01)
                            print()
                    
                        else:
                            sn = open(text[text.index('-s')+1], 'a')
                            user = text[text.index('track')+1]
                            res = Tracker.start(user)
                            sn.write(res)
                            sn.close()
                            pystyle.Write.Print(f'File Saved in {text[text.index("-s")+1]}', pystyle.Colors.purple_to_red, 0.01)
                            print()
            
                    elif "--save" in text:
                        if "--save" == text[-1]:
                            with open('resultsTracker.txt', 'a') as ss:
                                user = text[text.index('track')+1]
                                res = Tracker.start(user)
                                ss.write(res)
                                ss.close()
                                
                            pystyle.Write.Print('File Saved in resultsTracker.txt', pystyle.Colors.purple_to_red, 0.01)
                            print()
                    
                        else:
                            sn = open(text[text.index('--save')+1], 'a')
                            user = text[text.index('track')+1]
                            res = Tracker.start(user)
                            sn.write(res)
                            sn.close()
                            pystyle.Write.Print(f'File Saved in {text[text.index("--save")+1]}', pystyle.Colors.purple_to_red, 0.01)
                            print()
        
MainACT.Main()
