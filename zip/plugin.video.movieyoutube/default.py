# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Movies on YouTube Addon by coldkeys
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

addonID = 'plugin.video.movieyoutube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "TheKingsofHorror"
YOUTUBE_CHANNEL_ID_2 = "UCfjp6_4aAvhDGzvSkkAo0Jg"
YOUTUBE_CHANNEL_ID_3 = "UCaDVeUo4Xw2J7CX7Oyet1HA"
YOUTUBE_CHANNEL_ID_4 = "classicscifimovie"
YOUTUBE_CHANNEL_ID_5 = "classiccomedymovie"
YOUTUBE_CHANNEL_ID_6 = "classicmysterymovies"
YOUTUBE_CHANNEL_ID_7 = "classicromancemovies"
YOUTUBE_CHANNEL_ID_8 = "monsterhorrorhouse"
YOUTUBE_CHANNEL_ID_9 = "FullHorrorcom"
YOUTUBE_CHANNEL_ID_10 = "TVTERRORLAND"

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
        title="Kings of Horror",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-kQJTY1j3FwM/AAAAAAAAAAI/AAAAAAAAAAA/WYLXCrtBTGE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CiNENET",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-4PaF-kMXwvc/AAAAAAAAAAI/AAAAAAAAAAA/UYnCs4kSqJc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Adventure Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-nnYoNaEinJg/AAAAAAAAAAI/AAAAAAAAAAA/c-BsRFjaKLo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Science Fiction Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-8PiigD59rX8/AAAAAAAAAAI/AAAAAAAAAAA/ip_EJ5CzgVM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Comedy Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-eMJ4r2u0OCk/AAAAAAAAAAI/AAAAAAAAAAA/w2OPN7667rA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Mystery Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-YLrr88EKrgY/AAAAAAAAAAI/AAAAAAAAAAA/wT0QJS-q-z8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Classic Romance Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-rTkeUN4bWiI/AAAAAAAAAAI/AAAAAAAAAAA/dbU3G9xHeOA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Monster Horror House",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-Z6XCFHXssj8/AAAAAAAAAAI/AAAAAAAAAAA/mURlU68JKAc/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Full Horror",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-Y2CXkDfA2jo/AAAAAAAAAAI/AAAAAAAAAAA/7gl5qWST43w/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TVTERRORLAND",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail=icon,
        folder=True )                
run()
