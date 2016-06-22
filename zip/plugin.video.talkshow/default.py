# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Talk Show Addon by The Knife.
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: The Knife
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.talkshow'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "teamcoco"
YOUTUBE_CHANNEL_ID_2 = "TheEllenShow"
YOUTUBE_CHANNEL_ID_3 = "TheLateLateShow"
YOUTUBE_CHANNEL_ID_4 = "latenight"
YOUTUBE_CHANNEL_ID_5 = "JimmyKimmelLive"
YOUTUBE_CHANNEL_ID_6 = "LastWeekTonight"
YOUTUBE_CHANNEL_ID_7 = "LIVEKellyandMichael"
YOUTUBE_CHANNEL_ID_8 = "LateNightSeth"
YOUTUBE_CHANNEL_ID_9 = "UCMtFAi84ehTSYSE9XoHefig"
YOUTUBE_CHANNEL_ID_10 = "UCwWhs_6x42TyRM4Wstoq8HA"
YOUTUBE_CHANNEL_ID_11 = "ABCTheView"

# Entry point
def run():
    plugintools.log("talkshow.run")
    
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
        title="Conan - Conan O'Brien",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-fl-1HlAzrrI/AAAAAAAAAAI/AAAAAAAAAAA/pYLiLlQWlTE/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ellen DeGeneres - The Ellen DeGeneres Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-dDZUkj9sY4g/AAAAAAAAAAI/AAAAAAAAAAA/oy6dm2Uy8dc/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="James Corden - The Late Late Show with James Corden",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-NhxJe9XKyV8/AAAAAAAAAAI/AAAAAAAAAAA/XkSb5PFaHP8/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jimmy Fallon - The Tonight Show Starring Jimmy Fallon",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-x3CU1CXklQI/AAAAAAAAAAI/AAAAAAAAAAA/jPQ9GJeU53g/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jimmy Kimmel - Jimmy Kimmel Live",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-icjlceY943o/AAAAAAAAAAI/AAAAAAAAAAA/U0fuYSj5vJ0/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="John Oliver - Last Week Tonight with John Oliver",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-lc3LinEhpgA/AAAAAAAAAAI/AAAAAAAAAAA/A6-FbtNyNgU/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kelly Ripa - LIVE with Kelly",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-_jcmQMr68G4/AAAAAAAAAAI/AAAAAAAAAAA/-ThryHCJwrs/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Seth Meyers - Late Night with Seth Meyers",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-TI5ffZo0Qd4/AAAAAAAAAAI/AAAAAAAAAAA/glgeFHJ0Sto/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Stephen Colbert - The Late Show with Stephen Colbert",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-_DMSPt1vZaw/AAAAAAAAAAI/AAAAAAAAAAA/sSVARCDuXwE/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Trevor Noah - The Daily Show with Trevor Noah",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-lYZk4150pXc/AAAAAAAAAAI/AAAAAAAAAAA/CR6MoHGaJiY/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Those chicks from... - The View",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-jn7rThGotIc/AAAAAAAAAAI/AAAAAAAAAAA/LnxMsxRV3Aw/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )  
              		
run()
