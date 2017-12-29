import subprocess
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmc

doacao = "https://www.paypal.me/SECRETTV"
site = "http://vip.amerikanotuga.tech/HomeVip/"
faceebok = "https://www.facebook.com/groups/vipsecret2017/"

def report():
    osWin = xbmc.getCondVisibility('system.platform.windows')
    osOsx = xbmc.getCondVisibility('system.platform.osx')
    osLinux = xbmc.getCondVisibility('system.platform.linux')
    osAndroid = xbmc.getCondVisibility('system.platform.linux')

    if osWin:
         subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",""+doacao+""])
    if  osAndroid:
        cmd = 'StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,,'+doacao+')'
        xbmc.executebuiltin(cmd)
    if  osLinux:
       subprocess.call(["/usr/bin/google-chrome",""+doacao+""])
    if osOsx:
        r = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",""+doacao+""])


def credit():
    osWin = xbmc.getCondVisibility('system.platform.windows')
    osOsx = xbmc.getCondVisibility('system.platform.osx')
    osLinux = xbmc.getCondVisibility('system.platform.linux')
    osAndroid = xbmc.getCondVisibility('system.platform.linux')

    if osWin:
         subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",""+site+""])
    if  osAndroid:
        cmd = 'StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,,'+site+')'
        xbmc.executebuiltin(cmd)
    if  osLinux:
       subprocess.call(["/usr/bin/google-chrome",""+credit+""])
    if osOsx:
        r = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",""+site+""])
       

def face():
    osWin = xbmc.getCondVisibility('system.platform.windows')
    osOsx = xbmc.getCondVisibility('system.platform.osx')
    osLinux = xbmc.getCondVisibility('system.platform.linux')
    osAndroid = xbmc.getCondVisibility('system.platform.linux')

    if osWin:
         subprocess.call(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",""+faceebok+""])
    if  osAndroid:
        cmd = 'StartAndroidActivity(com.android.chrome,android.intent.action.VIEW,,'+faceebok+')'
        xbmc.executebuiltin(cmd)
    if  osLinux:
       subprocess.call(["/usr/bin/google-chrome",""+faceebok+""])
    if osOsx:
        r = subprocess.call(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",""+faceebok+""])