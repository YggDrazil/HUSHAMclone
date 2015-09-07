# -*- coding: utf-8 -*-
#------------------------------------------------------------
# SF Movies on YouTube Addon by coldkeys
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

addonID = 'plugin.video.ytsf'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "classicscifimovie"
YOUTUBE_CHANNEL_ID_2 = "oldscifimovies"
YOUTUBE_CHANNEL_ID_3 = "UChG9taCaJvLAL66QuDuKK2A"
YOUTUBE_CHANNEL_ID_4 = "UCEA1biEh0Z2MrdXMB8W1g0A"
YOUTUBE_CHANNEL_ID_5 = "tdebbie2002s"
YOUTUBE_CHANNEL_ID_6 = "ABMovieChannel"
YOUTUBE_CHANNEL_ID_7 = "UCFuZe7O_A4au4IPkUDE1HFQ"
YOUTUBE_CHANNEL_ID_8 = "Blakes7Movies"
YOUTUBE_CHANNEL_ID_9 = "UCCXEt6-fZgeDpqK4PHbGUpg"
YOUTUBE_CHANNEL_ID_10 = "SciFiHorrorTrailers"

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
        title="Classic Science Fiction Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-8PiigD59rX8/AAAAAAAAAAI/AAAAAAAAAAA/ip_EJ5CzgVM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Old Science Fiction Movies",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-2JBQ9iwEyHg/AAAAAAAAAAI/AAAAAAAAAAA/E8MFen8HgMw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vintage Science Fiction Movies",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-kfwaQwwBD-s/AAAAAAAAAAI/AAAAAAAAAAA/FAX69BBvgHo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Sci-Fi Cinema Channel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-WsYQYTOkwT4/AAAAAAAAAAI/AAAAAAAAAAA/JYfTQ_L6b4Q/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="tdebbie2002s CLICK ON PLAYLIST",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.ytimg.com/i/uAjz1LAvgudcQNQeGjF2wQ/mq1.jpg?v=510cc89e",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="AB Movie Channel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-t7toB6M6RdQ/AAAAAAAAAAI/AAAAAAAAAAA/2N8_BIlF_9g/s100-c-k-no/photo.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="#ScienceFiction - Check the Playlists",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://i.ytimg.com/i/FuZe7O_A4au4IPkUDE1HFQ/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Blakes 7",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-X4V-Gk2ylZI/AAAAAAAAAAI/AAAAAAAAAAA/fZ8ZmTYXPnw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="#Fantasy - Check the Playlists",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://i.ytimg.com/i/CXEt6-fZgeDpqK4PHbGUpg/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SciFi Horror Movie Trailers",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-lPsxV27vOb4/AAAAAAAAAAI/AAAAAAAAAAA/iJWZbAqxjcc/s100-c-k-no/photo.jpg",
        folder=True )
run()
