username = None
password = None


def getHasGUI():
    # return True
    return False


def getDriverPath():
    # return '/usr/local/bin/msedgedriver'
    return 'C:\\F-Env\\14-edgeDriver\\msedgedriver.exe'


def setUserInfo(un, pw):
    global username, password
    username = un
    password = pw


def getUserInfo():
    return username, password


