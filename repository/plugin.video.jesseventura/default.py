# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Jesse Ventura Addon by coldkeys
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

addonID = 'plugin.video.jesseventura'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "JesseVenturaChannel"
YOUTUBE_CHANNEL_ID_2 = "VenturaOffGrid"
YOUTUBE_CHANNEL_ID_3 = "PL-PGk0xTdoUJDeXLkr7EEsvwjEFc79A0H"
YOUTUBE_CHANNEL_ID_4 = "PL3DA87XCdlgxW5MMcnS9irZB2UWVRvbH0"

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
        title="JesseVenturaChannel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.ytimg.com/i/le0Wj0sQPJF4MeJeZKQQmw/mq1.jpg?v=b54f41",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jesse Ventura Off The Grid",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-xA9bGVn0C78/AAAAAAAAAAI/AAAAAAAAAAA/4g6_j2bctyg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Off The Grid with Jesse Ventura - Ora TV",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-QdslBT71Usk/AAAAAAAAAAI/AAAAAAAAAAA/nVe111QnTWg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Conspiracy Theory with Jesse Ventura",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail=icon,
        folder=True )
run()
