import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,urlparse,random
import threading
addon_id = 'plugin.video.arabmovies'
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
HOME         =  xbmc.translatePath('special://home/')
aralab = "http://tv1.alarab.com"
extensioncheck = ['.avi','.mp4','.mpg','.mpeg','.mov','.mkv','.xvid','.divx']
dialog = xbmcgui.Dialog()
def CATEGORIES():
	addDir2('ARALAB',aralab,2,icon,fanart)
def TV1ARALAB(url):
	addDir2('SEARCH','url',23,icon,fanart)
	link = open_url(url)
	try:
		latest = re.compile('<li itemscope itemtype="(.+?)/li>',re.DOTALL).findall(link)
		for block in latest:
			match = re.compile('href="([^"]+)').findall(block)
			for url in match:
				matchimg = re.compile('src="(.+?)" alt="(.+?)" />').findall(block)
				for img,name in matchimg:
					url = aralab + url
					addDir2("LATEST: " + name,url,21,img,fanart)	
	except: pass
	try:
		latest = re.compile('<a class="channels(.+?)/a>',re.DOTALL).findall(link)
		for block in latest:
			match = re.compile('href="([^"]+)').findall(block)
			for url in match:
				matchimg = re.compile('src="(.+?)" alt="(.+?)"').findall(block)
				for img,name in matchimg:
					url = aralab + url
					addDir2("CHANNEL: " + name,url,21,img,fanart)	
	except: pass
	
	menu=re.compile('<ul class="menu(.+?)/ul>',re.DOTALL).findall(link)
	for url in menu:
		matchsections = re.compile('<a title="" href="(.+?)" ><span>(.+?)</span>').findall(url)
		for url,name in matchsections:
			url = aralab + url
			url = re.sub(' ','%20',url)
			addDir2(name,url,21,icon,fanart)

def TV1ARALAB_ITEMS(url):
	link = open_url(url)
	items = re.compile('<div class="video-box"(.+?)/div>',re.DOTALL).findall(link)
	try:
		for url in items:
			movielink = re.compile('<a href="(.+?)">').findall(url)
			for links in movielink:
				matchimg = re.compile('src="(.+?)" alt="(.+?)" />').findall(url)
				for img,name in matchimg:
					links = aralab + links
					if "series" in links:
						addDir2(name,links,21,img,fanart)
					else:
						addDir2(name,links,22,img,fanart)
	except:addDir2('Videos not Found...',links,1,icon,fanart)
	try:
		items = re.compile('<div class="pages"(.+?)/div>',re.DOTALL).findall(link)
		for pages in items:
			matchpages = re.compile('<a class="(.+?)" href="(.+?)" title="(.+?)"').findall(pages)
			for check,url,page in matchpages:
				if not "blue" in check:
					if not aralab in url:
						url = aralab + url
						addDir2(page,url,21,icon,fanart)
	except: pass
def TV1ARALAB_PLAY(name,url,iconimage):
	moviename = name
	movieposter = iconimage
	link = open_url(url)
	items = re.compile('<iframe style="background(.+?)llowFullScreen></iframe>',re.DOTALL).findall(link)
	try:
		for url in items:
			match = re.compile('src="([^"]+)').findall(url)
			for movielink in match:
				movielink = re.sub(' ','%20',movielink)
				link = open_url(movielink)
				matchfinal = re.compile('file: "(.+?)",').findall(link)
				for url in matchfinal: 
					if any(value in url for value in extensioncheck):
						addLink("PLAY: " + moviename,url,100,movieposter,fanart)
	except: addDir2('Videos not Found...',links,1,icon,fanart)

def SEARCH_TV1ARALAB():
	search_entered =''
	keyboard = xbmc.Keyboard(search_entered, 'Search')
	keyboard.doModal()
	if keyboard.isConfirmed(): search_entered = keyboard.getText()
	if len(search_entered)>1:
		search = re.sub(' ','-',search_entered)
		query = "/q/%s" %(search)
		searchlink = aralab + query
		TV1ARALAB_ITEMS(searchlink)
		
def PLAYMOVIE(name,url,iconimage):
	movieimage = iconimage
	# url = "http://flv2.alarab.com:8080/new/iphone/104983.mp4"
	item = xbmcgui.ListItem(name, iconImage=movieimage, thumbnailImage=movieimage)
	item.setArt({'icon': movieimage, 'thumb': movieimage, 'poster': movieimage, 'tvshow.poster': movieimage, 'season.poster': movieimage})
	item.setInfo(type='Video', infoLabels={ "Title": name})
	xbmc.Player().play(url, item)
	
def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param
			
def SEARCH(url,name):


	search_entered =''
	keyboard = xbmc.Keyboard(search_entered, 'Search')
	keyboard.doModal()
	if keyboard.isConfirmed(): search_entered = keyboard.getText()
	if len(search_entered)>1:
		global global_search ; global_search = search_entered
		global global_fetch ; global_fetch = []
		threads_hosts = [threading.Thread(target=fetch_hosts, args=(host,)) for host in hosts]
		for thread in threads_hosts:
			thread.start()
		for thread in threads_hosts:
			thread.join()


def PLAYURLRESOLVER(url,name,mode,iconimage):

			stream_url = urlresolver.HostedMediaFile(link).resolve()
			liz=xbmcgui.ListItem(name, iconImage=fanart_image, thumbnailImage=iconimage); liz.setInfo( type="Video", infoLabels={ "Title": originalname } )
			xbmc.Player ().play(stream_url,liz,False)


	
def addDir2(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addLink(name,url,mode,iconimage,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
def addDir(name,url,mode,iconimage,itemcount,isFolder=False):
        try:
          if not 'COLOR' in name:
            splitName=name.partition('(')
            simplename=""
            simpleyear=""
            if len(splitName)>0:
                simplename=splitName[0]
                simpleyear=splitName[2].partition(')')
            if len(simpleyear)>0:
                simpleyear=simpleyear[0]
            mg = metahandlers.MetaData()
            meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
            liz.setInfo( type="Video", infoLabels= meta )
            liz.setProperty("IsPlayable","true")
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=False)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
            else: liz.setProperty('fanart_image', fanart)
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder,totalItems=itemcount)
            return ok
        except:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={ "Title": name } )
            liz.setProperty('fanart_image', fanart)
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=isFolder)
            return ok

			
####### SCRAPING TOOLS #####			
def regex_get_all(text, start_with, end_with):
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r				
def regex_from_to(text, from_string, to_string, excluding=True):
    if excluding:
	   try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
	   except: r = ''
    else:
       try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
       except: r = ''
    return r        
####### PARSEDOM THX TO TKNORRIS #####

def _getDOMContent(html, name, match, ret):
    end_str = "</%s" % (name)
    start_str = '<%s' % (name)

    start = html.find(match)
    end = html.find(end_str, start)
    pos = html.find(start_str, start + 1)

    while pos < end and pos != -1:  # Ignore too early </endstr> return
        tend = html.find(end_str, end + len(end_str))
        if tend != -1:
            end = tend
        pos = html.find(start_str, pos + 1)

    if start == -1 and end == -1:
        result = ''
    elif start > -1 and end > -1:
        result = html[start + len(match):end]
    elif end > -1:
        result = html[:end]
    elif start > -1:
        result = html[start + len(match):]
    else:
        result = ''

    if ret:
        endstr = html[end:html.find(">", html.find(end_str)) + 1]
        result = match + result + endstr

    return result

def _getDOMAttributes(match, name, ret):
    pattern = '''<%s[^>]* %s\s*=\s*(?:(['"])(.*?)\\1|([^'"].*?)(?:>|\s))''' % (name, ret)
    results = re.findall(pattern, match, re.I | re.M | re.S)
    return [result[1] if result[1] else result[2] for result in results]

def _getDOMElements(item, name, attrs):
    if not attrs:
        pattern = '(<%s(?: [^>]*>|/?>))' % (name)
        this_list = re.findall(pattern, item, re.M | re.S | re.I)
    else:
        last_list = None
        for key in attrs:
            pattern = '''(<%s [^>]*%s=['"]%s['"][^>]*>)''' % (name, key, attrs[key])
            this_list = re.findall(pattern, item, re.M | re. S | re.I)
            if not this_list and ' ' not in attrs[key]:
                pattern = '''(<%s [^>]*%s=%s[^>]*>)''' % (name, key, attrs[key])
                this_list = re.findall(pattern, item, re.M | re. S | re.I)
    
            if last_list is None:
                last_list = this_list
            else:
                last_list = [item for item in this_list if item in last_list]
        this_list = last_list
    
    return this_list

def parse_dom(html, name='', attrs=None, ret=False):
    if attrs is None: attrs = {}
    if isinstance(html, str):
        try:
            html = [html.decode("utf-8")]  # Replace with chardet thingy
        except:
            print "none"
            try:
                html = [html.decode("utf-8", "replace")]
            except:
                
                html = [html]
    elif isinstance(html, unicode):
        html = [html]
    elif not isinstance(html, list):
        
        return ''

    if not name.strip():
        
        return ''
    
    if not isinstance(attrs, dict):
        
        return ''

    ret_lst = []
    for item in html:
        for match in re.findall('(<[^>]*\n[^>]*>)', item):
            item = item.replace(match, match.replace('\n', ' ').replace('\r', ' '))

        lst = _getDOMElements(item, name, attrs)

        if isinstance(ret, str):
            lst2 = []
            for match in lst:
                lst2 += _getDOMAttributes(match, name, ret)
            lst = lst2
        else:
            lst2 = []
            for match in lst:
                temp = _getDOMContent(item, name, match, ret).strip()
                item = item[item.find(temp, item.find(match)):]
                lst2.append(temp)
            lst = lst2
        ret_lst += lst

    # log_utils.log("Done: " + repr(ret_lst), xbmc.LOGDEBUG)
    return ret_lst

##### OPEN URL ######	
def open_url(url):
        # url=url.replace(' ','%20')
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link
def setView(content, viewType):
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if selfAddon.getSetting('auto-view')=='true':
        xbmc.executebuiltin("Container.SetViewMode(%s)" % selfAddon.getSetting(viewType) )
		
params=get_params(); url=None; name=None; mode=None; site=None; iconimage=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)
print params

if mode==None or url==None or len(url)<1: CATEGORIES()
elif mode==2: TV1ARALAB(url)
elif mode==21: TV1ARALAB_ITEMS(url)
elif mode==22: TV1ARALAB_PLAY(name,url,iconimage)
elif mode==23: SEARCH_TV1ARALAB()
elif mode==100: PLAYMOVIE(name,url,iconimage)
xbmcplugin.endOfDirectory(int(sys.argv[1]))

