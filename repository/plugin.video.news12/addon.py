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

from xbmcswift2 import Plugin


STRINGS = {
    'page': 30001,
    'streams': 30100,
    'streams2': 30101,
	

}

STATIC_STREAMS = (
    {
        'title': 'News 12 Long Island',
        'logo': 'news12.jpg',
        'stream_url': ('rtmp://fs-b4e3010000000000.id.cdn.cv.net/vxedge/fs-b4e3010000000000 playpath=fs-b4e3010000000000 swfUrl=http://longisland.news12.com/js/libs/jwplayer/6.9/jwplayer.flash.swf app=vxedge/fs-b4e3010000000000 pageUrl=http://longisland.news12.com/news/news-12-long-island-live-stream-1.3923191?qr=1'
                       ' live=true swfVfy=true timeout=10'),
    },
	{
        'title': 'News 12 Bronx',
        'logo': 'news12.jpg',
        'stream_url': ('rtmp://fs-b5e3010000000000.id.cdn.cv.net/vxedge/fs-b5e3010000000000 playpath=fs-b5e3010000000000 swfUrl=http://bronx.news12.com/js/libs/jwplayer/6.9/jwplayer.flash.swf app=vxedge/fs-b5e3010000000000 pageUrl=http://bronx.news12.com/news/news-12-bronx-live-stream-1.3924984?qr=1 live=true swfVfy=true timeout=10'
                       ' live=true swfVfy=true timeout=10'),
    },
	{
        'title': 'News 12 Connecticut',
        'logo': 'news12.jpg',
        'stream_url': ('rtmp://fs-bbe3010000000000.id.cdn.cv.net/vxedge/fs-bbe3010000000000 playpath=fs-bbe3010000000000 swfUrl=http://connecticut.news12.com/js/libs/jwplayer/6.9/jwplayer.flash.swf app=vxedge/fs-bbe3010000000000 pageUrl=http://connecticut.news12.com/news/news-12-connecticut-live-stream-1.3925523?qr=1 live=true swfVfy=true timeout=10'
                       ' live=true swfVfy=true timeout=10'),
    },
	{
        'title': 'News 12 Hudson Valley',
        'logo': 'news12.jpg',
        'stream_url': ('rtmp://fs-bae3010000000000.id.cdn.cv.net/vxedge/fs-bae3010000000000 playpath=fs-bae3010000000000 swfUrl=http://hudsonvalley.news12.com/js/libs/jwplayer/6.9/jwplayer.flash.swf app=vxedge/fs-bae3010000000000 pageUrl=http://hudsonvalley.news12.com/news/news-12-hudson-valley-live-stream-1.3925702?qr=1 live=true swfVfy=true timeout=10'
                       ' live=true swfVfy=true timeout=10'),
    },
	{
        'title': 'NEWS 12 NEW JERSEY',
        'logo': 'news12.jpg',
        'stream_url': ('rtmp://fs-b9e3010000000000.id.cdn.cv.net/vxedge/fs-b9e3010000000000 playpath=fs-b9e3010000000000 swfUrl=http://newjersey.news12.com/js/libs/jwplayer/6.9/jwplayer.flash.swf app=vxedge/fs-b9e3010000000000 pageUrl=http://newjersey.news12.com/news/news-12-new-jersey-live-stream-1.3925819?qr=1 live=true swfVfy=true timeout=10'
                       ' live=true swfVfy=true timeout=10'),
    },
	{
        'title': 'News 12 Westchester',
        'logo': 'news12.jpg',
        'stream_url': ('rtmp://fs-bce3010000000000.id.cdn.cv.net/vxedge/fs-bce3010000000000 playpath=fs-bce3010000000000 swfUrl=http://westchester.news12.com/js/libs/jwplayer/6.9/jwplayer.flash.swf app=vxedge/fs-bce3010000000000 pageUrl=http://westchester.news12.com/news/news-12-westchester-live-stream-1.3924903?qr=1 live=true swfVfy=true timeout=10'
                       ' live=true swfVfy=true timeout=10'),
    },
	{
        'title': 'News 12 Brooklyn',
        'logo': 'news12.jpg',
        'stream_url': ('rtmp://fs-ace3010000000000.id.cdn.cv.net/vxedge/fs-ace3010000000000 playpath=fs-ace3010000000000 swfUrl=http://brooklyn.news12.com/js/libs/jwplayer/6.9/jwplayer.flash.swf app=vxedge/fs-ace3010000000000 pageUrl=http://brooklyn.news12.com/news/news-12-brooklyn-live-stream-1.3925389?qr=1 live=true swfVfy=true timeout=10'
                       ' live=true swfVfy=true timeout=10'),
    },
)


STATIC_STREAMS2 = (
    {
        'title': 'Events IPTV Only Links',
        'logo': 'Hushamallsports.jpg',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/event.m3u'),
    },
)


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
