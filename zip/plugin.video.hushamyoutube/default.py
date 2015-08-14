#Youtube channels
#
#
#
#
#
#Husham Memar
import re
import os
import sys
import urllib2
import buggalo
import xbmcgui
import xbmcaddon
import xbmcplugin

BASE_URL = 'http://www.gametest.dk/'
PLAY_VIDEO_PATH = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s'
PLAYLIST_PATH = 'plugin://plugin.video.youtube/user/hmemar22/'
PLAYLIST_PATH2 = 'plugin://plugin.video.youtube/channel/UC0XB4eRTTYxYeLMpVcIClSQ/'
PLAYLIST_PATH4 = 'plugin://plugin.video.youtube/channel/UCMF9CvIermsfS-hwrKwcFsA/'
PLAYLIST_PATH3 = 'plugin://plugin.video.youtube/channel/UCUglpFpByLwcKnbxfUlVc2g/'

if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    HANDLE = int(sys.argv[1])

    try:
        u = urllib2.urlopen(BASE_URL)
        html = u.read()
        u.close()


        m = re.search('//www.youtube.com/embed/([^"]+)"', html, re.DOTALL)
        if m:
            item = xbmcgui.ListItem('Husham Memar Guides',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://raw.githubusercontent.com/hmemar/husham.com/master/images/husham.com%20logo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH, item, True)
            item = xbmcgui.ListItem('XBMC Guides',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://raw.githubusercontent.com/hmemar/husham.com/master/images/xbmc-kodi%20help%20logo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH2, item, True)
            item = xbmcgui.ListItem('Memar Games Channel',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://raw.githubusercontent.com/hmemar/husham.com/master/images/Memear%20Games%20Channel.png')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH3, item, True)
            item = xbmcgui.ListItem('Husham Unboxing vidoes',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://raw.githubusercontent.com/hmemar/husham.com/master/images/hsuahmlogosmall.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH4, item, True)
	
        xbmcplugin.endOfDirectory(HANDLE)
    except:
        buggalo.onExceptionRaised()
