# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Talent Lottery Addon by The Knife.
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

addonID = 'plugin.video.TalentLottery'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLorGSwlLq2vvdCE8YyL8tpTsL-6FFpXsl"
YOUTUBE_CHANNEL_ID_2 = "PLg-gx_BzTsSeJHXz28Z4KLiAY1rwFmyWm"
YOUTUBE_CHANNEL_ID_3 = "Mynameisbambi16"
YOUTUBE_CHANNEL_ID_4 = "UCdZcASOcp8Z-QpWW1idSMdA"
YOUTUBE_CHANNEL_ID_5 = "UCdTlq7YnE21mINBZTEjKWiA"
YOUTUBE_CHANNEL_ID_6 = "PLVr_wPDjxv5rI7vjriqL8rWGXJq51DRj8"

# Entry point
def run():
    plugintools.log("TalentLottery.run")
    
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
        title="Aspiring Singer/Songwriter - April Story - apester187",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-WCV_ade52jM/AAAAAAAAAAI/AAAAAAAAAAA/UJsFv7QFCO0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Aspiring Film Maker - Mafftech",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-y2aMd2q31ao/AAAAAAAAAAI/AAAAAAAAAAA/ZwFnNinFptI/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Aspiring Makeup Artist - Ali Vaughan-Masamitsu",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-oSqKG32O5lk/AAAAAAAAAAI/AAAAAAAAAAA/zZHS9Dpid20/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Aspiring Voice Actor - Chris Mullins",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-UxGZ0xWhbSw/AAAAAAAAAAI/AAAAAAAAAAA/kdAQ30GHq98/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Aspiring Animator - Haley",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-RFXFz9QPYWA/AAAAAAAAAAI/AAAAAAAAAAA/31pSVMbgMpQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Aspiring Dancers - Sophia and Alex",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-qzud4EWNsxA/AAAAAAAAAAI/AAAAAAAAAAA/3rbiByWlqP8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

run()
