# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Cooking on YouTube 2 by coldkeys
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

addonID = 'plugin.video.yt-cook2'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLI0ThKlu3KpNofdPgXdLHEthOSDtyfwVl"
YOUTUBE_CHANNEL_ID_2 = "PL_waVzAxWNJX5tsRXoAvWRIzjgL0D1_oR"
YOUTUBE_CHANNEL_ID_3 = "PLSwj9aP0N1peoXDF0x_RjmBiu_AA2Qu1g"
YOUTUBE_CHANNEL_ID_4 = "PLgN9b15D76vK7cUs6-wvm_WwZt5YBymbo"
YOUTUBE_CHANNEL_ID_5 = "EpicMealTime"
YOUTUBE_CHANNEL_ID_6 = "MarioBatali"
YOUTUBE_CHANNEL_ID_7 = "tastemade"
YOUTUBE_CHANNEL_ID_8 = "escoffieronline"
YOUTUBE_CHANNEL_ID_9 = "CakeVideosfromexpert"
YOUTUBE_CHANNEL_ID_10 = "SimplyBakings"
YOUTUBE_CHANNEL_ID_11 = "montrealconfections"
YOUTUBE_CHANNEL_ID_12 = "eateastIndian"
YOUTUBE_CHANNEL_ID_13 = "SeonkyoungLongest"
YOUTUBE_CHANNEL_ID_14 = "cookingmexicanrecipe"
YOUTUBE_CHANNEL_ID_15 = "slolita1"
YOUTUBE_CHANNEL_ID_16 = "SmokeyGoodness"
YOUTUBE_CHANNEL_ID_17 = "StokedOnSmoke"
YOUTUBE_CHANNEL_ID_18 = "howtobbqright"
YOUTUBE_CHANNEL_ID_19 = "TheWolfePit"
YOUTUBE_CHANNEL_ID_20 = "pastryparrot1"
YOUTUBE_CHANNEL_ID_21 = "stevescooking"
YOUTUBE_CHANNEL_ID_22 = "cookingguide"
YOUTUBE_CHANNEL_ID_23 = "howtocookgreat"
YOUTUBE_CHANNEL_ID_24 = "PLKi96GGIQsFIx4o3c_6Aamd9OUql0hCUJ"
YOUTUBE_CHANNEL_ID_25 = "PLb2FN4PHG1lcqMPhaNRWePFprAlvLMoWX"
YOUTUBE_CHANNEL_ID_26 = "PLF386D66A05F06E60"
YOUTUBE_CHANNEL_ID_27 = "TheKitchenWitch1"
YOUTUBE_CHANNEL_ID_28 = "simpleeasycooking"
YOUTUBE_CHANNEL_ID_29 = "CookingwithKarma"
YOUTUBE_CHANNEL_ID_30 = "SimpleCookingChannel"
YOUTUBE_CHANNEL_ID_31 = "myvirginkitchen"
YOUTUBE_CHANNEL_ID_32 = "BBCFood"
YOUTUBE_CHANNEL_ID_33 = "EZGlutenFree"
YOUTUBE_CHANNEL_ID_34 = "mooneyskitchen"
YOUTUBE_CHANNEL_ID_35 = "PLDn0RqHU2n_4EQLDY80Ji9mNO44djWH1U"
YOUTUBE_CHANNEL_ID_36 = "FoodFoodindia"
YOUTUBE_CHANNEL_ID_37 = "RajshriFood"
YOUTUBE_CHANNEL_ID_38 = "madhura94"
YOUTUBE_CHANNEL_ID_39 = "sruthiskitchen"
YOUTUBE_CHANNEL_ID_40 = "FoodsAndFlavors"
YOUTUBE_CHANNEL_ID_41 = "AsianCookingmadeEasy"
YOUTUBE_CHANNEL_ID_42 = "ezjapanesecooking"
YOUTUBE_CHANNEL_ID_43 = "justonecookbook"
YOUTUBE_CHANNEL_ID_44 = "vongs510"
YOUTUBE_CHANNEL_ID_45 = "JoyofBaking1"
YOUTUBE_CHANNEL_ID_46 = "OriginalNakedChef"
YOUTUBE_CHANNEL_ID_47 = "TheChiappaSisters"
YOUTUBE_CHANNEL_ID_48 = "Tescofoodandwine"
YOUTUBE_CHANNEL_ID_49 = "CookingAndCrafting"
YOUTUBE_CHANNEL_ID_50 = "JamiesDrinksTube"


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
        title="Sichuan Cuisine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.ytimg.com/i/UZJ-KjIC5gkESKz3zy4SKw/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cantonese Cuisine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://i.ytimg.com/i/ey1WzFPD181vBpFFRZkiSA/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chinese Cuisine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://i.ytimg.com/i/KW4AKFF9y3czCUZizh6BUA/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hunan Cuisine",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://i.ytimg.com/i/hfzlZ7hx5J4BKPs5GUbdFA/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Epic Meal Time",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-wsUurA2UA6Q/AAAAAAAAAAI/AAAAAAAAAAA/mYrc7qkwqbw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mario Batali",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-clv2EOqjdao/AAAAAAAAAAI/AAAAAAAAAAA/di81_dER5Fw/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Tastemade",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-aPb0s8NqbWY/AAAAAAAAAAI/AAAAAAAAAAA/Bogt-RdYi4s/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Escoffier Online",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-Ea_83EVxVQM/AAAAAAAAAAI/AAAAAAAAAAA/P5OWyxBzSBA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HowToCakeVideos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-KdJvKHSY4iY/AAAAAAAAAAI/AAAAAAAAAAA/hHMNgzlYp_M/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SimplyBakings",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-3QhvErVbnbk/AAAAAAAAAAI/AAAAAAAAAAA/1bEBc-NSiug/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Montreal Confections",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-1i4TW9vAD_0/AAAAAAAAAAI/AAAAAAAAAAA/gQImflh0BmI/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Eat East Indian",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-aU2LR98GKdg/AAAAAAAAAAI/AAAAAAAAAAA/Xl_u70MF_rc/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Seonkyoung Longest",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-nwZx51glSZ8/AAAAAAAAAAI/AAAAAAAAAAA/ZPo-bpKXxr0/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Rockin Robin's Cooking Mexican Recipes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-Y-ZW9ZV5twQ/AAAAAAAAAAI/AAAAAAAAAAA/5YD3lmeuoBM/s100-c-k-no/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Easy Cooking with Sandy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-7K3Xz_h6uqI/AAAAAAAAAAI/AAAAAAAAAAA/lvirB8tcLx8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SmokeyGoodness",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-pDGqrOt3oas/AAAAAAAAAAI/AAAAAAAAAAA/YwpLcpaXGD0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="StokedOnSmoke",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-7XboBG5m65k/AAAAAAAAAAI/AAAAAAAAAAA/Iil7_t4iHaU/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HowToBBQRight Malcom Reed",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-PSf7ibg0KNo/AAAAAAAAAAI/AAAAAAAAAAA/92Ode5upl88/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="TheWolfePit",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-HI7kRyWB0b0/AAAAAAAAAAI/AAAAAAAAAAA/HsSB9zi4I0c/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Frugal Chef",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-BKCnFvLj3ds/AAAAAAAAAAI/AAAAAAAAAAA/UrPn1ZhDC4w/s100-c-k-no/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="STEVESCOOKING",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-QHyMkD-IgLk/AAAAAAAAAAI/AAAAAAAAAAA/AMn7L7vqCug/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="eHow Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-eke0ac0PpeI/AAAAAAAAAAI/AAAAAAAAAAA/TLeTPhdrGog/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="How to Cook GREAT",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-AuevfWGmgYs/AAAAAAAAAAI/AAAAAAAAAAA/hlxDiILP-54/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Betty Crocker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://i.ytimg.com/i/FvcyhqkRtuuEmUZmTNl83A/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Julia Child The French Chef",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://i.ytimg.com/i/IlHkThvc9pXelst40y81OA/mq1.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Caribbean Pot",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-APYreRY-_tg/AAAAAAAAAAI/AAAAAAAAAAA/nqmxbm4_lFk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Lyndsay Wells, The Kitchen Witch",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-ISV7rnKwkBQ/AAAAAAAAAAI/AAAAAAAAAAA/t06arLSLDSc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Todd's Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-Fg67btVgZkI/AAAAAAAAAAI/AAAAAAAAAAA/tfrKjjD6yZc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CookingwithKarma",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/-QIX1-GcNwGg/AAAAAAAAAAI/AAAAAAAAAAA/kgTCV6FIX6E/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="SimpleCookingChannel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/-NZqy4NglTzY/AAAAAAAAAAI/AAAAAAAAAAA/-Wo1LsYXJtg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="My Virgin Kitchen - Barry Lewis",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-EEXzm10q6dc/AAAAAAAAAAI/AAAAAAAAAAA/MeyIBA01MMs/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="BBC Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/-O3tT5_1Spuc/AAAAAAAAAAI/AAAAAAAAAAA/TINkiISleWs/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="EZGlutenFree",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-RVbfgBvwquU/AAAAAAAAAAI/AAAAAAAAAAA/n91hu_2WVuM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Chef Mooney",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-1tunkxmgd_E/AAAAAAAAAAI/AAAAAAAAAAA/_lNZcp4lXwc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Quick and Easy Indian Food Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-loutHGQgpts/AAAAAAAAAAI/AAAAAAAAAAA/GMuoes2sxuo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="FoodFood India",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-MlPj8fz7Pwg/AAAAAAAAAAI/AAAAAAAAAAA/t8sJ07Lb6dw/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Rajshri Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-rULo2zocsVY/AAAAAAAAAAI/AAAAAAAAAAA/wqdcIK_yBV8/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="MadhurasRecipe.com",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-T2xL9_7-F6U/AAAAAAAAAAI/AAAAAAAAAAA/KD8vb_iBDhk/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Sruthi's Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-Z34IdzMrUvY/AAAAAAAAAAI/AAAAAAAAAAA/cJ3G6556XZU/s100-c-k-no/photo.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Foods and Flavors by Shilpi",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-puH_uGOC2GM/AAAAAAAAAAI/AAAAAAAAAAA/pCDM5-RNV7M/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Asian Cooking Made Easy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-9b5VJhkXoKM/AAAAAAAAAAI/AAAAAAAAAAA/H6LSq-Ay4x8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="E Z Japanese Cooking",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-qUOa5heipwM/AAAAAAAAAAI/AAAAAAAAAAA/doYUacOwU7k/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Just One Cookbook - Easy Japanese Recipes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-WMi1MHF5wOA/AAAAAAAAAAI/AAAAAAAAAAA/8DBTADTPiwM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Khoan Vong",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/-aU5WFjhEEnU/AAAAAAAAAAI/AAAAAAAAAAA/8vWI_HcO7-A/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Joy of Baking",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://yt3.ggpht.com/-C-FKi0zjMYA/AAAAAAAAAAI/AAAAAAAAAAA/ZiLQS9TM88M/s100-c-k-no/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Original Naked Chef",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/-KPOx6aOneHU/AAAAAAAAAAI/AAAAAAAAAAA/TvdHOmTVaoY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Chiappa Sisters - Simply Italian",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/-hfWvAJQhYIo/AAAAAAAAAAI/AAAAAAAAAAA/-Ap_EkPgvlM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tesco Food and Wine",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/-rspRJSfTR6Q/AAAAAAAAAAI/AAAAAAAAAAA/YPN5LaIF27A/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cooking And Crafting",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://yt3.ggpht.com/-5raKrDwamMI/AAAAAAAAAAI/AAAAAAAAAAA/pwoLmjbRPkE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jamie Oliver's Drinks Tube",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/-M3C3E6RGISs/AAAAAAAAAAI/AAAAAAAAAAA/5Zp8vWpaPF4/s100-c-k-no/photo.jpg",
        folder=True )
run()
