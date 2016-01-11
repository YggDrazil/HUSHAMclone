# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Dancehall Geniuz
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: geniuz
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.dancehallgeniuz'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "malawifreak007"
YOUTUBE_CHANNEL_ID_2 = "reggaeville"
YOUTUBE_CHANNEL_ID_3 = "UCDCXWGyh3Po6IVcoH9ny6wQ"
YOUTUBE_CHANNEL_ID_4 = "vprecords"
YOUTUBE_CHANNEL_ID_5 = "krishgeniusmusic"
YOUTUBE_CHANNEL_ID_6 = "jjevafrassonceagain"
YOUTUBE_CHANNEL_ID_7 = "Crushroad876"
YOUTUBE_CHANNEL_ID_8 = "GazaPriinceEnt1"
YOUTUBE_CHANNEL_ID_9 = "AkamEntertainments"
YOUTUBE_CHANNEL_ID_10 = "JopKid100"
YOUTUBE_CHANNEL_ID_11 = "DigitalPlaylistEntt"
YOUTUBE_CHANNEL_ID_12 = "rdk29"
YOUTUBE_CHANNEL_ID_13 = "DancehallOfWar"
YOUTUBE_CHANNEL_ID_14 = "ityandfancycatshow"
YOUTUBE_CHANNEL_ID_15 = "majahhype"
YOUTUBE_CHANNEL_ID_16 = "goonstandup"
YOUTUBE_CHANNEL_ID_17 = "madaroadcom"
YOUTUBE_CHANNEL_ID_18 = "firejugglingtv"
YOUTUBE_CHANNEL_ID_19 = "OnstageTVJamaica"
YOUTUBE_CHANNEL_ID_20 = "NightlyFix"
YOUTUBE_CHANNEL_ID_21 = "SupaDupaFli79"
YOUTUBE_CHANNEL_ID_22 = "zjeasy"
YOUTUBE_CHANNEL_ID_23 = "justicedagreat"
YOUTUBE_CHANNEL_ID_24 = "malawifreak007"
YOUTUBE_CHANNEL_ID_25 = "UC7_aGyrvwh5TBZvyleQ97pw"
YOUTUBE_CHANNEL_ID_26 = "TheReggaeselecta"
YOUTUBE_CHANNEL_ID_27 = "LoversStylee"

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
        title="Dancehall Reggae TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-UILdUsWxXr4/AAAAAAAAAAI/AAAAAAAAAAA/TnfWsXhhdTo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Reggae Ville",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-wwYQZWrEoOQ/AAAAAAAAAAI/AAAAAAAAAAA/y-tI-bR0Xa0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Dancehall Navigator",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-ahQ7WQFBYvE/AAAAAAAAAAI/AAAAAAAAAAA/7VQa50FylcA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="VP Records",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-WjviOnlfdkI/AAAAAAAAAAI/AAAAAAAAAAA/DUfNjVF4q6s/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Krish Genius Media",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-Pz9pBrSszBY/AAAAAAAAAAI/AAAAAAAAAAA/YbfFa3cQr2w/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="JJ Eva Fras",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-j4Ctyr2aOpk/AAAAAAAAAAI/AAAAAAAAAAA/QK5mF_Rl5w0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Crushroad876",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-R4mhvzZN2aU/AAAAAAAAAAI/AAAAAAAAAAA/jbF0tt6xkhs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gaza Prince Ent",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-1lU5iYmA1ks/AAAAAAAAAAI/AAAAAAAAAAA/DWOCpPLuA8I/s88-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Akam Entertainments",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-wQ8woE0PkAM/AAAAAAAAAAI/AAAAAAAAAAA/V5jh5XF6NBQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="MafiaTheViper Ent",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-U66Oiy_aoV0/AAAAAAAAAAI/AAAAAAAAAAA/NbFMtYP5cUg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Digital Playlist Ent",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-CkmPiJyIWXc/AAAAAAAAAAI/AAAAAAAAAAA/SCblc7MMb50/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Soundbwoy Vinyl",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-wM65HM4VbJM/AAAAAAAAAAI/AAAAAAAAAAA/nnIY51KTeIc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DJ RV Mixes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-ELZButABiaM/AAAAAAAAAAI/AAAAAAAAAAA/2k7Kv1yYW9M/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ity and Fancy Cat",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-2vbYzbWOVtU/AAAAAAAAAAI/AAAAAAAAAAA/j5GD3vC9ya4/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Majah Hype and Di Ras",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-1OyV92jp6Gk/AAAAAAAAAAI/AAAAAAAAAAA/-4YZ2BG1hMg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Trabass Tv",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-OxZvZX1ztl8/AAAAAAAAAAI/AAAAAAAAAAA/Gdwh2PCUatQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mad A Road",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-TPfp829AqNI/AAAAAAAAAAI/AAAAAAAAAAA/yJl21BTxlhM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gibbo Presents",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-Z5d_4QnYU4w/AAAAAAAAAAI/AAAAAAAAAAA/CG7JQsYGGfE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="On Stage TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-HLiOyUwEP6U/AAAAAAAAAAI/AAAAAAAAAAA/Sq16XO4vIUQ/s100-c-k-no/photo.jpg",
        folder=True )
               
    plugintools.add_item( 
        #action="", 
        title="Nightly Fix",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-FnaeZPH_0f8/AAAAAAAAAAI/AAAAAAAAAAA/YONbdeaa9_g/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Strictly Dubplatemixes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/--MSfOAMdjpY/AAAAAAAAAAI/AAAAAAAAAAA/Flz39IIg-0I/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ZJ Easy Mixes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-xar1H1JC_wo/AAAAAAAAAAI/AAAAAAAAAAA/tOf-j-i9fwE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Justice Sound Mixes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-ljvnZ4QG7WA/AAAAAAAAAAI/AAAAAAAAAAA/YqzZPYxAaCY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="DJ Kaas",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://i.ytimg.com/vi/9n1B_YRrWsw/mqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lloyd Williams 90's Dancehallmixes",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-pYpEOEE_IS4/AAAAAAAAAAI/AAAAAAAAAAA/t70MqZ9IxSQ/s100-c-k-no/photo.jpg",
        folder=True )

    
    plugintools.add_item( 
        #action="", 
        title="The Reggae Selecta",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/--DubggjdhGs/AAAAAAAAAAI/AAAAAAAAAAA/Lg5zk-i_X_0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lovers Stylee",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-qPRJy80EeNA/AAAAAAAAAAI/AAAAAAAAAAA/kQEj566YGts/s100-c-k-no/photo.jpg",
        folder=True )
               		
run()
