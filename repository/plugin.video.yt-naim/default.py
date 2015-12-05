# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Native American Indian Movies Addon by coldkeys
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

addonID = 'plugin.video.yt-naim'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLEGHogmscTy3LjnC4QwVCK5hzAOzIxbhm"
YOUTUBE_CHANNEL_ID_2 = "PLS2UsKtbxrfKn-uf_xL4KtKTKYOBP5B6s"
YOUTUBE_CHANNEL_ID_3 = "PLl-k9d3w4HiEVQdWifDnqD-7vbXqtIr5Z"
YOUTUBE_CHANNEL_ID_4 = "PLqxphBuPVws7NSSEdMJZGckhS98rpgnGb"
YOUTUBE_CHANNEL_ID_5 = "PL152bjytsMC4o5VSVv7ysShoA7dmWHx3b"
YOUTUBE_CHANNEL_ID_6 = "PL152bjytsMC5b05u9NxqkP7xhsxOY89R5"

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
        title="Native American Indian Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.ytimg.com/vi/1pX6FBSUyQI/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Native American Films",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-mHCXCA2YuIg/AAAAAAAAAAI/AAAAAAAAAAA/G-sxEHIhcmc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Native American TV-Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.ytimg.com/i/Ol-6cE7XneGkfgkzQfSB0A/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Native American Movies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-fLv9tmg6zpU/AAAAAAAAAAI/AAAAAAAAAAA/XkwHHnq17as/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Native American Movies-Documentaries",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://i.ytimg.com/vi/d02DbJyRFrQ/default.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Native American Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-QekG8ajGWI4/AAAAAAAAAAI/AAAAAAAAAAA/bJiFSbgNh3U/s100-c-k-no/photo.jpg",
        folder=True )
run()
