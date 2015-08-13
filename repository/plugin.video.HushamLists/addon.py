#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2012 Tristan Fischer (sphere@dersphere.de)
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
    'more': 30103,
	'streams2': 30101,
	

}

STATIC_STREAMS = (
    {
        'title': 'The All Sports Links',
        'logo': 'Hushamallsports.jpg',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/allsports.m3u'),
    }, {
        'title': 'Sports ACE Stream Links',
        'logo': 'HushamMonsterlist.gif',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/acestreamlinks.m3u'),
    }, {
        'title': 'UK English Lists',
        'logo': 'HushamMonsterlist.gif',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/uk-english.m3u'),
    }, {
        'title': 'Arabic Lists',
        'logo': 'HushamMonsterlist.gif',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/ArabicIPTV.m3u'),
    }, {
        'title': 'USA Links',
        'logo': 'HushamMonsterlist.gif',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/usalive.m3u'),
    }, {
        'title': 'Canada IPTV Lists',
        'logo': 'HushamMonsterlist.gif',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/canada.m3u'),
    }, {
        'title': 'Iran IPTV Lists',
        'logo': 'HushamMonsterlist.gif',
        'stream_url': ('https://raw.githubusercontent.com/hmemar/husham.com/master/'
                       'Lists/irantv.m3u'),
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
        'name': 'Husham Guides',
        'logo': 'TheMainH.jpg',
        'channel_id': 'UCb5DkdbEOBNoOY7RGkGN4pg',
        'user': 'hmemar22',
    }, {
        'name': 'The XBMC/KODI Help Guides',
        'logo': 'xbmchelp.jpg',
        'channel_id': 'UC0XB4eRTTYxYeLMpVcIClSQ',
        'user': 'XBMChelpguide',
    }, {
        'name': 'The Memar Games Channel',
        'logo': 'MemarGames.jpg',
        'channel_id': 'UCUglpFpByLwcKnbxfUlVc2g',
        'user': 'HushamMemarGames',
    }, {
        'name': 'Learn Arabic with Arabic Pod 101',
        'logo': 'arabicpod.jpg',
        'channel_id': 'UC5bjJ5x0i_XRGTMHF2IoL8w',
        'user': 'arabicpod101',
    }, {
        'name': 'MBC The X Factor',
        'logo': 'xfactor.jpg',
        'channel_id': 'UCb0pvpGeKMRiwqjg2mP5rBA',
        'user': 'TheXFactorArabia',
    },
	 {
        'name': 'MBC The X Factor',
        'logo': 'mbc.jpg',
        'channel_id': 'UCy2CIDKYZqqbeJ0NHNcJ9sQ',
        'user': 'mbc',
    },
	 {
        'name': 'Arab Idol',
        'logo': 'arabidol.jpg',
        'channel_id': 'UCt8w6KPEDkf_Qe1FreHCU0A',
        'user': 'ArabIdol',
    },
	 {
        'name': 'The Voice Arabic',
        'logo': 'arabicvoice.jpg',
        'channel_id': 'UCBgVoRRoRuIpVwD6CfoBRag',
        'user': 'MBCTheVoiceShow',
    },
	 {
        'name': 'The Voice UK',
        'logo': 'voiceuk.jpg',
        'channel_id': 'UCozj60ha6CLG1LsAmBFRE0g',
        'user': 'theVOICEuk',
    },
	 {
        'name': 'The Voice USA',
        'logo': 'nbcvoice.jpg',
        'channel_id': 'UCpdK1NLHxEUGXc1gq2NxkTw',
        'user': 'NBCTheVoice',
    },
	 {
        'name': 'The Ellen Show',
        'logo': 'ellen.jpg',
        'channel_id': 'UCp0hYYBW6IMayGgR-WeoCvQ',
        'user': 'TheEllenShow',
    }
)



YOUTUBE_URL ='plugin://plugin.video.youtube/channel/%s/?page=1'

plugin = Plugin()


@plugin.route('/')
def show_root_menu():
    items = [
        {'label': _('streams'),
         'path': plugin.url_for('show_streams')},
		 {'label': _('more'),
         'path': plugin.url_for('show_streams2')},
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

	

@plugin.route('/streams2/')
def show_streams2():
    items = [{
        'label': stream['title'],
        'thumbnail': get_logo(stream['logo']),
        'path': stream['stream_url'],
        'is_playable': True,
    } for stream in STATIC_STREAMS2]
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
