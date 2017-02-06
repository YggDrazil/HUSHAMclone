#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("NTYgMmYgNDcgM2YKCgozYiA9IHsKCSc1MCc6IDRjLAoJJzI0JzogNGUsCgknMzQnOiA0ZCwKCQoKfQoKMjUgPSAoCgl7CgkJJzQnOiAnMTAgMTIgMzcgMjgnLAoJCSc3JzogJzEuOCcsCgkJJzAnOiAoJzk6Ly82LWUuMTkuMTcuMTguMTYvNS82LWUvNi1lJyksCgl9LAoJewoJCSc0JzogJzEwIDEyIDM3IDI4IGEnLAoJCSc3JzogJzEuOCcsCgkJJzAnOiAoJzk6Ly82LTE0LjE5LjE3LjE4LjE2LzUvNi0xNC82LTE0JyksCgl9LAoJewoJCSc0JzogJzEwIDEyIDJlJywKCQknNyc6ICcxLjgnLAoJCScwJzogKCc5Oi8vNi0xNS4xOS4xNy4xOC4xNi81LzYtMTUvNi0xNScpLAoJfSwKCXsKCQknNCc6ICcxMCAxMiAyZSBhJywKCQknNyc6ICcxLjgnLAoJCScwJzogKCc5Oi8vNi0yLjE5LjE3LjE4LjE2LzUvNi0yLzYtMicpLAoJfSwKCXsKCQknNCc6ICcxMCAxMiAxYicsCgkJJzcnOiAnMS44JywKCQknMCc6ICgnOTovLzYtMWEuMTkuMTcuMTguMTYvNS82LTFhLzYtMWEnKSwKCX0sCgl7CgkJJzQnOiAnMTAgMTIgMWIgYScsCgkJJzcnOiAnMS44JywKCQknMCc6ICgnOTovLzYtZi4xOS4xNy4xOC4xNi81LzYtZi82LWYnKSwKCX0sCgl7CgkJJzQnOiAnMTAgMTIgMmEgMmInLAoJCSc3JzogJzEuOCcsCgkJJzAnOiAoJzk6Ly82LWQuMTkuMTcuMTguMTYvNS82LWQvNi1kJyksCgl9LAoJewoJCSc0JzogJzEwIDEyIDJhIDJiIGEnLAoJCSc3JzogJzEuOCcsCgkJJzAnOiAoJzk6Ly82LTMuMTkuMTcuMTguMTYvNS82LTMvNi0zJyksCgl9LAoJewoJCSc0JzogJzI3IDEyIDQzIDJkJywKCQknNyc6ICcxLjgnLAoJCScwJzogKCc5Oi8vNi01YS4xOS4xNy4xOC4xNi81LzYtNWEvNi01YScpLAoJfSwKCXsKCQknNCc6ICcyNyAxMiA0MyAyZCBhJywKCQknNyc6ICcxLjgnLAoJCScwJzogKCc5Oi8vNi0xMS4xOS4xNy4xOC4xNi81LzYtMTEvNi0xMScpLAoJfSwKCXsKCQknNCc6ICcxMCAxMiAxYycsCgkJJzcnOiAnMS44JywKCQknMCc6ICgnOTovLzYtYy4xOS4xNy4xOC4xNi81LzYtYy82LWMnKSwKCX0sCgl7CgkJJzQnOiAnMTAgMTIgMWMgYScsCgkJJzcnOiAnMS44JywKCQknMCc6ICgnOTovLzYtMy4xOS4xNy4xOC4xNi81LzYtMy82LTMnKSwKCX0sCgl7CgkJJzQnOiAnMTAgMTIgMjAnLAoJCSc3JzogJzEuOCcsCgkJJzAnOiAoJzk6Ly82LTEzLjE5LjE3LjE4LjE2LzUvNi0xMy82LTEzJyksCgl9LAoJewoJCSc0JzogJzEwIDEyIDIwIGEnLAoJCSc3JzogJzEuOCcsCgkJJzAnOiAoJzk6Ly82LTIuMTkuMTcuMTguMTYvNS82LTIvNi0yJyksCgl9LAoJewoJCSc0JzogJzU5IDI3JywKCQknNyc6ICcxLjgnLAoJCScwJzogKCcxZjovLzNkLjNjLjI5LzVkLzMyQDQ0LzI2LWIuMjEnKSwKCX0sCgl7CgkJJzQnOiAnMzEnLAoJCSc3JzogJzEuOCcsCgkJJzAnOiAoJzFmOi8vNTUuNDAuMzAuMjkvNTgvNWUvMWQuMjE/Yj9iKjYyJCcpLAoJfSwKCXsKCQknNCc6ICczNSA1MycsCgkJJzcnOiAnMS44JywKCQknMCc6ICgnMWY6Ly80NS02MC4zNi4xNi81ZC8zOUA0Mi8xZC4yMScpLAoJfSwKCXsKCQknNCc6ICczNSA1MyA1ZicsCgkJJzcnOiAnMS44JywKCQknMCc6ICgnMWY6Ly8yYy0zMy4zZS42MS81Mi8zYS8yNC81MS8yYy8zOC4yMScpLAoJfSwKKQoKCjIzID0gKAoJewoJCSc0JzogJzQ4IDU0IDU3IDRiJywKCQknNyc6ICcyMi44JywKCQknMCc6ICgnNDk6Ly81Yi4xZS4yOS80MS80Ni4yOS8xZC8nCgkJCQkJICAgJzRhLzRmLjVjJyksCgl9LAop")))(lambda a,b:b[int("0x"+a.group(1),16)],"stream_url|news12|afe3010000000000|b8e3010000000000|title|vxedge|fs|logo|jpg|rtmp|Weather|b|bce3010000000000|bae3010000000000|b4e3010000000000|b6e3010000000000|News|b3e3010000000000|12|ace3010000000000|aee3010000000000|b5e3010000000000|net|cdn|cv|id|bbe3010000000000|Connecticut|Westchester|master|githubusercontent|http|Brooklyn|m3u8|Hushamallsports|STATIC_STREAMS2|streams|STATIC_STREAMS|index_1200_av|NEWS|Island|com|Hudson|Valley|iphone|JERSEY|Bronx|xbmcswift2|bloomberg|Bloomberg|abc_live4|streaming|streams2|NASA|akamaihd|Long|playlist|NASA_101|6540154|STRINGS|abcnews|abclive|ustream|Plugin|videos|hmemar|319270|NEW|136330|nasatv|husham|import|Events|https|Lists|Links|30001|30101|30100|event|page|live|uhls|TV|IPTV|cdn3|from|Only|btv|ABC|b9e3010000000000|raw|m3u|i|us|HD|lh|tv|t".split("|")))


YOUTUBE_CHANNELS = (
    {
        'name': 'WXII 12 NEWS',
        'logo': 'news12.jpg',
        'channel_id': 'UC0ZsHHC_frpcqneDpMiteCQ',
        'user': 'hmemar22',
    }, 
	{
        'name': 'WDEF News 12',
        'logo': 'news12.jpg',
        'channel_id': 'UCMp6dYTbPOrKFHMH6rGcp2g',
        'user': 'hmemar22',
    }, 
	{
        'name': 'twelvedottv',
        'logo': 'news12.jpg',
        'channel_id': 'UC_DlTqJhRV-OafjHESJciNw',
        'user': 'hmemar22',
    }, 
	{
        'name': 'CNN',
        'logo': 'news12.jpg',
        'channel_id': 'UCupvZG-5ko_eiXAupbDfxWw',
        'user': 'hmemar22',
    }, 
	{
        'name': 'CNN Live',
        'logo': 'news12.jpg',
        'channel_id': 'UCRrW0ddrbFnJCbyZqHHv4KQ',
        'user': 'hmemar22',
    }, 
	{
        'name': 'euronews (in English)',
        'logo': 'news12.jpg',
        'channel_id': 'UCSrZ3UV4jOidv8ppoVuvW9Q',
        'user': 'hmemar22',
    },  
)



YOUTUBE_URL ='plugin://plugin.video.youtube/channel/%s/?page=1'

plugin = Plugin()


@plugin.route('/')
def show_root_menu():
    items = [
        {'label': _('streams'),
         'path': plugin.url_for('show_streams')},
		 {'label': _('Videos'),
         'path': plugin.url_for('show_channels')},

    ]
    return plugin.finish(items)


@plugin.route('/streams/')
def show_streams():
    items = [{
        'label': stream['title'],
        'thumbnail': get_logo(stream['logo']),
        'path': stream['stream_url'],
        'is_playable': True,
    } for stream in STATIC_STREAMS]
    return plugin.finish(items)

	
	

@plugin.route('/channels/')
def show_channels():
    items = [{
        'label': channel['name'],
        'thumbnail': get_logo(channel['logo']),
        'path': YOUTUBE_URL % channel['channel_id'],
    } for channel in YOUTUBE_CHANNELS]
    return plugin.finish(items)

def get_logo(logo):
    addon_id = plugin._addon.getAddonInfo('id')
    return 'special://home/addons/%s/resources/media/%s' % (addon_id, logo)


def _(string_id):
    if string_id in STRINGS:
        return plugin.get_string(STRINGS[string_id])
    else:
        plugin.log.warning('String is missing: %s' % string_id)
        return string_id


def log(text):
    plugin.log.info(text)

if __name__ == '__main__':
    plugin.run()
