# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Kodi Help Addon by coldkeys
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: coldkeys
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.kodihelp'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "hmemar22"
YOUTUBE_CHANNEL_ID_2 = "UCoMOQDEEBECQ81CdojuEqfg"
YOUTUBE_CHANNEL_ID_3 = "JoeNobody010101"
YOUTUBE_CHANNEL_ID_4 = "UCuSdObYHdjize3ziP951org"
YOUTUBE_CHANNEL_ID_5 = "pctech9990"
YOUTUBE_CHANNEL_ID_6 = "XBMChelpguide"
YOUTUBE_CHANNEL_ID_7 = "dawild1504"
YOUTUBE_CHANNEL_ID_8 = "XBMCHELPER"
YOUTUBE_CHANNEL_ID_9 = "xbmconnect"
YOUTUBE_CHANNEL_ID_10 = "nareshkeswani80"

# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Husham Memar",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://forum.husham.com/download/file.php?avatar=48_1441275835.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tech Timeruuu",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-xrpSGZutUms/AAAAAAAAAAI/AAAAAAAAAAA/WoCkFC1pt8Q/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JoeNobody010101",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-yyi7bfBAFdM/AAAAAAAAAAI/AAAAAAAAAAA/YZtjGJ9XsYo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Solo Man",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-YUHW44PfRLU/AAAAAAAAAAI/AAAAAAAAAAA/TMK9xizbGJU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SpoonFed Productions",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-AEmubMpBV6I/AAAAAAAAAAI/AAAAAAAAAAA/bzycEE8Y5qA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="XBMC - KODI Help",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-6mLNnnG4sKE/AAAAAAAAAAI/AAAAAAAAAAA/78_ra-ZQpnI/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="SUPA CHARGEDiOS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-Se4DrSNofmU/AAAAAAAAAAI/AAAAAAAAAAA/KWZhJotP3d0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="OneTechGenius XBMC HELPER",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-gz5CkSVvQW0/AAAAAAAAAAI/AAAAAAAAAAA/5tL5WmC4U4w/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="XBMConnect",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-op-ozll4OWI/AAAAAAAAAAI/AAAAAAAAAAA/Hoq_od6Z9MY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="naresh lal",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-Kb9zJh_02NI/AAAAAAAAAAI/AAAAAAAAAAA/QuwbM3wc9vI/s100-c-k-no/photo.jpg",
        folder=True )
run()
