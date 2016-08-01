# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Talk Show Addon by The Knife.
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

addonID = 'plugin.video.talkshow'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UCGbofRROopWrumVob5w61OA"
YOUTUBE_CHANNEL_ID_2 = "teamcoco"
YOUTUBE_CHANNEL_ID_3 = "UC18vz5hUUqxbGvym9ghtX_w"
YOUTUBE_CHANNEL_ID_4 = "JimmyKimmelLive"
YOUTUBE_CHANNEL_ID_5 = "UCVQSnAUlAPllc-VtYG3H7Eg"
YOUTUBE_CHANNEL_ID_6 = "UC3XTzVzaHQEd30rQbuvCtTQ"
YOUTUBE_CHANNEL_ID_7 = "LateNightSeth"
YOUTUBE_CHANNEL_ID_8 = "UCMKvYnuiz1rhzcGNor7_s8w"
YOUTUBE_CHANNEL_ID_9 = "UC2qL1gQdXYsYop3JprivN4A"
YOUTUBE_CHANNEL_ID_10 = "abcthechew"
YOUTUBE_CHANNEL_ID_11 = "UCwWhs_6x42TyRM4Wstoq8HA"
YOUTUBE_CHANNEL_ID_12 = "UCjH0RBT-7QhpSgLFnPLgD0Q"
YOUTUBE_CHANNEL_ID_13 = "DoctorOz"
YOUTUBE_CHANNEL_ID_14 = "UCYLR1ghzYNyvfjw78raCuxA"
YOUTUBE_CHANNEL_ID_15 = "TheEllenShow"
YOUTUBE_CHANNEL_ID_16 = "OfficialGrahamNorton"
YOUTUBE_CHANNEL_ID_17 = "UCq6W9je0X7mYG48Wu6BfLeA"
YOUTUBE_CHANNEL_ID_18 = "UCJ0uqCI0Vqr2Rrt1HseGirg"
YOUTUBE_CHANNEL_ID_19 = "UCMtFAi84ehTSYSE9XoHefig"
YOUTUBE_CHANNEL_ID_20 = "TheRealDaytime"
YOUTUBE_CHANNEL_ID_21 = "UCSV8iMrDMdzc79kPCS9qucg"
YOUTUBE_CHANNEL_ID_22 = "UC8-Th83bH_thdKZDJCrn88g"
YOUTUBE_CHANNEL_ID_23 = "UCeH6qE4V7n5tVwP7NkdrtJg"
YOUTUBE_CHANNEL_ID_24 = "UCy6D16zE_mMEm1HVD20WFxA"
YOUTUBE_CHANNEL_ID_25 = "UCv7YFWATebnJ1ty4cwMKgsQ"
YOUTUBE_CHANNEL_ID_26 = "UCzlzGhKI5Y1LIeDJI53cWjQ"
YOUTUBE_CHANNEL_ID_27 = "UCD9jSZLsftoOACtkrDNZlsg"

# Entry point
def run():
    plugintools.log("talkshow.run")
    
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
        title="Caso Cerrado",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://i.ytimg.com/vi/thU3ElkvmRM/hqdefault.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Conan",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/-fl-1HlAzrrI/AAAAAAAAAAI/AAAAAAAAAAA/pYLiLlQWlTE/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Full Frontal with Samantha Bee",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/-Y0J1h_dJYDM/AAAAAAAAAAI/AAAAAAAAAAA/8iyctPDKmL4/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Jimmy Kimmel Live!",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/clIWfe8-ebj1X8KZYzGpabffEBemGFeV7pVXYwsbZK3rGPrOlADUQoE6efQI94_G1eaJJDpZnlNsQbOhfdc=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Kocktails with Khloé",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/29yplDyeby0YOgm0WdsSCqAFQUDkFcTO_NGL-p5xAWl01Ae25koPvbg8KoMXA00vX_wZ2oxDKKJjaU1Rzg=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Last Week Tonight",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/c-c1ulSouKl7WfNb5iw4-nQzkULaPp0jl9y7rpuPF0QGDtJ-D2z7Rm4vXjLvW1xc00oQhv8bSu__grOl=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Late Night with Seth Meyers",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-TI5ffZo0Qd4/AAAAAAAAAAI/AAAAAAAAAAA/glgeFHJ0Sto/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Live! with Kelly",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://yt3.ggpht.com/-bg3RnPykslKwxZZWtkBGlhuD5Nghfu6d6a4Q58dUvOBrAyoQST8iqzIyuCi0HdvFdJKi-AhLJBOTy1SEQ=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Real Time with Bill Maher",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/e2Lrr2bkkjFh7GTtImatIxYllxcPLLglfvaZdFhFN2T7SEnlLGAOC1-9mQc8QpySoQ7Fa7yOYWc7y9BxcA=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Chew",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/vjEBN41ZOCDPr4xNssfH5q3nCmsYuJNMVmKB7m46AgXVaLj6ieCECcUZxUMED_lZ19pgsKLJWT9D0Yxo8A=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Daily Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-lYZk4150pXc/AAAAAAAAAAI/AAAAAAAAAAA/CR6MoHGaJiY/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Doctors",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-WfddzAW3Jh0/AAAAAAAAAAI/AAAAAAAAAAA/0jlanuIIL28/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Dr. Oz Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/UL3oCYaftN3oeOYgcjADqW1z9rTUjVlUb4vkZ6LZM8PUnHMcKXr9F520JTcfoOJwlkfVhmUvM3wEBPSHZQ=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="The Dr. Phil Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/smo4uDQof0NXz5DxU4l7jhE3zR5OY164pBDIF4SKWaxJxi8KrhkDXO77NEmTWVmFe6bRKw1bNbw8Kn9iuA=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Ellen DeGeneres Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/SEy0ohRjqKBtQmcIctOg-BGS876V4xHtScf5rcw12zq7aiQ0vNrMnSJThPq1D_a_lNqPvi6pzEsD92L5=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Graham Norton Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/UbA9aHwuOuoMgyxyC2HwQpffXdxfNfV1VfcLdjbPKYIfuJsO4FDNpRyBEt81TktMBCWym-LbugKL2k3guQ=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Jeremy Kyle Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-R1kJSKCoORo/AAAAAAAAAAI/AAAAAAAAAAA/z7saWnNh4hk/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Late Late Show with James Corden",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-NhxJe9XKyV8/AAAAAAAAAAI/AAAAAAAAAAA/XkSb5PFaHP8/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Late Show with Stephen Colbert",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/y7kpUEahrAPW4gtdi7sfyEaQJzDwfdYEsAUEbiKLVXMtCFLqeysfnT5fcOUoqWwvCwfRvCnEz3U9tI91ng=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="The Real Daytime",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/2ohh7BVYEfDf3dtHXvhPxHcasELTij60nRXt8ZPdPkjH3FU3Nl1bmO-Ki2YcCqFJYNvDtVt7jQ8AbOQH=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Talk",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/3C6BthQyKZ9NvtwSYdMRU8g_eFt8sCcc0aBBvzbB08Uy_WLQqQWu_tYlu6WFciSMRRZ4CuCt64KEc5PDoA=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Tonight Show Starring Jimmy Fallon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/yJAkoYZIlb5u_pfg24cxJ1KxC3mD4Yqjd16W2JbzRLqs7LbwwxK-003qlMd7RktjHN5ORhAXQQAqSV6-=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The View",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/7z5pzHKzGvyhD3LMHKhKk6N9QqoZkFejpv4UbtCXYd8mgKIk2W0Gg_xiu8veWOjM6qFY0EvhSJxv6xLeKSQ=s100-nd-c-c0xffffffff-rj-k-no",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="WWHL Clubhouse!",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/-9JqDKNPEBC0/AAAAAAAAAAI/AAAAAAAAAAA/7vLBitY2_X8/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Wendy Williams",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/-aD3C8Na9GBc/AAAAAAAAAAI/AAAAAAAAAAA/0vfNeTUGYZI/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Вечерний Ургант",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-srYNR2jQ3pQ/AAAAAAAAAAI/AAAAAAAAAAA/n5DlxfDINrw/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Пусть говорят",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-vZcdwQSG91o/AAAAAAAAAAI/AAAAAAAAAAA/ED4KttisIzo/s100-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True ) 			
              		
run()
