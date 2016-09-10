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

YOUTUBE_CHANNEL_ID_1 = ""
YOUTUBE_CHANNEL_ID_2 = "PLrEnWoR732-CN09YykVof2lxdI3MLOZda"
YOUTUBE_CHANNEL_ID_3 = "PL1aRhDks3AaP48Vayjo0AXqgl1kcemvfj"
YOUTUBE_CHANNEL_ID_4 = "UCDUxOvbwu1bnyD7AucP0ESw"
YOUTUBE_CHANNEL_ID_5 = "OfficialChattyMan"
YOUTUBE_CHANNEL_ID_6 = "UCG7ez8nmq7ZyQJ3QHzNjW6Q"
YOUTUBE_CHANNEL_ID_7 = "UCb7IFajK_rUvahl8wzxNLQw"
YOUTUBE_CHANNEL_ID_8 = "UCGbofRROopWrumVob5w61OA"
YOUTUBE_CHANNEL_ID_9 = "CBSThisMorning"
YOUTUBE_CHANNEL_ID_10 = "PLlAiDifn-0o0AQ682tNKytEbdJQVXEy8S"
YOUTUBE_CHANNEL_ID_11 = "UC8GRXKNv9CyIq3T3xsYmEcg"
YOUTUBE_CHANNEL_ID_12 = "teamcoco"
YOUTUBE_CHANNEL_ID_13 = "UCMVlTv8EXJ2ZC-r6YCS1PIg"
YOUTUBE_CHANNEL_ID_14 = "UC18vz5hUUqxbGvym9ghtX_w"
YOUTUBE_CHANNEL_ID_15 = "UCH1oRy1dINbMVp3UFWrKP0w"
YOUTUBE_CHANNEL_ID_16 = "UCJPd6seu4JK4PZjVVTWb0QA"
YOUTUBE_CHANNEL_ID_17 = "JimmyKimmelLive"
YOUTUBE_CHANNEL_ID_18 = "UC3XTzVzaHQEd30rQbuvCtTQ"
YOUTUBE_CHANNEL_ID_19 = "LateNightSeth"
YOUTUBE_CHANNEL_ID_20 = "LIVEKellyandMichael"
YOUTUBE_CHANNEL_ID_21 = "UChJfh0Y4ycfMbf2SHQzRasg"
YOUTUBE_CHANNEL_ID_22 = "UC9MZOzmuhMnT7VkIyX-f-bw"
YOUTUBE_CHANNEL_ID_23 = "UCkZLcPd42ptm0XWyZMn1x3A"
YOUTUBE_CHANNEL_ID_24 = "UC864XQMCi4raTKsvWfJTq2A"
YOUTUBE_CHANNEL_ID_25 = "UCSNWs8T-h7Oqqa_reBivo1w"
YOUTUBE_CHANNEL_ID_26 = "UC9SUMV0oYm0XK9H-c3GmKaQ"
YOUTUBE_CHANNEL_ID_27 = "therachaelrayshowyt"
YOUTUBE_CHANNEL_ID_28 = "UC2qL1gQdXYsYop3JprivN4A"
YOUTUBE_CHANNEL_ID_29 = "UCiR-sCjJGDhhrRP-xzt_tgA"
YOUTUBE_CHANNEL_ID_30 = "SteveHarveyDaytime"
YOUTUBE_CHANNEL_ID_31 = "SteveWilkosNBC"
YOUTUBE_CHANNEL_ID_32 = "abcthechew"
YOUTUBE_CHANNEL_ID_33 = "UCwWhs_6x42TyRM4Wstoq8HA"
YOUTUBE_CHANNEL_ID_34 = "UCjH0RBT-7QhpSgLFnPLgD0Q"
YOUTUBE_CHANNEL_ID_35 = "DoctorOz"
YOUTUBE_CHANNEL_ID_36 = "UCYLR1ghzYNyvfjw78raCuxA"
YOUTUBE_CHANNEL_ID_37 = "TheEllenShow"
YOUTUBE_CHANNEL_ID_38 = "OfficialGrahamNorton"
YOUTUBE_CHANNEL_ID_39 = "UCq6W9je0X7mYG48Wu6BfLeA"
YOUTUBE_CHANNEL_ID_40 = "OfficialJonathanRoss"
YOUTUBE_CHANNEL_ID_41 = "UCJ0uqCI0Vqr2Rrt1HseGirg"
YOUTUBE_CHANNEL_ID_42 = "UCMtFAi84ehTSYSE9XoHefig"
YOUTUBE_CHANNEL_ID_43 = "UC4FBzTlkDF44xT0LiqnlA7Q"
YOUTUBE_CHANNEL_ID_44 = "TheRealDaytime"
YOUTUBE_CHANNEL_ID_45 = "UCSV8iMrDMdzc79kPCS9qucg"
YOUTUBE_CHANNEL_ID_46 = "UC8-Th83bH_thdKZDJCrn88g"
YOUTUBE_CHANNEL_ID_47 = "UCeH6qE4V7n5tVwP7NkdrtJg"
YOUTUBE_CHANNEL_ID_48 = "TODAYNBC"
YOUTUBE_CHANNEL_ID_49 = "levantatetelemundo"
YOUTUBE_CHANNEL_ID_50 = "Univision"
YOUTUBE_CHANNEL_ID_51 = "UCy6D16zE_mMEm1HVD20WFxA"
YOUTUBE_CHANNEL_ID_52 = "UCv7YFWATebnJ1ty4cwMKgsQ"
YOUTUBE_CHANNEL_ID_53 = "UCzlzGhKI5Y1LIeDJI53cWjQ"
YOUTUBE_CHANNEL_ID_54 = "UCD9jSZLsftoOACtkrDNZlsg"
YOUTUBE_CHANNEL_ID_55 = "PLMATWUx3t7L96rNjgH09sBMvtz4Gjrma9"
YOUTUBE_CHANNEL_ID_56 = "PL1aRhDks3AaMWIN2kv6vP7p5ibwEeFIGy"


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
        title="Report dead sources to: the.knife.repo@yandex.com",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="http://simpleicon.com/wp-content/uploads/mail-6.svg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Catch Up on Late Night",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://cdn.psychologytoday.com/sites/default/files/styles/article-inline-half/public/blogs/46501/2011/11/80110-70739.jpg?itok=SJi7vC5w",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="*Random Talk Show updates",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://www.theme-junkie.com/wp-content/uploads/2015/11/randomposts.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Al Rojo Vivo",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/-vPpIFdmssIU/AAAAAAAAAAI/AAAAAAAAAAA/WSbau3BkDOA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Alan Carr: Chatty Man",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://yt3.ggpht.com/-XGxuS4hwQ2w/AAAAAAAAAAI/AAAAAAAAAAA/nybJ7c-Mj2M/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Ballarò",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://yt3.ggpht.com/Ac3R_LH40eMB3bKgBxM78CXI2QQoNf6J6Z5A0LuHF-5mqhTmbQRNFKTAJPnKdjfSnfenWb-Tqh23Dw7Jyw=s900-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bill Cunningham Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://yt3.ggpht.com/-q4e_iMDX97Q/AAAAAAAAAAI/AAAAAAAAAAA/3VrRZdBUO2U/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Caso Cerrado",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://i.ytimg.com/vi/thU3ElkvmRM/hqdefault.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="CBS This Morning",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://yt3.ggpht.com/-5qz2CAFRDw8/AAAAAAAAAAI/AAAAAAAAAAA/aw0NkINOR5I/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Che tempo che fa",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://pbs.twimg.com/profile_images/721666293359894528/WSVn-KYU.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Como dice el dicho",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/-4E0LRFbeYRg/AAAAAAAAAAI/AAAAAAAAAAA/7KezHDev1rA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Conan",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://yt3.ggpht.com/-fl-1HlAzrrI/AAAAAAAAAAI/AAAAAAAAAAA/pYLiLlQWlTE/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Despierta América",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://yt3.ggpht.com/-zj2wr4xkjMs/AAAAAAAAAAI/AAAAAAAAAAA/Ll59HyiPDfs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Full Frontal with Samantha Bee",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://yt3.ggpht.com/-Y0J1h_dJYDM/AAAAAAAAAAI/AAAAAAAAAAA/8iyctPDKmL4/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Good Morning America",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://yt3.ggpht.com/-ZpKzkVykzf0/AAAAAAAAAAI/AAAAAAAAAAA/PPtEGe5Byss/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Hoy",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://yt3.ggpht.com/-DJUztvoL_TU/AAAAAAAAAAI/AAAAAAAAAAA/mMb0BKpic9c/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Jimmy Kimmel Live!",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://yt3.ggpht.com/-icjlceY943o/AAAAAAAAAAI/AAAAAAAAAAA/U0fuYSj5vJ0/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Last Week Tonight",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://yt3.ggpht.com/-lc3LinEhpgA/AAAAAAAAAAI/AAAAAAAAAAA/A6-FbtNyNgU/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Late Night with Seth Meyers",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://yt3.ggpht.com/-TI5ffZo0Qd4/AAAAAAAAAAI/AAAAAAAAAAA/glgeFHJ0Sto/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Live! with Kelly",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://yt3.ggpht.com/-e06tMwTq2dI/AAAAAAAAAAI/AAAAAAAAAAA/qlumVKbyPOg/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Loose Women",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://yt3.ggpht.com/--eQMueVRxyw/AAAAAAAAAAI/AAAAAAAAAAA/wudfwVtuiJ0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Omnibus",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://yt3.ggpht.com/ObSSv7_eWReRQu3z42ZqJsCnwGqmQzMmHBdcdOnGpWoMe_K1BmiY8M_VTcm6Ae28A-QAR2uTgovzw-ponW4=s900-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Piers Morgan's Life Stories",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://yt3.ggpht.com/ykxX93O0zToi3KXcTlqSr8Sgo1zOmKoMjVtm1dNq4fdfSCnxvPkryxdbS5fA5fqOD3DPeONIzerRl7C2=s900-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Pomeriggio Cinque",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://yt3.ggpht.com/kMBq1yyP4MKIe85GHi3iqWns2yc58Fux8FJGF54U9eVegeZtBy80uJPg3vxYwEgXJezhUdOS4ld9JMweaQ=s900-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Porta a Porta",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://yt3.ggpht.com/BUW34H7RbRNJBDwk4n8iUyIteGWGM-bTm7ki5M9crwxxeTMexZ3PCZWg6Wf5dnKDL3ushTVmZX6_IwIVww=s900-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Primer Impacto",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="https://yt3.ggpht.com/-AtXmlOS8-7Q/AAAAAAAAAAI/AAAAAAAAAAA/NAk-TE8cx48/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Rachael Ray Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://yt3.ggpht.com/-m05U72XlYFE/AAAAAAAAAAI/AAAAAAAAAAA/CkKiumzY7_g/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Real Time with Bill Maher",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://yt3.ggpht.com/-tbRHRuxcqwE/AAAAAAAAAAI/AAAAAAAAAAA/vrXiH3dsY1E/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="ShowsLive",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://yt3.ggpht.com/-K8DPjjjmksw/AAAAAAAAAAI/AAAAAAAAAAA/k0qsWx1SgQY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steve Harvey",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://yt3.ggpht.com/-uyA4fmFV_N4/AAAAAAAAAAI/AAAAAAAAAAA/dZ4I2dhmAU0/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Steve Wilkos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="https://yt3.ggpht.com/-YDr74H5pYfs/AAAAAAAAAAI/AAAAAAAAAAA/hGypsf2a-3k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Chew",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://i.ytimg.com/i/1aFHfIz3Al8lCeDIPbso9g/mq1.jpg?v=520bf2ec",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Daily Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://yt3.ggpht.com/-lYZk4150pXc/AAAAAAAAAAI/AAAAAAAAAAA/CR6MoHGaJiY/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Doctors",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://yt3.ggpht.com/-WfddzAW3Jh0/AAAAAAAAAAI/AAAAAAAAAAA/0jlanuIIL28/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Dr. Oz Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://yt3.ggpht.com/-wUFAO6VDNR0/AAAAAAAAAAI/AAAAAAAAAAA/Eu-a0dQaVxU/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True ) 	

    plugintools.add_item( 
        #action="", 
        title="The Dr. Phil Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://yt3.ggpht.com/-w2L71mwv0ro/AAAAAAAAAAI/AAAAAAAAAAA/t1dyzaEsj_Q/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Ellen DeGeneres Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://yt3.ggpht.com/-dDZUkj9sY4g/AAAAAAAAAAI/AAAAAAAAAAA/oy6dm2Uy8dc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Graham Norton Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://yt3.ggpht.com/-jx04VEy8uP8/AAAAAAAAAAI/AAAAAAAAAAA/29F8o6LixXY/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Jeremy Kyle Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://yt3.ggpht.com/-R1kJSKCoORo/AAAAAAAAAAI/AAAAAAAAAAA/z7saWnNh4hk/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Jonathan Ross Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://yt3.ggpht.com/-15zT89idIJ4/AAAAAAAAAAI/AAAAAAAAAAA/OPpNuO_cvds/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Late Late Show with James Corden",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://yt3.ggpht.com/-NhxJe9XKyV8/AAAAAAAAAAI/AAAAAAAAAAA/XkSb5PFaHP8/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Late Show with Stephen Colbert",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://yt3.ggpht.com/-_DMSPt1vZaw/AAAAAAAAAAI/AAAAAAAAAAA/sSVARCDuXwE/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Marilyn Denis Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://yt3.ggpht.com/Ed2gOWLmH3_FTQI6ZEJkIHoUnrD2qAPJhp7erZs9Ok604B-mRyoBmSMQBy5bqcJarNxfgqQ4fOAGsrOr=s900-nd-c-c0xffffffff-rj-k-no",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Real Daytime",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://yt3.ggpht.com/-iTkqPnbTS4w/AAAAAAAAAAI/AAAAAAAAAAA/I8LL8kiBk0Y/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Talk",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://yt3.ggpht.com/-vmhYyZDl_00/AAAAAAAAAAI/AAAAAAAAAAA/2I357wOEcME/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The Tonight Show Starring Jimmy Fallon",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://yt3.ggpht.com/-x3CU1CXklQI/AAAAAAAAAAI/AAAAAAAAAAA/jPQ9GJeU53g/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="The View",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://yt3.ggpht.com/-jn7rThGotIc/AAAAAAAAAAI/AAAAAAAAAAA/LnxMsxRV3Aw/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Today Show",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="https://yt3.ggpht.com/-S0Lj4ll3_mU/AAAAAAAAAAI/AAAAAAAAAAA/MEdajoo_Ozo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Un Nuevo Día",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://yt3.ggpht.com/-mNI4JGNffnY/AAAAAAAAAAI/AAAAAAAAAAA/c4_bg56iEvk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Univision",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://yt3.ggpht.com/-qcqUmE_igSs/AAAAAAAAAAI/AAAAAAAAAAA/BVF8n2ocgwQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="WWHL Clubhouse!",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://yt3.ggpht.com/-9JqDKNPEBC0/AAAAAAAAAAI/AAAAAAAAAAA/7vLBitY2_X8/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wendy Williams",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://yt3.ggpht.com/-aD3C8Na9GBc/AAAAAAAAAAI/AAAAAAAAAAA/0vfNeTUGYZI/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Вечерний Ургант",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://yt3.ggpht.com/-srYNR2jQ3pQ/AAAAAAAAAAI/AAAAAAAAAAA/n5DlxfDINrw/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Пусть говорят",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://yt3.ggpht.com/-vZcdwQSG91o/AAAAAAAAAAI/AAAAAAAAAAA/ED4KttisIzo/s900-c-k-no-rj-c0xffffff/photo.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Top 200 Popular Talk Shows",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="http://ewweb.com/site-files/ewweb.com/files/Top-200-cover-logo-on-black.jpg",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Videos Auto-generated by YouTube",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="http://www.adweek.com/socialtimes/wp-content/uploads/sites/2/2011/04/YouTube-Search.jpg",
        folder=True )

run()
