# UK Expat Radio
# We do not own or publish the content delivered by the plugin
# streaming UK radio

import sys
import xbmcgui
import xbmcplugin
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://sc6.radiocaroline.net:8040/listen.pls'
li = xbmcgui.ListItem('[COLOR red][B]Radio Caroline[/B][/COLOR] >>', iconImage='https://www.phonostar.de/images/auto_created/radio_caroline124x124.png', thumbnailImage= 'https://www.phonostar.de/images/auto_created/radio_caroline124x124.png')
li.setProperty('fanart_image', 'http://www.enuu93.plus.com/images/memories_3/caroline319sticker.JPG?resize=981%2C552')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://media-ice.musicradio.com/GoldMP3.m3u'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Gold Radio[/B][/COLOR] >>', iconImage='http://d1i6vahw24eb07.cloudfront.net/s110055q.png', thumbnailImage= 'http://d1i6vahw24eb07.cloudfront.net/s110055q.png')
li.setProperty('fanart_image', 'http://wallpaperfx.com/view_image/queen-figures-1920x1080-wallpaper-9172.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://icy-e-bz-04-cr.sharp-stream.com:8000/planetrock.mp3'
li = xbmcgui.ListItem('[COLOR red][B]Planet Rock[/B][/COLOR] >>', iconImage='http://www.liveradio.ie/files/images/105152/resized/180x172c/planet_rock.jpg', thumbnailImage= 'http://www.liveradio.ie/files/images/105152/resized/180x172c/planet_rock.jpg')
li.setProperty('fanart_image', 'http://images7.alphacoders.com/308/308507.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://media-sov.musicradio.com:80/HeartUKMP3'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Heart[/B][/COLOR] >>', iconImage='http://www.iqbeatsblog.com/wp-content/uploads/2012/04/HeartLogo.jpg', thumbnailImage= 'http://www.iqbeatsblog.com/wp-content/uploads/2012/04/HeartLogo.jpg')
li.setProperty('fanart_image', 'http://freewallshd.com/wp-content/uploads/2014/05/2795_queen_band.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://50.7.129.122:8372/listen.pls'
li = xbmcgui.ListItem('[COLOR red][B]Glam FM[/B][/COLOR] >>', iconImage='https://fbcdn-profile-a.akamaihd.net/hprofile-ak-prn1/t5/50513_52649132555_7994406_n.jpg', thumbnailImage= 'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-prn1/t5/50513_52649132555_7994406_n.jpg')
li.setProperty('fanart_image', 'http://3.bp.blogspot.com/-l7avs1ELr-M/TvS9jrtq1kI/AAAAAAAABJY/MCPXfID3-Es/s1600/Slade-001.jpg?resize=981%2C552')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://djcmedia.com/stations/hrhradio/listen.m3u'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Hard Rock Heaven[/B][/COLOR] >>', iconImage='http://www.streamfinder.com/listing-logos/30116_logo.jpg', thumbnailImage= 'http://www.streamfinder.com/listing-logos/30116_logo.jpg')
li.setProperty('fanart_image', 'https://lh5.ggpht.com/3aMW69YuEXZkY0gpjMUO3hk0thhVH_ZfdyGMCCcfUXhRe9MOhq65rKHeMI9Crgn7bA=h900?resize=981%2C552')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://icy-e-bz-04-cr.sharp-stream.com:8000/magic1054.mp3'
li = xbmcgui.ListItem('[COLOR red][B]Magic[/B][/COLOR] >>', iconImage='http://my.magic.co.uk/playlist/cache/default4.jpg', thumbnailImage= 'http://my.magic.co.uk/playlist/cache/default4.jpg')
li.setProperty('fanart_image', 'http://cdn.superbwallpapers.com/wallpapers/music/michael-jackson-24873-1920x1080.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://icy-e-bl-02-gos.sharp-stream.com:8000/kerrang.mp3'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Kerrang Radio[/B][/COLOR] >>', iconImage='https://pbs.twimg.com/profile_images/1400401344/kerrang_twitter.jpg', thumbnailImage= 'https://pbs.twimg.com/profile_images/1400401344/kerrang_twitter.jpg')
li.setProperty('fanart_image', 'http://images2.alphacoders.com/199/199660.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://icy-e-ba-05-cr.sharp-stream.com:8000/kissnational.mp3'
li = xbmcgui.ListItem('[COLOR red][B]Kiss FM[/B][/COLOR] >>', iconImage='http://i.img.co/radio/60/10/160_290.png', thumbnailImage= 'http://i.img.co/radio/60/10/160_290.png')
li.setProperty('fanart_image', 'http://www.betaarchive.co.uk/imageupload/1283877178.or.61533.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://media-sov.musicradio.com:80/CapitalUKMP3'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Capital[/B][/COLOR] >>', iconImage='http://www.christianw.co.uk/wp-content/uploads/2013/10/CapitalFMLogo.png', thumbnailImage= 'http://www.christianw.co.uk/wp-content/uploads/2013/10/CapitalFMLogo.png')
li.setProperty('fanart_image', 'http://coolpcwallpapers.com/wp-content/uploads/2015/03/Music-Taylor-Swift-Best-Wallpaper-1920x1080.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://icecast.timlradio.co.uk:80/ar128.mp3'
li = xbmcgui.ListItem('[COLOR red][B]Absolute Radio[/B][/COLOR] >>', iconImage='https://lh5.ggpht.com/rEbHerdT1Jh8tWuKZly3Qi9N5Tox-Ix7xxMhigS-sfPgeDBF9bd93KkXsovwR5BuFMM=w170', thumbnailImage= 'https://lh5.ggpht.com/rEbHerdT1Jh8tWuKZly3Qi9N5Tox-Ix7xxMhigS-sfPgeDBF9bd93KkXsovwR5BuFMM=w170')
li.setProperty('fanart_image', 'http://www.techagesite.com/desktop-wallpapers/radio-waves-background-for-desktop-full-hd-1920x1080.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://icecast.timlradio.co.uk:80/a8128.mp3'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Absolute 80s[/B][/COLOR] >>', iconImage='https://kajafax.files.wordpress.com/2011/05/absolute2080s20logo.jpg', thumbnailImage= 'https://kajafax.files.wordpress.com/2011/05/absolute2080s20logo.jpg')
li.setProperty('fanart_image', 'http://rockstarwallpapers10.net/wp-content/uploads/images/13/status-quo-0.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://icecast.timlradio.co.uk:80/a9128.mp3'
li = xbmcgui.ListItem('[COLOR red][B]Absolute 90s[/B][/COLOR] >>', iconImage='http://cdn.marketplaceimages.windowsphone.com/v8/images/586287a9-6cb8-4b8a-b06e-79f7c58622ad?imageType=ws_icon_large', thumbnailImage= 'http://cdn.marketplaceimages.windowsphone.com/v8/images/586287a9-6cb8-4b8a-b06e-79f7c58622ad?imageType=ws_icon_large')
li.setProperty('fanart_image', 'http://www.kewlwallpapers.com/images/1920x1080/Spice%20Girls%2004.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://adsi-e-02-boh.sharp-stream.com/jazzfmmobile.mp3'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]Jazz FM[/B][/COLOR] >>', iconImage='https://pbs.twimg.com/profile_images/1187114839/Jazz_FM_Logo_SMALL__57328FC_400x400.jpg', thumbnailImage= 'https://pbs.twimg.com/profile_images/1187114839/Jazz_FM_Logo_SMALL__57328FC_400x400.jpg')
li.setProperty('fanart_image', 'http://conversationsabouther.net/wp-content/uploads/2015/05/amy-winehouse.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://media-sov.musicradio.com:80/SmoothExtraMP3'
li = xbmcgui.ListItem('[COLOR red][B]Smooth Extra[/B][/COLOR] >>', iconImage='http://www.listenradios.com/wp-content/uploads/2012/01/Smooth-Radio-Logo.png', thumbnailImage= 'http://www.listenradios.com/wp-content/uploads/2012/01/Smooth-Radio-Logo.png')
li.setProperty('fanart_image', 'http://img.cache.vevo.com/Content/VevoImages/video/52C9F5EB1CDFA3CFA49E4087DD1C1E37.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_q?s=1444861706&e=1444876106&h=fa502f197bfc9ac005532c68192462ad'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]BBC Radio One[/B][/COLOR] >>', iconImage='https://johannesdujsik.files.wordpress.com/2010/11/bbc-radio-1-logo.jpg', thumbnailImage= 'https://johannesdujsik.files.wordpress.com/2010/11/bbc-radio-1-logo.jpg')
li.setProperty('fanart_image', 'http://p1.pichost.me/i/46/1700496.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1xtra_mf_q?s=1444863218&e=1444877618&h=210fd2c55b541a73e3b3a06207b28169'
li = xbmcgui.ListItem('[COLOR red][B]BBC 1Extra[/B][/COLOR] >>', iconImage='http://i2.cdnds.net/broadcasting/library/160x120_logo_radio_bbc_1xtra_white.jpg', thumbnailImage= 'http://i2.cdnds.net/broadcasting/library/160x120_logo_radio_bbc_1xtra_white.jpg')
li.setProperty('fanart_image', 'https://larrygifford.files.wordpress.com/2013/08/broken_radio_mess_1920x1080_33254.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://www.listenlive.eu/bbcradio2.m3u'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]BBC Radio Two[/B][/COLOR] >>', iconImage='http://img2.wikia.nocookie.net/__cb20091201155447/logopedia/images/thumb/5/56/BBC_Radio_2_logo_90s.png/200px-BBC_Radio_2_logo_90s.png', thumbnailImage= 'http://img2.wikia.nocookie.net/__cb20091201155447/logopedia/images/thumb/5/56/BBC_Radio_2_logo_90s.png/200px-BBC_Radio_2_logo_90s.png')
li.setProperty('fanart_image', 'http://p1.pichost.me/i/55/1785624.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://www.listenlive.eu/bbcradio3.m3u'
li = xbmcgui.ListItem('[COLOR red][B]BBC Radio Three[/B][/COLOR] >>', iconImage='http://static4.wikia.nocookie.net/__cb20130215164726/logopedia/images/8/8b/Bbcradio3.png', thumbnailImage= 'http://static4.wikia.nocookie.net/__cb20130215164726/logopedia/images/8/8b/Bbcradio3.png')
li.setProperty('fanart_image', 'https://wallpaperscraft.com/image/london_philharmonic_orchestra_scene_show_play_conductor_8925_1920x1080.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio4fm_mf_q?s=1444862534&e=1444876934&h=a69b75c7c7ef48566d78a7ea3fbab907'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]BBC Radio Four[/B][/COLOR] >>', iconImage='http://www.bbc.co.uk/cornwall/content/images/2007/01/10/radio4_203_203x152.jpg', thumbnailImage= 'http://www.bbc.co.uk/cornwall/content/images/2007/01/10/radio4_203_203x152.jpg')
li.setProperty('fanart_image', 'http://cdn.desktopwallpapers4.me/wallpapers/music/1920x1080/1/6781-microphone-and-monitors-1920x1080-music-wallpaper.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://www.listenlive.eu/bbc5live.m3u'
li = xbmcgui.ListItem('[COLOR red][B]BBC Five Live[/B][/COLOR] >>', iconImage='http://news.bbc.co.uk/nol/shared/spl/hi/newswatch/history/img/1991_radio_fivelive.jpg', thumbnailImage= 'http://news.bbc.co.uk/nol/shared/spl/hi/newswatch/history/img/1991_radio_fivelive.jpg')
li.setProperty('fanart_image', 'http://gonedigital.net/wp-content/uploads/HD-Testcard-original.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://www.listenlive.eu/bbc5liveextra.m3u'
li = xbmcgui.ListItem('[COLOR deepskyblue][B]BBC Five Live Extra[/B][/COLOR] >>', iconImage='https://upload.wikimedia.org/wikipedia/commons/7/76/Bbc_radio_five_live_sports_extra_old.jpg', thumbnailImage= 'https://upload.wikimedia.org/wikipedia/commons/7/76/Bbc_radio_five_live_sports_extra_old.jpg')
li.setProperty('fanart_image', 'http://img0.cfstatic.com/wallpapers/a1154166491c63aec5e6e75a1bbc9e7d_large.jpeg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
 
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'audio')
url = 'http://www.listenlive.eu/bbc6music.m3u'
li = xbmcgui.ListItem('[COLOR red][B]BBC Six Music[/B][/COLOR] >>', iconImage='http://www.bbc.co.uk/6music/news/media/6-logo205.jpg', thumbnailImage= 'http://www.bbc.co.uk/6music/news/media/6-logo205.jpg')
li.setProperty('fanart_image', 'http://www.htbackdrops.org/v2/albums/userpics/12172/orig_band_live-3a.jpg')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)

