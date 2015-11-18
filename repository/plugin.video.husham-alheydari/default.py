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

addonID = 'plugin.video.husham-alheydari'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCFj9KQcceK3XduMOVNyXrVg"
YOUTUBE_CHANNEL_ID_2 = "UCVZNS89ZdukOh26qBnM-S_g"
YOUTUBE_CHANNEL_ID_3 = "UCrgJRoRy37qzHOYLz7u6H4A"
YOUTUBE_CHANNEL_ID_4 = "UCBDsHHOrbdlrTOgkRvhYF5g"

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
        title="السيد كمال الحيدري",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-yTO8iBROuII/AAAAAAAAAAI/AAAAAAAAAAA/ltUtz3Y095Q/s100-c-k-no/photo.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="اية الله السيد كمال الحيدري",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-wMd67Z6lN6Y/AAAAAAAAAAI/AAAAAAAAAAA/lwFbCFdfQHg/s100-c-k-no/photo.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="alhaydari-tube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-TiFlfrdhBgg/AAAAAAAAAAI/AAAAAAAAAAA/jdYf3F7R7YY/s100-c-k-no/photo.jpg",
        folder=True )
    plugintools.add_item( 
        #action="", 
        title="مقتطفات مهمة من بحوث السيد كمال الحيدري",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-JktRrJlrQQ8/AAAAAAAAAAI/AAAAAAAAAAA/1PE5HcYxao4/s100-c-k-no/photo.jpg",
        folder=True )

run()
