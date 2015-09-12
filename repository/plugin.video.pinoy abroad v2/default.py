# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pinoy abroad v2 by pulsemediahubuk (pulsemediahub)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: pulsemediahubuk
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.pinoyabroadv2'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "TheABSCBNNews"
YOUTUBE_CHANNEL_ID_2 = "abscbnsports"
YOUTUBE_CHANNEL_ID_3 = "starrecordsinc"
YOUTUBE_CHANNEL_ID_4 = "PTVPhilippines"
YOUTUBE_CHANNEL_ID_5 = "TV5Philippines"
YOUTUBE_CHANNEL_ID_6 = "GMANETWORK"
YOUTUBE_CHANNEL_ID_7 = "gmanews"
YOUTUBE_CHANNEL_ID_8 = "gocochiry"
YOUTUBE_CHANNEL_ID_9 = "TheVoiceKidsABSCBN"
YOUTUBE_CHANNEL_ID_10 = "PinoyNewsBlogger"
YOUTUBE_CHANNEL_ID_11 = "cebu47"
YOUTUBE_CHANNEL_ID_12 = "pinoytube2010"
YOUTUBE_CHANNEL_ID_13 = "luweehsah"
YOUTUBE_CHANNEL_ID_14 = "PagkaingPinoyTV"
YOUTUBE_CHANNEL_ID_15 = "GMAweekendtelebabad"
YOUTUBE_CHANNEL_ID_16 = "gmapublicaffairs"
YOUTUBE_CHANNEL_ID_17 = "mannypacquiaofficial"

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
        title="ABS CBN NEWS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="http://s7.postimg.org/4knv46bdn/ABS_CBN_logo_2014.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ABS CBN SPORTS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://s1.postimg.org/o87kegl2n/abscbnsports.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ABS CBN STAR MUSIC",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://s16.postimg.org/suw3hxos5/ABS_CBN_Starmusic.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="PTVPhilippines",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="http://s14.postimg.org/dq601q7qp/Peoplestvph_svg.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TV5 Philippines",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://s9.postimg.org/asj8ixirj/TV5.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="GMA NETWORK",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="http://s3.postimg.org/w1qan9q2b/gma.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="GMA NEWS",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="http://s16.postimg.org/rrl5xgiwl/gmaaaa.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pinoy Top List",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://s29.postimg.org/n7kmaee1j/top.png",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="The_Voice_Kids_ABSCBN",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="http://s8.postimg.org/gkrrdlqfp/The_Voice_Kids_ABSCBN.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pinoy News Blogger",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://s18.postimg.org/kgvzt48ud/pnb.png",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Cctn Cebu",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://s3.postimg.org/vhkgc2blf/Cctn_Cebu.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="PINOY TUBE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://s7.postimg.org/4qu152zkr/PINOYTUBE.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Tagalog Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="http://s11.postimg.org/4fo8isxw3/Tagalog_Kitchen.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="PagkaingPinoyTV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="http://s15.postimg.org/b5c1z35cb/pagkaingpinoytv_com.png",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="GMA weekend telebabad",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="http://s1.postimg.org/52x3hbovj/GMAweekendtelebabad.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="gma public affairs",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="http://s2.postimg.org/6qqwv7rkp/gmapublicaffairs.png",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="manny pacquia official",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="http://s3.postimg.org/uwu7q8tv7/mannypacquiaofficial.jpg",
        folder=True )

        
   	
run()
