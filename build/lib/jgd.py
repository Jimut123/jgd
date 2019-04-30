"""
JGD: Jimut's GIT Downloader is a Copyrighted scraper program to download/ clone a git repo/ folder.
Author: Jimut Bahan Pal (jimutbahanpal@yahoo.com)
python jgd.py <any-git-folder-url>
python jgd.py <any-git-repo-url>

It is pretty niggerlicious way to clone a folder/repo, since you need to reclone this again, if they update it.
Thank me and remember me, since this doesn't use AUTH/TOKEN! and downloads files of long and big repo present out there.
"""

import urllib.request, urllib.parse, urllib.error
from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path
from tqdm import tqdm
import argparse
import sqlite3
import time
import json
import wget
import ssl
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str,
                    help='URL is mandatory!\n Please provide URL to folder/repo of Public repository.')
    args = parser.parse_args()
    print(args.url)

    conn = sqlite3.connect('git.sqlite')
    cur = conn.cursor()

    cur.executescript('''
    CREATE TABLE IF NOT EXISTS data (
        url   TEXT UNIQUE PRIMARY KEY,
        type TEXT,
        parent TEXT,
        traversed INTEGER
    );
    ''')

    url = str(args.url)
    LENGTH = len(url)
    while True:
        ol_url = url
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0")
        driver = webdriver.Firefox(profile)
        driver.get(url)
        get_file_names = []
        get_file_names_f = []
        get_file_names = driver.find_elements_by_class_name("js-navigation-open")
        
        for items in get_file_names:
            
            #item_ = items.text 
            href_ = items.get_attribute('href')
            if len(href_)<LENGTH:
                continue
            try:
                split_1,split_2 = str(href_).split('/')[5], str(href_).split('/')[6]
                if split_1 == "tree":
                    print("folder =>",href_)
                    cur.execute('''INSERT OR IGNORE INTO data (url, type, parent, traversed)
                        VALUES ( ?, ?, ?, ? )''', (href_,"folder",url,0 ) )
                if split_1 == "blob":
                    s = href_.split('/')
                    get_url = s[0]+"//"+"raw.githubusercontent.com/"+s[3]+"/"+s[4]+"/"+s[6]+"/"+s[7]
                    print("file =>",href_)
                    cur.execute('''INSERT OR IGNORE INTO data (url, type, parent, traversed)
                        VALUES ( ?, ?, ?, ? )''', (href_,"file",url,1 ) )
            except:
                print()
        driver.close()

        urls = cur.execute('''SELECT * FROM data WHERE traversed = ?''',(0,)).fetchall()
        if not urls:
            print("NO URL PRESENT")
            break
        for k in urls:
            url = k[0]
            print("----------------------------- k[0] ==",url)
            #print(k[1],k[2],k[3])
            print("URL ==",url)
            cur.execute('''UPDATE data SET traversed = ? WHERE url = ?''',(1,url,))
            conn.commit()
            break
        print("NOT TRAVERSED : ")
        urls = cur.execute('''SELECT * FROM data WHERE traversed = ?''',(0,)).fetchall()
        if not urls:
            print("NO URL PRESENT")
            break
        if ol_url == url:
            print("EXITING")
            break
        for j in urls:
            print(j)
    conn.commit()
    cur.close()

    conn = sqlite3.connect('git.sqlite')
    cur = conn.cursor()

    data = cur.execute('''SELECT * FROM data''')

    final_json = {}

    for item in data:
        fin_item = item[0]
        split_it = fin_item.split('/')
        #print(fin_item)
        root_folder_1 = split_it[4]
        all_item = split_it[7:]
        all_item_3 = ''
        all_item_3 = '/'.join(all_item)
        #print()
        folder = root_folder_1+'/'+all_item_3

        s = item[0].split('/')
        if s[5] == 'blob':
            get_url = s[0]+"//"+"raw.githubusercontent.com/"+s[3]+"/"+s[4]+"/"+'/'.join(s[6:])
        else:
            get_url = ''
        final_json[folder] = get_url

    print(json.dumps(final_json, indent=2, sort_keys=True))

    cur_wd = os.getcwd()
    data = final_json

    for item in data:
        #print(item)
        if data[item] != '':
            dir_ = item.split('/')[:-1]
            go_dir = '/'.join(dir_)
            link_ = data[item]
            #print(go_dir,link_)
            if not os.path.exists(go_dir):
                os.makedirs(go_dir)
            os.chdir(go_dir)
            wget.download(link_)
            os.chdir(cur_wd)
    os.remove("git.sqlite")
    os.remove("geckodriver.log")
    print("\nCLEANING!")


if __name__ == "__main__":
    main()