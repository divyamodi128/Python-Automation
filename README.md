# Python-Automation

FUNCTIONS

    appThreads(app)
        Function used for creating threads
        Eg. threading.Thread(target=appThreads, args=(app,))

    openAllApps(apps)
        Creates the thread for each applications passed in apps.

        Inputs:
            apps: list of paths

    openUpUrls(urls, browser=None, mode=None)
        Opening bunch of urls in Google-chrome OR Firefox.

        Inputs:
            urls: list of urls
            browser: firefox, chrome (default is chrome)
            mode: private for firefox and incognito for chrome (default mode is normal)

    openUrl(url, browser=None)
        Just opening a particular urls and exit immediately.
        Eg. www.netflix.com

Declare all the desired applications based on your OS.

For MacOS:

    "CHROME": "open -a /Applications/Google\ Chrome.app %s"

For Windows:

    "CHROME": "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s",

For Linux/Ubuntu:

    "CHROME": "/usr/bin/google-chrome %s"

List your Applications in `Dynamics/dynamicslist.json`.

    "Applications": {
        "CHROME": "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s",
        "INCOGNITO_CHROME": "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito",
        "FIREFOX": "C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s",
        "Others": [
            "C:/Program Files (x86)/Microsoft VS Code/Code.exe",
            "C:/Program Files/Git/git-bash.exe",
            ...
        ]
    }

For all your tabs specify them respectively or just leave it blank

    "Chrome": [
        "mail.google.com",
        "www.facebook.com"
    ],
    "Chrome-inco": [],
    "Firefox": [
        "mail.google.com"
    ],
