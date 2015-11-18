# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Used an addon from coldkeys devlopment to make this addon for islamic reason
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Original addon Author: coldkeys
# Author: Husham.com
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.husham-ahalmuhajir'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCNkQZkmCiT7gOVTSMlLz7cQ"
YOUTUBE_CHANNEL_ID_2 = "UCVZNS89ZdukOh26qBnM-S_g"
YOUTUBE_CHANNEL_ID_3 = "UCrgJRoRy37qzHOYLz7u6H4A"


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
        title="Sheikh Abdul Hamid -الشيخ عبدالحميد المهاجر",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-cvxdWTXh_Hc/AAAAAAAAAAI/AAAAAAAAAAA/qLxLYuq0OoE/s100-c-k-no/photo.jpg",
        folder=True )
		
	plugintools.add_item( 
        #action="", 
        title="اية الله السيد كمال الحيدري",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-wMd67Z6lN6Y/AAAAAAAAAAI/AAAAAAAAAAA/lwFbCFdfQHg/s100-c-k-no/photo.jpg",
        folder=True )
		
	plugintools.add_item( 
        #action="", 
        title="Alhaydari-tube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-TiFlfrdhBgg/AAAAAAAAAAI/AAAAAAAAAAA/jdYf3F7R7YY/s100-c-k-no/photo.jpg",
        folder=True )
			
run()













