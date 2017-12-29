import xbmcaddon, base64

Decode = base64.decodestring
MainBase = (Decode('aHR0cDovL2xpc3RzLnRoZXB5cmFtaWQuc2VlZHIuaW8vcHlyYW1pZC9ob21lLnR4dA=='))
addon = xbmcaddon.Addon('plugin.video.thepyramid')