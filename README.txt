Steps for geckodriver installation:

1)Geckodriver links :https://github.com/mozilla/geckodriver/releases
2)Download the geckodriver
3)Extract the files
4)Copy in the Scripts where Python is installed, incase of venv, just copy the "geckodriver.exe" to the Scripts


Common errors :

1)selenium.common.exceptions.SessionNotCreatedException: Message: Unable to find a matching set of capabilities
Solutions : Version with the browser, or the browser is not installed

2)Issue with PATH:
Solution : Download the geckodriver from the above mentioned link and then copy it to the location mentioned above

requirements.txt has all the set of installed libraries