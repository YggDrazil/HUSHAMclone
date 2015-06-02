#Youtube channels
#
#
#
#
#
#Husham with Ryan reggae n dancehall music Addon
import re
import os
import sys
import urllib2
import buggalo
import xbmcgui
import xbmcaddon
import xbmcplugin

BASE_URL = 'http://iwaztv.com/?p=51'
PLAY_VIDEO_PATH = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
PLAYLIST_PATH = 'plugin://plugin.video.youtube/user/AkamEntertainments/'

if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    HANDLE = int(sys.argv[1])

    try:
        u = urllib2.urlopen(BASE_URL)
        html = u.read()
        u.close()


        m = re.search('//www.youtube.com/embed/([^"]+)"', html, re.DOTALL)
        if m:
            item = xbmcgui.ListItem('Reggae n Dancehall music',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-wQ8woE0PkAM/AAAAAAAAAAI/AAAAAAAAAAA/V5jh5XF6NBQ/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH, item, True)
            		
        xbmcplugin.endOfDirectory(HANDLE)
    except:
        buggalo.onExceptionRaised()
