#! C:/Program Files (x86)/Python36-32/python.exe
import webbrowser
import subprocess
import threading
import json
import time

"""
MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

Windows
chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

Linux
chrome_path = '/usr/bin/google-chrome %s'
"""


def openUrl(url, browser=None):
    '''
    Just opening a particular urls and exit immediately. 
    Eg. www.netflix.com
    '''
    if browser:
        webbrowser.get(CHROME).open_new_tab(url)
    exit()

# def openWorkTerminal(cmds):
#     # Working with Teminal or Command Prompt.
#     all_cmds = [
#         'start', 'cmd', '/k'
#     ]
#     [all_cmds.append(cmd) for cmd in cmds]
#     print(all_cmds)
#     p = subprocess.call(all_cmds, stderr=subprocess.PIPE, shell=True)

def openUpUrls(urls, browser=None, mode=None):
    '''Opening bunch of urls in Google-chrome OR Firefox.

    Inputs:
        urls: list of urls
        browser: firefox, chrome (default is chrome)
        mode: private for firefox and incognito for chrome (default mode is normal)
    '''
    if browser == 'firefox':
        if mode == 'private':
            browse_instance = webbrowser.get(INCOGNITO_FIREFOX)
        else:
            browse_instance = webbrowser.get(FIREFOX)
    else:
        if mode == 'incognito':
            browse_instance = webbrowser.get(INCOGNITO_CHROME)
        else:
            browse_instance = webbrowser.get(CHROME)
    for url in urls:
        browse_instance.open_new_tab(url)
        print("Opened URL:", url)

def appThreads(app):
    '''Function used for creating threads
    Eg. threading.Thread(target=appThreads, args=(app,))
    '''
    print("Open:", app)
    subprocess.Popen(app)
    # time.sleep(60)

def openAllApps(apps):
    '''Creates the thread for each applications passed in apps.
    
    Inputs:
        apps: list of paths
    '''
    for app in apps:
        print("Opening Apps:", app)
        threading.Thread(target=appThreads, args=(app,)).start()


if __name__ == '__main__':
    choices = input("Netflix default is N (Y/N) :")
    with open('Dynamics/dynamicslist.json', 'r') as urlLists:
        allurls = json.load(urlLists)
    from pprint import pprint
    pprint(allurls)
    try:
        webbrowser.get(allurls["Applications"]["CHROME"])
        webbrowser.get(allurls["Applications"]["FIREFOX"])
    except Exception:
        print("Invalid browser paths")
        input()
    
    CHROME = allurls["Applications"]["CHROME"]
    INCOGNITO_CHROME = allurls["Applications"]["INCOGNITO_CHROME"]
    FIREFOX = allurls["Applications"]["FIREFOX"]
    INCOGNITO_FIREFOX = allurls["Applications"]["INCOGNITO_FIREFOX"]

    if choices.lower().startswith('y'):
        openUrl(allurls['SingleUrl'], browser=allurls["Applications"]["CHROME"])

    print("\nStarting browser threads")
    if allurls.get('Chrome'):
        chrome_thread = threading.Thread(name='ChromeThread', target=appThreads, args=(CHROME,))
        chrome_thread.start()
    if allurls.get('Firefox'):
        firefox_thread = threading.Thread(name='FirefoxThread', target=appThreads, args=(FIREFOX[:-3],))
        firefox_thread.start()
    if allurls.get('Chrome-inco'):
        incognito_thread = threading.Thread(name='IncoThread', target=appThreads, args=(INCOGNITO_CHROME))
        incognito_thread.start()
    if allurls.get('Firefox-private'):
        private_thread = threading.Thread(name='PrivateThread', target=appThreads, args=(INCOGNITO_CHROME))
        private_thread.start()
    
    # All the other applications are opened here.
    print("\nMeanwhile opening all other applications in threads")
    openAllApps(allurls['Applications']['Others'])

    print("Waitng for threads")
    threadlist = threading.enumerate()
    print("All Threads:", threadlist)

    if 'ChromeThread' in threadlist:
        chrome_thread.join()
    if 'FirefoxThread' in threadlist:
        firefox_thread.join()
    if 'IncoThread' in threadlist:
        incognito_thread.join()
    if 'PrivateThread' in threadlist:
        private_thread.join()
    print("All threads joined and completed")

    openUpUrls(allurls['Chrome'])
    openUpUrls(allurls['Firefox'], browser='firefox')
    openUpUrls(allurls['Chrome-inco'], mode='incognito')

    # Opening up the terminal for work
    # cmds = [
    #     'python', 'OpenNewTerminal.py'
    # ]
    # openWorkTerminal(cmds)



# import subprocess

# p0 = subprocess.Popen(['start', 'cmd', '/k'], stdout=subprocess.PIPE, shell=True)
# cmds1 = ['echo', 'Hello World']
# p1 = subprocess.Popen(cmds1, stdout=subprocess.PIPE, shell=True)
# cmds2 = ['grep', '-i', '-o', "'Hello'"]
# p2 = subprocess.Popen(cmds2, stdin=p1.stdout, stdout=sunprocess.PIPE, shell=True)
