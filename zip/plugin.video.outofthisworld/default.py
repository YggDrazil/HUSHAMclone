# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Out of this World Documentaries Addon by coldkeys
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

addonID = 'plugin.video.outofthisworld'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UFOTVstudios"
YOUTUBE_CHANNEL_ID_2 = "thirdphaseofmoon"
YOUTUBE_CHANNEL_ID_3 = "ProjectUFOs"
YOUTUBE_CHANNEL_ID_4 = "UCtwAqRfw901jAo9JbX3KEHQ"
YOUTUBE_CHANNEL_ID_5 = "DiscloseTruthTV"
YOUTUBE_CHANNEL_ID_6 = "DisclosureDiscovery"
YOUTUBE_CHANNEL_ID_7 = "UC0cHyy4uVB8ydT5R-Z963yg"
YOUTUBE_CHANNEL_ID_8 = "MrTechinnovations"
YOUTUBE_CHANNEL_ID_9 = "UC4Q36FUg_NOHCpxoBv2wQ1g"
YOUTUBE_CHANNEL_ID_10 = "UCANjoLwIMhnOJxWASig2AWQ"
YOUTUBE_CHANNEL_ID_11 = "UCIDz9vqfnvQsmx4QncJRiMw"
YOUTUBE_CHANNEL_ID_12 = "UCqLr8VyFA9qYPuGSLedT2RQ"
YOUTUBE_CHANNEL_ID_13 = "thetruthrevealed777"
YOUTUBE_CHANNEL_ID_14 = "UCebWvcOGXtQpx66QuVECvwA"
YOUTUBE_CHANNEL_ID_15 = "ParanormalMoviesful"
YOUTUBE_CHANNEL_ID_16 = "UCUiC4S6mdNi_eOEsnxrBZEQ"
YOUTUBE_CHANNEL_ID_17 = "UCLmJkq6aPq-koRv0RUYNwvA"
YOUTUBE_CHANNEL_ID_18 = "UC6wsBunCYqRt3XBS11rifHg"
YOUTUBE_CHANNEL_ID_19 = "HubbleSiteChannel"
YOUTUBE_CHANNEL_ID_20 = "UCUv6Ihpc5WtQ2MyEiUY9n3g"
YOUTUBE_CHANNEL_ID_21 = "TheUFODocumentaries"
YOUTUBE_CHANNEL_ID_22 = "UFOvni2012"
YOUTUBE_CHANNEL_ID_23 = "FindingUFO"
YOUTUBE_CHANNEL_ID_24 = "UC8oWasW79JSMJ885UNVlVFA"
YOUTUBE_CHANNEL_ID_25 = "UCrIABzlPThjFkKigOPRiZdQ"

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
        title=" UFOTV® The Disclosure Movie Network ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="thirdphaseofmoon",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Project UFOs",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" The WTF Files ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title=" Disclose Truth TV ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" Disclosure Discovery ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail=icon,
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title=" Art of the World ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail=icon,
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title=" Ancient Innovations ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="  E.B.E Extraterrestrial Biological Entity ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" Science Documentary ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" Jinx Lol ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail=icon,
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="  Beyond UFOs 2015 ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail=icon,
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title=" thetruthrevealed777 ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail=icon,
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title=" Forbidden Knowledge 2015 ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail=icon,
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title=" Paranormal Alien Movies ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" Ancient Aliens【HD】 ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" DiscoveryDisclosure ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" Documentaries of UFO 2015 ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail=icon,
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title=" Hubble Space Telescope ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title=" Star Movie+ ",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail=icon,
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="The UFO Documentaries",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="UFOvni2012",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Finding UFO",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Documentary TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="UFO Documentary 2015",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail=icon,
        folder=True )
run()
