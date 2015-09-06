# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Western Movies on YouTube Addon by coldkeys
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

addonID = 'plugin.video.ytwesterns'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "WatchAcmeMovies"
YOUTUBE_CHANNEL_ID_2 = "SpaghettiWesternTV"
YOUTUBE_CHANNEL_ID_3 = "WorldHipHopStarTv"
YOUTUBE_CHANNEL_ID_4 = "Nunuhihikeke"
YOUTUBE_CHANNEL_ID_5 = "WesternTvSeries"
YOUTUBE_CHANNEL_ID_6 = "westernmaniadotcom"
YOUTUBE_CHANNEL_ID_7 = "westernsontheweb"
YOUTUBE_CHANNEL_ID_8 = "wildwesttoys1"
YOUTUBE_CHANNEL_ID_9 = "westernfilms35"
YOUTUBE_CHANNEL_ID_10 = "wildweststuff"

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
        title="Acme Moving Pictures",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-FcoBuknCEiE/AAAAAAAAAAI/AAAAAAAAAAA/9a8wAGje3X4/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SpaghettiWesternTV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-8sISB0fYdn8/AAAAAAAAAAI/AAAAAAAAAAA/Cjlrgh5rRa4/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Western Life",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-R3Oy0FZW8Uw/AAAAAAAAAAI/AAAAAAAAAAA/kUcYnjFUMBs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Western Movie",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-YapAjlLAxWg/AAAAAAAAAAI/AAAAAAAAAAA/FoWfDttJuvc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WesternTvSeries",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-4VZmrkcU_j8/AAAAAAAAAAI/AAAAAAAAAAA/q8wqbu6c5-I/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Western Mania",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-Xr84C-lRqLY/AAAAAAAAAAI/AAAAAAAAAAA/SE1-KWnNDs8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WesternsOnTheWeb",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-8InAo4LXZzI/AAAAAAAAAAI/AAAAAAAAAAA/UhaMtxxn4WI/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wild West Toys",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-Xn4vWNCDVYE/AAAAAAAAAAI/AAAAAAAAAAA/MjIiZeyCUGU/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Jess Calson - Westerns",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-tjlbkWNZxi4/AAAAAAAAAAI/AAAAAAAAAAA/kiXxMgoloVs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="wildweststuff",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-ghyJ1mo0yII/AAAAAAAAAAI/AAAAAAAAAAA/yu1E0eMxGMM/s100-c-k-no/photo.jpg",
        folder=True )                
run()
