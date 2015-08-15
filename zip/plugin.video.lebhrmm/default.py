#Youtube channels
#
#
#
#
#
#Hisham Marzouk
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
PLAYLIST_PATH = 'plugin://plugin.video.youtube/channel/UCnkTo_wMqGtLiA4xX7roORg/'
PLAYLIST_PATH2 = 'plugin://plugin.video.youtube/channel/UC5f_fxJa5G9AR9L3J5Z2I4A/'
PLAYLIST_PATH3 = 'plugin://plugin.video.youtube/channel/UC2eG5fa3N4I3yFLepNoXaMw/'
PLAYLIST_PATH4 = 'plugin://plugin.video.youtube/channel/UC9_XmAwE5szLHF76FjMylaw/'
PLAYLIST_PATH5 = 'plugin://plugin.video.youtube/channel/UC4JCsTLFcHGk10qpiNMh0Ww/'
PLAYLIST_PATH6 = 'plugin://plugin.video.youtube/channel/UCBrIvQGxLdxfpeAKXy5wALA/'
PLAYLIST_PATH7 = 'plugin://plugin.video.youtube/channel/UCGaOCoe5XaJJKNEKWM1WpJQ/'
PLAYLIST_PATH8 = 'plugin://plugin.video.youtube/channel/UCh8BdTka1DRnu4uHrEB-EaA/'
PLAYLIST_PATH9 = 'plugin://plugin.video.youtube/channel/UCpE6gpKewomi17XDyPfpFjA/'
PLAYLIST_PATH10 = 'plugin://plugin.video.youtube/channel/UCJu-0vnWt0wFMQuLsjzwjRQ/'
PLAYLIST_PATH11 = 'plugin://plugin.video.youtube/channel/UCWtY7mckeLR__j-Jqcdkv4g/'
PLAYLIST_PATH12 = 'plugin://plugin.video.youtube/channel/UCfiwzLy-8yKzIbsmZTzxDgw/'
PLAYLIST_PATH13 = 'plugin://plugin.video.youtube/channel/UCHAbNxkU837UAkZ-OPtdUUw/'
PLAYLIST_PATH14 = 'plugin://plugin.video.youtube/channel/UC65zwKz2W3NvfAkt5pGs18w/'
PLAYLIST_PATH15 = 'plugin://plugin.video.youtube/channel/UCM96e_r6hk9tRT0X_McU9pQ/'
PLAYLIST_PATH16 = 'plugin://plugin.video.youtube/channel/UCcbAo_QpfV0Zf1aYrnPVFdQ/'

if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    HANDLE = int(sys.argv[1])

    try:
        u = urllib2.urlopen(BASE_URL)
        html = u.read()
        u.close()


        m = re.search('//www.youtube.com/embed/([^"]+)"', html, re.DOTALL)
        if m:
            item = xbmcgui.ListItem('MTV LEBANON',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-1o9XNmB6a9c/AAAAAAAAAAI/AAAAAAAAAAA/jKUrvHVFEfA/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH, item, True)
            item = xbmcgui.ListItem('MTV LEBANON NEWS',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://i.ytimg.com/i/9_XmAwE5szLHF76FjMylaw/mq1.jpg?v=51546248')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH4, item, True)
            item = xbmcgui.ListItem('AL JADEED',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-RG-QdhFCAA0/AAAAAAAAAAI/AAAAAAAAAAA/plXq_661M_0/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH2, item, True)
            item = xbmcgui.ListItem('AL JADEED NEWS',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-RG-QdhFCAA0/AAAAAAAAAAI/AAAAAAAAAAA/plXq_661M_0/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH5, item, True)
            item = xbmcgui.ListItem('FutureTV Society & Lifestyle',ADDON.getLocalizedString(30001),
                                   iconImage='https://yt3.ggpht.com/-C7Cx2d7I2XY/AAAAAAAAAAI/AAAAAAAAAAA/fyr4U5GI1Ow/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH6, item, True)
            item = xbmcgui.ListItem('FutureTV News',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-mMY5tb3eymc/AAAAAAAAAAI/AAAAAAAAAAA/E6SYDQa6_kQ/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH7, item, True)
            item = xbmcgui.ListItem('AlManar Channel',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-ojE_FF95vLA/AAAAAAAAAAI/AAAAAAAAAAA/CfBgDYEVqK4/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH8, item, True)
            item = xbmcgui.ListItem('lbcgroup',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-Dy0fH96YvF8/AAAAAAAAAAI/AAAAAAAAAAA/JP5W8z4Ft1U/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH9, item, True)
            item = xbmcgui.ListItem('OTV Lebanon',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-m0pQvf5oAic/AAAAAAAAAAI/AAAAAAAAAAA/DT-Po4j1q1g/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH10, item, True)
            item = xbmcgui.ListItem('Mafi Metlo',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-P1yW3OfbFw8/AAAAAAAAAAI/AAAAAAAAAAA/L0-n9P9QRxE/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH11, item, True)
            item = xbmcgui.ListItem('Al Jazeera Arabic',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-c3pNXYa0Q7Q/AAAAAAAAAAI/AAAAAAAAAAA/_ccpfp5MaAs/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH12, item, True)
            item = xbmcgui.ListItem('Toyour Baby',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-QAB6Yjm9KrI/AAAAAAAAAAI/AAAAAAAAAAA/zaGYJpwhpZQ/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH13, item, True)
            item = xbmcgui.ListItem('Classical Arabic Music',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-nNoS5BFPsPU/AAAAAAAAAAI/AAAAAAAAAAA/Q9UYS-ACuVc/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH14, item, True)
            item = xbmcgui.ListItem('Rotana Mousica',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-iSvEN0c91Lo/AAAAAAAAAAI/AAAAAAAAAAA/9BfLayE1Mfk/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH15, item, True)
            item = xbmcgui.ListItem('Geo Arabic',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-IH1Kcle0oyU/AAAAAAAAAAI/AAAAAAAAAAA/GegRRTep6YU/s100-c-k-no/photo.jpg')
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH16, item, True)
            
            item = xbmcgui.ListItem('HISHAM MARZOUK',
                                    ADDON.getLocalizedString(30001),
                                    iconImage='https://yt3.ggpht.com/-hJVRdFTzvSE/AAAAAAAAAAI/AAAAAAAAAAA/-iBBhqPAy_4/s100-c-k-no/photo.jpg' )
            xbmcplugin.addDirectoryItem(HANDLE, PLAYLIST_PATH3, item, True)
        xbmcplugin.endOfDirectory(HANDLE)
    except:
        buggalo.onExceptionRaised()
