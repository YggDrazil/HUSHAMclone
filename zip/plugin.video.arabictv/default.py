# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Binky TV special thanks to original authors of the code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: Dandymedia
#------------------------------------------------------------

import os
import sys, dandy
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.arabictv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

xbmc.executebuiltin('Container.SetViewMode(500)')

YOUTUBE_CHANNEL_ID_1 = "PLJ-qZvjnxPlRLXoSY233JNAyrZAe2t3Sr"
YOUTUBE_CHANNEL_ID_2 = "UCLmDjHLmnXB8cpnYJDUfKCA"
YOUTUBE_CHANNEL_ID_3 = "PLZHhFgNF6x35FUWu1a8qysaZhHm4lY3Nf"



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
        title="arabic live",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.imgsafe.org/a76f1562af.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="arabic movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.imgsafe.org/a77b2dd308.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="arabic music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.imgsafe.org/a780e90c72.jpg",
        folder=True )   
		
    

   

run()		
