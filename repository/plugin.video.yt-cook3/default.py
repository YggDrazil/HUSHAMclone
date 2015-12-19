# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Cooking on YouTube 3 by coldkeys
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

addonID = 'plugin.video.yt-cook3'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCxWkRfzbILiLfH_ecpvceJA"
YOUTUBE_CHANNEL_ID_2 = "Fablunch"
YOUTUBE_CHANNEL_ID_3 = "HealthNutNutrition"
YOUTUBE_CHANNEL_ID_4 = "crumbsfood"
YOUTUBE_CHANNEL_ID_5 = "TheWorldKitchen"
YOUTUBE_CHANNEL_ID_6 = "OfficialMyKitchen"
YOUTUBE_CHANNEL_ID_7 = "KitchenNightmares"
YOUTUBE_CHANNEL_ID_8 = "theFword"
YOUTUBE_CHANNEL_ID_9 = "gordonramsayfoodie"
YOUTUBE_CHANNEL_ID_10 = "HomeVedaNutrition"
YOUTUBE_CHANNEL_ID_11 = "LetsBeFoodie"
YOUTUBE_CHANNEL_ID_12 = "jgswife"
YOUTUBE_CHANNEL_ID_13 = "UCmrNAfskDlTqfBeWQ5FFYGQ"
YOUTUBE_CHANNEL_ID_14 = "howtocookthat"
YOUTUBE_CHANNEL_ID_15 = "MokoBrownVegan"
YOUTUBE_CHANNEL_ID_16 = "VeganCookingWithLove"
YOUTUBE_CHANNEL_ID_17 = "veggietorials"
YOUTUBE_CHANNEL_ID_18 = "CupcakesandCardio"
YOUTUBE_CHANNEL_ID_19 = "hilahcooking"
YOUTUBE_CHANNEL_ID_20 = "PL152bjytsMC6d52kn7M5IhoxjchNMIhN6"
YOUTUBE_CHANNEL_ID_21 = "PLecDmWZ6vbWTjFPqyBd8w1APtlqLNofXh"
YOUTUBE_CHANNEL_ID_22 = "PLqH_GG24TkpKe_iulTSsRTI8JheauBM3t"
YOUTUBE_CHANNEL_ID_23 = "PL152bjytsMC6wpLO831xaiY9xFMFXzD9m"
YOUTUBE_CHANNEL_ID_24 = "PLoFCUKOoR9lv4hQccHHMsVvnvFgG4gCzG"
YOUTUBE_CHANNEL_ID_25 = "indiancrockpot"
YOUTUBE_CHANNEL_ID_26 = "PLY3TbPI0Vg8PPrVkqFjX12eE8MjyqIfD8"
YOUTUBE_CHANNEL_ID_27 = "PLcl0kBajtGOzAKorDisc1SDXUINzcu4ri"
YOUTUBE_CHANNEL_ID_28 = "PLgvK2FHxmOZd9F22KDz4B0BUvhXxCEzB6"
YOUTUBE_CHANNEL_ID_29 = "PL6C42540A9EF07175"
YOUTUBE_CHANNEL_ID_30 = "PL152bjytsMC7KPwj49Ew5YBIW9NmbBH0H"
YOUTUBE_CHANNEL_ID_31 = "PLGydKfiYcHj37KMdZW4U3LH8cC3JTF8Bn"
YOUTUBE_CHANNEL_ID_32 = "PLTyTajNN-cAom0ylkVKWgsCW7zJGVg07p"
YOUTUBE_CHANNEL_ID_33 = "PLqMrQ50EcKojm8Bh8rFivLyauoGPeW9um"
YOUTUBE_CHANNEL_ID_34 = "PLqMrQ50EcKohToUu8pLolnnt89yq34B5t"
YOUTUBE_CHANNEL_ID_35 = "PLqMrQ50EcKohztQI1NfPnael0RJxjGhmj"
YOUTUBE_CHANNEL_ID_36 = "PLqMrQ50EcKog4AHBxFHRju6QX-NFHo-hY"
YOUTUBE_CHANNEL_ID_37 = "PLqMrQ50EcKoi0Lms-5-cFdzXVbdIX3cs0"
YOUTUBE_CHANNEL_ID_38 = "HealthyKadai"
YOUTUBE_CHANNEL_ID_39 = "PL9EBubzSOKxvcg-M_StmHzB5QGBHp45iw"
YOUTUBE_CHANNEL_ID_40 = "my3streetfood"
YOUTUBE_CHANNEL_ID_41 = "UCChqsCRFePrP2X897iQkyAA"
YOUTUBE_CHANNEL_ID_42 = "foodjunction"
YOUTUBE_CHANNEL_ID_43 = "PLnvT_7ZyrvIz02Hrb6c4cYm8HTIoH9Xju"
YOUTUBE_CHANNEL_ID_44 = "PLVAvUrL_VQiMZLIGCgjWwRqivPBHz0bZv"
YOUTUBE_CHANNEL_ID_45 = "PLJHjrZhf5Gfr_3Fv55FE_QdAfW8ikQ3XK"
YOUTUBE_CHANNEL_ID_46 = "PLWuJCpE4EP5L_WO03XHgD_rIpsNDFYqNn"
YOUTUBE_CHANNEL_ID_47 = "PLjMg8wIdiWauSGMdaok8FRUkRBIpMH4Jv"
YOUTUBE_CHANNEL_ID_48 = "PL64W5XBCyUkm3bhABCPB-u08BObxmgbwY"
YOUTUBE_CHANNEL_ID_49 = "PLHQkzAXnGgVctyhMvV68jnbdapLVcutVn"
YOUTUBE_CHANNEL_ID_50 = "PL9eWEHQPXHwWYSGjPUnjLoQ_mHv_PrTVb"


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
        title="Food File Live TV",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/-Em3mb-44LjI/AAAAAAAAAAI/AAAAAAAAAAA/bVmyPesM1Kc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Fablunch",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-4i7hcnonuMs/AAAAAAAAAAI/AAAAAAAAAAA/ShqTdFXpe_w/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HealthNutNutrition",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-ktTPXJ5jTcY/AAAAAAAAAAI/AAAAAAAAAAA/BcAYFOOA-mc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Crumbs Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-xf9Hv5MKagA/AAAAAAAAAAI/AAAAAAAAAAA/3jH9Bc0fxHw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The World Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-6eO5dkZoKOY/AAAAAAAAAAI/AAAAAAAAAAA/z95CvvL64WY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Official My Kitchen",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/-fABnvmrZzgQ/AAAAAAAAAAI/AAAAAAAAAAA/6YKvLWDNjUQ/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Kitchen Nightmares",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-WJNIkxOkUrM/AAAAAAAAAAI/AAAAAAAAAAA/pauY0DR-1Oc/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="The F Word",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-KkGN4mC_ryM/AAAAAAAAAAI/AAAAAAAAAAA/PDnVBPaxTGY/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Mack Michaels",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-6TJ4tG7jBzg/AAAAAAAAAAI/AAAAAAAAAAA/SZkJ-Zw1F9M/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="HomeVeda Nutrition",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/-5_AAgehKpgg/AAAAAAAAAAI/AAAAAAAAAAA/Kv-OmzYoVdM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Let's Be Foodie",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-blEfTsHFI88/AAAAAAAAAAI/AAAAAAAAAAA/2EMPYd2TJxc/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Weelicious",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-VdRQW1q5VLM/AAAAAAAAAAI/AAAAAAAAAAA/fd5V8YhS_6c/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Inspire To Cook",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-FAaaH4amR9k/AAAAAAAAAAI/AAAAAAAAAAA/gWLlOmdTFPs/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="How To Cook That",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-BVr3FGmxht8/AAAAAAAAAAI/AAAAAAAAAAA/Xvh_CKEbu4Y/s100-c-k-no/photo.jpg",
        folder=True ) 
		
    plugintools.add_item( 
        #action="", 
        title="Brown Vegan",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-8FXamSUzTps/AAAAAAAAAAI/AAAAAAAAAAA/B2oLHtFDuLw/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Vegan Cooking With Love",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-UuNT9whKROo/AAAAAAAAAAI/AAAAAAAAAAA/jaVx27PHyqc/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Veggietorials",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-0_D-SpO946I/AAAAAAAAAAI/AAAAAAAAAAA/xpIMh419B50/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Cookies Cupcakes and Cardio",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-C-p4TKf1VLQ/AAAAAAAAAAI/AAAAAAAAAAA/l0qyJCvcfIs/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hilah Cooking",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-8O-hBbxo6-8/AAAAAAAAAAI/AAAAAAAAAAA/yDh7E7-z2jk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Tefal Actify Recipes and Guides",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-OEeD9azcEpY/AAAAAAAAAAI/AAAAAAAAAAA/uU8H90DEHTc/s100-c-k-no/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Healthy Recipes - Philips Air Fryer",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/-INrY2l94xxg/AAAAAAAAAAI/AAAAAAAAAAA/v1dQsFQuMNg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Healthy Airfryer Recipes - Fry without Oil!!!",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/-3NFw9IsmjR8/AAAAAAAAAAI/AAAAAAAAAAA/XlOfiO8RqbE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Philips Airfryer Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/-EyNocRhocbo/AAAAAAAAAAI/AAAAAAAAAAA/lzi3qVtDcuM/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Slow Cooker / Crockpot / Crock Pot recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/-5raKrDwamMI/AAAAAAAAAAI/AAAAAAAAAAA/pwoLmjbRPkE/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Indian Crock-Pot Cookery",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-qFFP5WruQtw/AAAAAAAAAAI/AAAAAAAAAAA/DEJrF0yFM-s/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Slow Cooker Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://media-cache-ak0.pinimg.com/736x/15/dd/41/15dd41cf81353da44ad190c56f320bbf.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Allrecipes Slow Cooker Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-nVEDlVwhNrs/AAAAAAAAAAI/AAAAAAAAAAA/RGAs3-lUDS4/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Slow Cooker Recipes | Crock Pot Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-nIagi_zs0dQ/AAAAAAAAAAI/AAAAAAAAAAA/3qciRz-z3ww/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Slowcooker recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/-jnXq778Tbf0/AAAAAAAAAAI/AAAAAAAAAAA/AH9PhyLXJpg/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="More Slow Cooker Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="http://media-cache-ak0.pinimg.com/736x/15/dd/41/15dd41cf81353da44ad190c56f320bbf.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Weight Watcher Girl Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-njQA9uu0GVk/AAAAAAAAAAI/AAAAAAAAAAA/ra8H1_suYl4/s100-c-k-no/photo.jpg",
        folder=True )                

    plugintools.add_item( 
        #action="", 
        title="Weight Watchers Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://yt3.ggpht.com/-3nkmyHTMSl8/AAAAAAAAAAI/AAAAAAAAAAA/RaFjsXcLq5g/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Weight Watchers Points Plus Recipes - Lunch & Dinner",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-sVsN9U9Xzxo/AAAAAAAAAAI/AAAAAAAAAAA/rAypBRVIBdo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Weight Watchers Points Plus Recipes - Snacks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-sVsN9U9Xzxo/AAAAAAAAAAI/AAAAAAAAAAA/rAypBRVIBdo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Weight Watchers Points Plus Recipes - Breakfast",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-sVsN9U9Xzxo/AAAAAAAAAAI/AAAAAAAAAAA/rAypBRVIBdo/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Weight Watchers Points Plus Recipes - Dessert",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-sVsN9U9Xzxo/AAAAAAAAAAI/AAAAAAAAAAA/rAypBRVIBdo/s100-c-k-no/photo.jpg",
        folder=True )    

    plugintools.add_item( 
        #action="", 
        title="Weight Watchers Points Plus Recipes - Dessert 2",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-sVsN9U9Xzxo/AAAAAAAAAAI/AAAAAAAAAAA/rAypBRVIBdo/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Healthy Kadai  Best Indian Recipes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-3NFw9IsmjR8/AAAAAAAAAAI/AAAAAAAAAAA/XlOfiO8RqbE/s100-c-k-no/photo.jpg",
        folder=True )  

    plugintools.add_item( 
        #action="", 
        title="Finger Foods Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-wcbsOFoLD4w/AAAAAAAAAAI/AAAAAAAAAAA/tyUa8X2XtTI/s100-c-k-no/photo.jpg",
        folder=True ) 

    plugintools.add_item( 
        #action="", 
        title="Street Food",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-uN_mCvZ3KWg/AAAAAAAAAAI/AAAAAAAAAAA/XeTT3YSmtnQ/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Kabita's Kitchen",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-zDyCx20qJv8/AAAAAAAAAAI/AAAAAAAAAAA/WUSNccyFF-8/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Food Junction",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-2MIcBQu1Xn0/AAAAAAAAAAI/AAAAAAAAAAA/AAZFHHbALLk/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Buzzfeed Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/-iJJcDIkIjL0/AAAAAAAAAAI/AAAAAAAAAAA/Rf6VBJ2D-MA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="BuzzFeed Must Try Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/-GpCZ25vJ6CU/AAAAAAAAAAI/AAAAAAAAAAA/6qGF_ZTSSf0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Buzzfeed Food Hacks",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://yt3.ggpht.com/-qx3h-z3lc9w/AAAAAAAAAAI/AAAAAAAAAAA/QKFUBQtVG6A/s100-c-k-no/photo.jpg",
        folder=True )		

    plugintools.add_item( 
        #action="", 
        title="Diabetic Low-Carb Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/-tQR3Eg1svaw/AAAAAAAAAAI/AAAAAAAAAAA/8kMGGgAHinI/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Indian Diabetic Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/-nadO9YoAFPM/AAAAAAAAAAI/AAAAAAAAAAA/bwBIrMo8bl0/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Diabetic Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/-fWq_R-02uVo/AAAAAAAAAAI/AAAAAAAAAAA/lHhz7VZMmnI/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="healthy food for my diabetes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://yt3.ggpht.com/-92AYRSEyryQ/AAAAAAAAAAI/AAAAAAAAAAA/iY5RclZAtDA/s100-c-k-no/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Gluten Free Recipes",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/-xW77slWb5ac/AAAAAAAAAAI/AAAAAAAAAAA/6Xcf9ZZYf-o/s100-c-k-no/photo.jpg",
        folder=True )
run()
