# empireldn.com XBMC Plugin
# Developer: Android TV Boxes reworked by basscontroller
# Support: www.xbmchub.com or @bassleaks
# Disclaimer: Android TV Boxes or bass controller do not own or publish the content delivered by the plugin
# streams and content is owned by empireldn.com

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://91.121.165.88:8148/stream'
li = xbmcgui.ListItem('[COLOR red][B]EMPIRELDN.COM  [/B][/COLOR] [COLOR white][B][I](Live)[/B][/I][/COLOR]  [COLOR red][B] >>[/B][/COLOR] >>    [COLOR white](Stream 1)[/COLOR]', iconImage='http://s9.postimg.org/90nsjdd6z/Untitled.png', thumbnailImage= 'http://s9.postimg.org/90nsjdd6z/Untitled.png')
li.setProperty('fanart_image', 'http://s9.postimg.org/90nsjdd6z/Untitled.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'video')
url = 'http://91.121.165.88:8148/stream'
li = xbmcgui.ListItem('[COLOR white][B]EMPIRELDN.COM[/B][/COLOR] [COLOR red][B][I](Live)[/B][/I][/COLOR]  [COLOR white][B] >>[/B][/COLOR] >>    [COLOR red](STREAM 2)[/COLOR]', iconImage='http://s9.postimg.org/90nsjdd6z/Untitled.png', thumbnailImage= 'http://s9.postimg.org/90nsjdd6z/Untitled.png')
li.setProperty('fanart_image', 'http://s9.postimg.org/90nsjdd6z/Untitled.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://91.121.165.88:8148/stream'
li = xbmcgui.ListItem('Text:07909788404. Twitter: @EMPIRE_LDN. Empireldn.com  Internet Radio Station', iconImage='http://s9.postimg.org/90nsjdd6z/Untitled.png', thumbnailImage= 'http://s9.postimg.org/90nsjdd6z/Untitled.png')
li.setProperty('fanart_image', 'http://s9.postimg.org/90nsjdd6z/Untitled.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
xbmcplugin.endOfDirectory(addon_handle)


