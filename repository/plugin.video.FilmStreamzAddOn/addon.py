import requests
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import codecs
import urllib
from urlparse import parse_qsl
import re
import sys
import urlresolver
import xbmcaddon   # info
import xbmcgui     # play
import xbmcplugin  # diritem/
 

# -*- coding: utf-8 -*-
reload(sys)
sys.setdefaultencoding('utf-8')

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
txt = "hanswurst"
strLastSearch = "big game"
#get actioncodes from https://github.com/xbmc/xbmc/blob/master/xbmc/guilib/Key.h
ACTION_PREVIOUS_MENU = 10
ACTION_SELECT_ITEM   =  7

class textbox(xbmcgui.Window):
    txt = "test"
    def __init__(self):
        self.strActionInfoBox = xbmcgui.ControlTextBox(300, 120, 600, 600, 'font13', '0xFFFFFFFA')
        self.addControl(self.strActionInfoBox)
        self.strActionInfoBox.setText(txt)        

        self.strActionInfo = xbmcgui.ControlLabel(300, 500, 400, 200, '', 'font13', '0xFFAFAFAF')
        self.addControl(self.strActionInfo)
        self.strActionInfo.setLabel('zurueck (ESC)')

        self.strActionFade = xbmcgui.ControlFadeLabel(350, 50, 200, 200, 'font18', '0xFFAFAFAF')
        self.addControl(self.strActionFade)
        self.strActionFade.addLabel('Beschreibung')

    def settext(self, paramTxt):
        global txt
        self.txt = paramTxt
        self.strActionInfoBox.setText(paramTxt)
        #self.strActionInfo.setLabel(paramTxt)
        #print(paramTxt)
    def onAction(self, action):
        if action == ACTION_PREVIOUS_MENU:
            self.close()
        if action == ACTION_SELECT_ITEM:
            #self.strAction = xbmcgui.ControlLabel(300,200,200,200, "txt", "font14", "0xFF00FF00")
            #self.addControl(strAction)
            #self.strAction.setLabel("Hello World")
            self.strActionFade.reset()
 
#line1 = "Hello World!"
#line2 = "We can write anything we want here"
#line3 = "Using Python"
 
#xbmcgui.Dialog().ok(addonname, line1, line2, line3)
"""
r = requests.get("http://www.yellowpages.com/search?search_terms=coffee&geo_location_terms=newyork")
soup = BeautifulSoup(r.content)

g_data = soup.findAll("div", {"class":"info"})

for item in g_data:
    xbmcgui.Dialog().ok(addonname,
                        str(item.contents),
                        "",
                        "Hello World"
                        )
    break

xbmcgui.Dialog().ok(sys.platform,
                    sys.prefix,
                    sys.version,
                    sys.winver)


#hostUrl = "http://www.rapidvideo.com/view/iq0hqw26"
hostUrl = "http://beta.vidup.me/embed-y47ezftvhoy5-620x330.html"
videoLink = urlresolver.resolve(hostUrl)
# videoLink = decode_htmlentities(videoLink)
# videoLink -> http://46.4.78.201/f0/c47edb45c7b17ea101322ba531817485/50067006/6/mp4/5ryzwM1309081242.mp4

#xbmcgui.Dialog().ok(addonname, hostUrl, videoLink, "")
# play mv
#xbmc.Player().play(videoLink)

"""

# suchen
# alle f a-z
# sort wertung
# sort quali
# sort jahr
# sort datum



# suchen: http://www.filme-streamz.com/s/inception-stream-deutch-online-anschauen-p1.html
#         http://www.filme-streamz.com/s/ ###suchstring### -stream-deutch-online-anschauen-p1.html

# link zum F:
"""
<a href="/film/512/Inception-stream.html" title="Inception stream - film stream">
<div class="list_film">
<img src="http://www.filme-streamz.com/photos/54 e94e3ea99aed53e5889e4b166b7b012e23785952.jpg" width="216" height="320" alt="Inception stream - film stream" title="Inception im stream - film stream" class="scale-with-grid">
<h3 class="" style="" onclick="window.location = '/film/512/Inception-stream.html'">Inception (2010) - DVDRIP</h3>
</div>
</a>
"""

# Get the plugin url in plugin:// notation.
if 1 <= sys.argv:
    __url__ = sys.argv[0]
    
# Get the plugin handle as an integer number.
if 2 <= sys.argv:
    __handle__ = int(sys.argv[1])


# suchen
def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    :return: None
    """
    # Get video categories
    categories = ["search", "all", "year"]
    # Create a list for our items.
    listing = []
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category, thumbnailImage='http://www.vidsplay.com/vids/crab.jpg')
        # Set a fanart image for the list item.
        # Here we use the same image as the thumbnail for simplicity's sake.
        list_item.setProperty('fanart_image', 'http://www.vidsplay.com/vids/alligator.jpg')
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = '{0}?action=listing&category={1}'.format(__url__, category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))

    # most recent added:
    req = requests.get("http://www.filme-streamz.com/")
    soup = BeautifulSoup(req.content, "html.parser")

    overv = soup.find("ul", {"class":"overview"})
    for li in overv.findAll("li"):
        href = "http://www.filme-streamz.com"
        href += li.find("a")["href"]
        title = str(re.findall("\d/.+-stream", href)).replace("-stream", "")
        title = str(re.split("/", title, 1)[1])
        title = title.replace("']", "")
        #print(title)
        title = urllib.unquote(urllib.unquote(title))
        title = urllib.unquote_plus(urllib.unquote_plus(title))
        
        #print(title)
        #print(href)
        #print(li.find("img")["src"])
        list_item = xbmcgui.ListItem(label=title, thumbnailImage=li.find("img")["src"])
        list_item.setProperty('fanart_image', 'http://www.vidsplay.com/vids/alligator.jpg')
        list_item.setInfo('video', {'title': title, 'genre': "most recent"})
        url = '{0}?action=detail&url={1}'.format(__url__, href)
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))
    

    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    #xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_NONE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(__handle__)

# suchen: http://www.filme-streamz.com/s/inception-stream-deutch-online-anschauen-p1.html
#         http://www.filme-streamz.com/s/ ###suchstring### -stream-deutch-online-anschauen-p1.html
def dialog_search():
    global strLastSearch
    # Create a list for our items.
    listing = []

    keyboard = xbmc.Keyboard(strLastSearch)
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        strLastSearch = keyboard.getText()
        #xbmcgui.Dialog().ok("Keyb Input:", strLastSearch, "", "")
    else:
        xbmcgui.Dialog().ok("Keyb Input:", "canceled", "", "")
    req = requests.get("http://www.filme-streamz.com/s/%s-stream-deutch-online-anschauen-p1.html"%strLastSearch)
    #xbmcgui.Dialog().ok("Keyb Input:", "", req.content, "")
    #print(req.content)
    soup = BeautifulSoup(req.content)

    i = 0
    anc = ""
    img = ""
    text = ""

    g_data = soup.findAll("li", {"class", "imgborder"})
    for item in g_data:
        i = i + 1
        #print(i, " ", item, " tagname:", item.name)#, " Text:", item.getText())
        #print(item.findAll("li", {"class","imgborder"}))
        tag = item.findNext("a")
        #print(tag)
        #print("http://www.filme-streamz.com" + tag["href"])
        anc ="http://www.filme-streamz.com"
        anc += str(tag["href"])
        tag = item.findNext("img")
        #print(tag)
        try:
            #print(tag["src"].encode("ascii", "ignore").decode("utf-8"))
            img = tag["src"].encode("ascii", "ignore").decode("utf-8")
        except:
            print("dialog_search fehler: tag[src] anc:" + anc)
        tag = item.findNext("h3")
        #text = str(repr(tag.text)) #.strip(codecs.BOM_UTF8), 'utf-8') #.encode(sys.stdout.encoding, 'replace') #.encode("utf-8", "ignore").decode("utf-8")
        text = tag.text.encode("ascii", "ignore").decode("utf-8")
        #print(text)
        #print("\r\n------------\r\n")
        #print("\r\n")
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=text, thumbnailImage=img)
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': text, 'url': anc})
        # Create a URL for the plugin recursive callback.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = '{0}?action=detail&url={1}'.format(__url__, anc)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the listing as a 3-element tuple.
        listing.append((url, list_item, is_folder))

    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(__handle__)
    
    #xbmcgui.Dialog().ok(soup.text, strLastSearch, "", "")
    

def dialog_detail(paramURL):
    # Create a list for our items.
    listing = []
    img = "http://www.filme-streamz.com"
    req = requests.get(paramURL) #"http://www.filme-streamz.com/film/2128/Batman+Forever-stream.html")
    soup = BeautifulSoup(req.content)
    text = ""

    g_data = soup.find("div", {"class":"padcontent"})
    #print(g_data)

    tag = g_data.find_next("h3")
    text = tag.text
    #print(tag.text)
    tag = g_data.find_next("img", {"itemprop":"thumbnailUrl"})
    img = tag["src"]
    #print(tag["src"])
    # Create a list item with a text label and a thumbnail image.
    list_item = xbmcgui.ListItem(label=text, thumbnailImage=tag["src"])
    list_item.setInfo('video', {'title': text, 'url': tag["src"]})
    url = '{0}?action=headline&url={1}'.format(__url__, tag["src"])
    is_folder = False
    listing.append((url, list_item, is_folder))

    tag = g_data.find_next("p")
    child = tag.findNext("span", {"itemprop":"director"})
    child = child.findNext("span", {"itemprop":"name"})
    text = re.sub("\n", "", child.text)
    list_item = xbmcgui.ListItem(label=text, thumbnailImage=img)
    url = '{0}?action=director&text={1}'.format(__url__, text)
    listing.append((url, list_item, is_folder))
    #print("director:" + child.text)
    child = tag.findNext("span", {"itemprop":"actor"})
    child = child.findNext("span", {"itemprop":"name"})
    text = re.sub("\n", "", child.text)
    list_item = xbmcgui.ListItem(label=text, thumbnailImage=img)
    url = '{0}?action=description&text={1}'.format(__url__, str(text))
    listing.append((url, list_item, is_folder))
    #print("actor:" + child.text)
    child = tag.findNext("span", {"itemprop":"genre"})
    text = re.sub("\n", "", child.text)
    list_item = xbmcgui.ListItem(label=text, thumbnailImage=img)
    url = '{0}?action=genre&text={1}'.format(__url__, str(text))
    listing.append((url, list_item, is_folder))
    #print("genre:" + child.text)
    child = child.findNext("span")
    text = re.sub("\n", "", child.text)
    list_item = xbmcgui.ListItem(label=text, thumbnailImage=img)
    url = '{0}?action=country&text={1}'.format(__url__, str(text))
    listing.append((url, list_item, is_folder))
    #print("country:" + child.text.encode("ascii", "ignore").decode("utf-8"))
    tag = g_data.find("p", {"itemprop":"description"})
    #print("descr: " + str(tag.text))
    text = re.sub("\n", "", tag.text)
    list_item = xbmcgui.ListItem(label=text, thumbnailImage=img)
    url = '{0}?action=description&text={1}'.format(__url__, text)
    is_folder = False
    listing.append((url, list_item, is_folder))
    #print("descr.:" + tag.text.encode("ascii", "ignore").decode("utf-8"))
    #print("\r\n1-click-hoster\r\n")
    for item in g_data.findAll("a", {"target":"videoPlayer"}):
        s = item["href"]
        #name = str(re.findall("//\w.*[\w].+\w/", s))
        print(s)
        name = re.findall("[\w]+\.[\w]+/", s)
        if 0<len(name):
            name = name[0]
            print("name = re.findall([\w]+\.[\w]+/, name)[0]")
            print(name)
            name = re.split("\.", name, 1)[0]
            print(name)
        else:
            continue

        name = str(name)
        img = "http://www.filme-streamz.com"
        img += item.findNext("img")["src"]
        if 1<len(re.findall("http", img)):
            img = item.findNext("img")["src"]
        list_item = xbmcgui.ListItem(label=name, thumbnailImage=img)
        list_item.setInfo('video', {'title': name, 'url': s})
        url = '{0}?action=play&url={1}'.format(__url__, s)
        is_folder = False
        listing.append((url, list_item, is_folder))
        #print(name)
        #print("finde .w. : " + str(name))
        #print(re.search("http:", s) )
        #print(item["href"])

    # Add our listing to Kodi.
    # Large lists and/or slower systems benefit from adding all items at once via addDirectoryItems
    # instead of adding one by ove via addDirectoryItem.
    xbmcplugin.addDirectoryItems(__handle__, listing, len(listing))
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(__handle__, xbmcplugin.SORT_METHOD_NONE) #.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(__handle__)

    

def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring
    :param paramstring:
    :return:
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    #print(paramstring)
    params = dict(parse_qsl(paramstring[1:]))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            #xbmcgui.Dialog().ok("list_videos(params['category'])", str(params['category']), str(params), "")
            if "search" == params["category"]:
                dialog_search()
        elif params['action'] == 'detail':
            # Play a video from a provided URL.
            #play_video(params['video'])
            #print(params)
            dialog_detail(params["url"])
        elif params['action'] == 'description':
            #print(str(params))
            #print(str(params["text"]))
            try:
                descwindow = textbox()
                descwindow.settext(str(params["text"]))
                descwindow.doModal()
                del descwindow
            except:
                print("error: description-window")
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            #play_video(params['video'])
            #print(params)
            xbmcgui.Dialog().ok("play_video(params['video'])", str(params['url']), str(params), "")
            hostUrl = str(params['url'])
            #hostUrl = "http://beta.vidup.me/embed-y47ezftvhoy5-620x330.html"
            videoLink = urlresolver.resolve(hostUrl)
            # videoLink = decode_htmlentities(videoLink)
            # videoLink -> http://46.4.78.201/f0/c47edb45c7b17ea101322ba531817485/50067006/6/mp4/5ryzwM1309081242.mp4

            xbmcgui.Dialog().ok(addonname, str(hostUrl), videoLink, "")
            # play mv
            xbmc.Player().play(videoLink)
        else:
            xbmcgui.Dialog().ok("Router", params['action'], "", str(params))
            

    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    router(sys.argv[2])
