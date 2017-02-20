import urllib, urllib2, os, io, xbmcplugin, xbmc, xbmcgui, xbmcaddon, json, re

addon = xbmcaddon.Addon('plugin.video.boyztoyzclub')
localizedString = addon.getLocalizedString
title = addon.getAddonInfo('name')
icon = addon.getAddonInfo('icon')
user = addon.getSetting('btusername')
passw = addon.getSetting('btpassword')

if user == '' or passw == '':
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('Boyz Toyz Club', 'Please enter your account details','or register an account','at http://www.boyztoyz.club','Cancel','Login')
    if ret == 1:
        keyb = xbmc.Keyboard('', 'Enter Username')
        keyb.doModal()
        if (keyb.isConfirmed()):
            username = keyb.getText()
            keyb = xbmc.Keyboard('', 'Enter Password:')
            keyb.doModal()
            if (keyb.isConfirmed()):
                password = keyb.getText()
                addon.setSetting('btusername',username)
                addon.setSetting('btpassword',password)

def OpenURL(url, headers={}, user_data={}, justCookie=False):
	if user_data:
		user_data = urllib.urlencode(user_data)
		req = urllib2.Request(url, user_data)
	else:
		req = urllib2.Request(url)
	
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0')
	for k, v in headers.items():
		req.add_header(k, v)
	
	response = urllib2.urlopen(req)
	
	if justCookie == True:
		if response.info().has_key("Set-Cookie"):
			data = response.info()['Set-Cookie']
		else:
			data = None
	else:
		data = response.read().replace("\r", "")
	
	response.close()
	return data

def ReadFile(fileName):
	try:
		f = open(fileName,'r')
		content = f.read().replace("\n\n", "\n")
		f.close()
	except:
		content = ""

	return content

def m3u2list(url):
	if url.find("http") >= 0:
		response = OpenURL(url)
	else:
		response = ReadFile(url)
		
	matches=re.compile('^#EXTINF:-?[0-9]*(.*?),(.*?)\n(.*?)$',re.I+re.M+re.U+re.S).findall(response)
	li = []
	for params, display_name, url in matches:
		item_data = {"params": params, "display_name": display_name, "url": url}
		li.append(item_data)

	list = []
	for channel in li:
		item_data = {"display_name": channel["display_name"], "url": channel["url"]}
		matches=re.compile(' (.+?)="(.+?)"',re.I+re.M+re.U+re.S).findall(channel["params"])
		for field, value in matches:
			item_data[field.strip().lower().replace('-', '_')] = value.strip()
		list.append(item_data)
	return list

def GetEncodeString(str):
	try:
		import chardet
		str = str.decode(chardet.detect(str)["encoding"]).encode("utf-8")
	except:
		try:
			str = str.encode("utf-8")
		except:
			pass
	return str

def m3uCategory(url):	
	tmpList = []
	list = m3u2list(url)

	for channel in list:
		name = GetEncodeString(channel["display_name"])
		AddDir(name ,channel["url"], 3, "", isFolder=False)
		tmpList.append({"url": channel["url"], "image": "", "name": name.decode("utf-8")})

	return tmpList

def AddDir(name, url, mode, iconimage, description="", isFolder=True, background=None):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)

	liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={ "Title": name, "Plot": description})
	if background:
		liz.setProperty('fanart_image', background)
	if mode == 2:
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10008).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=22)'.format(sys.argv[0], urllib.quote_plus(url)))])
	elif mode == 3:
		liz.setProperty('IsPlayable', 'true')
		liz.addContextMenuItems(items = [('{0}'.format(localizedString(10009).encode('utf-8')), 'XBMC.RunPlugin({0}?url={1}&mode=31&iconimage={2}&name={3})'.format(sys.argv[0], urllib.quote_plus(url), iconimage, name))])
		
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring) >= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?','')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0].lower()] = splitparams[1]
	return param

def PlayUrl(name, url, iconimage=None):
	print '--- Playing "{0}". {1}'.format(name, url)
	listitem = xbmcgui.ListItem(path=url, thumbnailImage=iconimage)
	listitem.setInfo(type="Video", infoLabels={ "Title": name })
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)


params=get_params()
url=None
name=None
mode=None
iconimage=None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass
try:        
	mode = int(params["mode"])
except:
	pass

	
if mode == None or url == None or len(url) < 1:
	url = "http://iptv.wssiptv.com:80/get.php?username={0}&password={1}&type=m3u&output=hls".format(user, passw)
	print '--- Mode {0}, Calling m3yCategory with url {1}'.format(mode, url)
	m3uCategory(url)
elif mode == 2:
	print '--- Mode {0}, Calling m3yCategory with url {1}'.format(mode, url)
	m3uCategory(url)
elif mode == 3:
	print '--- Mode {0}, Calling PlayUrl with url {1}'.format(mode, url)
	PlayUrl(name, url, iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

