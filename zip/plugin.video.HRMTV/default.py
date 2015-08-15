#Programming by Hisham Khalil Marzouk
#plugin.video.HRMTV
import xbmc, xbmcgui
import xbmcplugin
import xbmcaddon
import sys


IMG='https://sites.google.com/site/arabicchannelslogos/'
EXT2='.jpg'
HD='_HD'
EXT='.m3u8'
BaseUrl= 'http://8.21.48.19:7777/'  
ch1 ='MBC1' 
ch2 ='MBC2' 
ch3 ='MBC3'   
ch4 ='MBC4'
ch5 ='MBCDrama' 
ch6 ='MBCAction'
ch7 ='MBCMAX'
ch8 ='MBCMaser'
ch9 ='RotanaAflam'
ch10 ='RotanaClip'
ch11 ='RotanaKhalijiah'
ch12 ='RotanaMusic'
ch13 ='RotanaMasriya'
ch14 ='RotanaZaman'
ch15 ='RotanaCinema'
ch16 ='ZeeAlwan'
ch17 ='ZeeAflam'
ch18 ='Hayat'
ch19 ='AlHayatMousalsalat'
ch20 ='Alhayat2'
ch21 ='NileSport'
ch22 ='NileNews'
ch23 ='NileFamily'
ch24 ='NileLife'
ch25 ='NileDrama2'
ch26 ='RotanaCinema'
ch27 ='AlAan'
ch28 ='AlMayadeen'
ch29 ='AlManar'
ch30 ='AlJadeed'
ch31 ='LBC'
ch32 ='AlLubnania'
ch33 ='TeleLiban'
ch34 ='Future'
ch35 ='FutureNews'
ch36 ='OTV'
ch37 ='NBNLebanon'
ch38 ='MTVLebanon'
ch39 ='SyriaSat'
ch40 ='SyrianEducation'
ch41 ='NourElSham'
ch42 ='SyriaDrama'
ch43 ='Talaqi'
ch44 ='SamaTV'
ch45 ='CairoCinema'
ch46 ='Mosar3'
ch47 ='CairoDrama'
ch48 ='CairoComedy'
ch49 ='CBC'
ch50 ='CBCSofra'
ch51 ='CBC2'
ch52 ='CBCDrama'
ch53 ='DubaiEurope'
ch54 ='SamaDubai'
ch55 ='NoorDubai'
ch56 ='DubaiOne'
ch57 ='DubaiSport2'
ch58 ='DubaiSports'
ch59 ='ADEmirates'
ch60 ='ADDrama'
ch61 ='ADSport'
ch62 ='Tunisia'
ch63 ='AlHiwarTunis'
ch64 ='Tunisie7'
ch65 ='Medi1'
ch66 ='Nessma'
ch67 ='Hannibal'
ch68 ='LayaliCinema'
ch69 ='AlNaharDrama'
ch70 ='AlNahar'
ch71 ='AlNaharMovies'
ch72 ='AlNahar2'
ch73 ='AlNaharSport'
ch74 ='ONTV'
ch75 ='AlMasriyah'
ch76 ='AlThanya'
ch77 ='SadaAlBaladDrama'
ch78 ='SadaAlBalad'
ch79 ='AlKaheraWalNas'
ch80 ='AlKaheraWalNas2'
ch81 ='AlQuran'
ch82 ='Iqraa'
ch83 ='ToyorAlJanah'
ch84 ='Baraem'
ch85 ='Semsem'
ch86 ='Koky'
ch87 ='AlJazeeraKid'
ch88 ='CNArabia'
ch89 ='AtfalwaMawaheb'
ch90 ='AlbaitBaitakCinema'
ch91 ='LayaliCinema'
ch92 ='LDC'
ch93 ='MasrawiAflam'
ch94 ='SamaCinema'
ch95 ='Fox'
ch96 ='FoxMovies'
ch97 ='OscarDrama'
ch98 ='CairoDrama'
ch99 ='MogaComedy'
ch100 ='PanoramaFilm'
ch101 ='Dream1'   
ch102 ='Dream2' 
ch103 ='PanoramaDrama'   
ch104 ='PanoramaDrama2'
ch105 ='TopMovies' 
ch106 ='OscarDrama2'
ch107 ='AlMasrawia'
ch108 ='SpacePower'
ch109 ='TimeTiatro'
ch110 ='ADNatGeo'
ch111 ='AlArabiya'   
ch112 ='AlArabiyaHadath' 
ch113 ='AlJazeera'   
ch114 ='AlJazeeraLive'
ch115 ='JSCLiveMisr' 
ch116 ='M2Morocco'
ch117 ='AlAoulaEurope'
ch118 ='AlMaghribia'
ch119 ='Tamazight'
ch120 ='Medi1'
ch121 ='CanalAlgerie'   
ch122 ='Thalitha' 
ch123 ='AlShrooq'   
ch124 ='AlAtlas'
ch125 ='A1Jordan' 
ch126 ='GamarHashimi'
ch127 ='RoyalAlBadawia'
ch128 ='Roya'
ch129 ='JordanSport'
ch130 ='ElMehwar'
ch131 ='AlAhlyTV'   
ch132 ='MusicPlus' 
ch133 ='Baghdad'   
ch134 ='AlFayhaa'
ch135 ='AlForat' 
ch136 ='Beladi'
ch137 ='Alsumaria'
ch138 ='AlBaghdadia'
ch139 ='AlSharqiya'
ch140 ='AlsharqiyaNews'
ch141 ='AlIraqiya'   
ch142 ='AlIraqia2' 
ch143 ='AqsaSatCh'   
ch144 ='PalestineLive'


#img
CH1 ='mbc'  
CH2 ='mbc2'
CH3 ='mbc3'   
CH4 ='mbc4'
CH5 ='mbcdrama' 
CH6 ='mbcaction'
CH7 ='mbcmax'
CH8 ='mbcmsr'
CH9 ='rotanaaflam'
CH10 ='rotanaclip'
CH11 ='rotanakhalejya'
CH12 ='rotanamusic'
CH13 ='rotanamasriya'
CH14 ='rotanazaman'
CH15 ='rotanacinma'
CH16 ='zeealwan'
CH17 ='zeeaflam'
CH18 ='hayat'
CH19 ='alhayatmousalsalat'
CH20 ='alhayat2'
CH21 ='nilesport'
CH22 ='nilenews'
CH23 ='nilefamly'
CH24 ='nilelife'
CH25 ='niledrama2'
CH26 ='rotanacinma'
CH27 ='alaan'
CH28 ='almayadeen'
CH29 ='almanar'
CH30 ='AlJadeed'
CH31 ='lbc'
CH32 ='allubnania'
CH33 ='teleliban'
CH34 ='futuer'
CH35 ='futurenews'
CH36 ='otvlebnon'
CH37 ='nbn'
CH38 ='mtv'
CH39 ='sirya'
CH40 ='syrianeducation'
CH41 ='nourelsham'
CH42 ='syriadrama'
CH43 ='talaqi'
CH44 ='samatv'
CH45 ='cairocinema'
CH46 ='mosar3'
CH47 ='cairodrama'
CH48 ='cairocomedy'
CH49 ='cbc'
CH50 ='cbcsofra'
CH51 ='cbc2'
CH52 ='cbcdrama'
CH53 ='dubaieurope'
CH54 ='samadubai'
CH55 ='noordubai'
CH56 ='dubaione'
CH57 ='dubaisport2'
CH58 ='dubaisports'
CH59 ='ademirates'
CH60 ='addrama'
CH61 ='adsport'
CH62 ='tunisia'
CH63 ='alhiwartunis'
CH64 ='tunisie7'
CH65 ='medi1'
CH66 ='nessma'
CH67 ='hannibal'
CH68 ='layalicinema'
CH69 ='alnahardrama'
CH70 ='alnahar'
CH71 ='alnaharmovies'
CH72 ='alnahar2'
CH73 ='alnaharsport'
CH74 ='ontv'
CH75 ='almasriyah'
CH76 ='althanya'
CH77 ='sadaalbaladdrama'
CH78 ='sadaalbalad'
CH79 ='alkaherawalnas'
CH80 ='alkaherawalnas2'
CH81 ='alquran'
CH82 ='iqraa'
CH83 ='toyoraljana'
CH84 ='baraem'
CH85 ='semsem'
CH86 ='koky'
CH87 ='aljazeerakid'
CH88 ='cnarabia'
CH89 ='atfalwamawaheb'
CH90 ='albaitbaitakcinema'
CH91 ='layalicinema'
CH92 ='ldc'
CH93 ='masrawiaflam'
CH94 ='samacinema'
CH95 ='fox'
CH96 ='foxmovies'
CH97 ='oscardrama'
CH98 ='cairodrama'
CH99 ='mogacomedy'
CH100 ='panoramafilm'
CH101 ='dreem'   
CH102 ='dreem2' 
CH103 ='panoramadrama'   
CH104 ='panoramadrama2'
CH105 ='topmovies' 
CH106 ='oscardrama2'
CH107 ='almasrawia'
CH108 ='spacepower'
CH109 ='timetiatro'
CH110 ='adnatgeo'
CH111 ='alarabiya'   
CH112 ='alarabiyahadath' 
CH113 ='aljazeera'   
CH114 ='aljazeeralive'
CH115 ='jsclivemisr' 
CH116 ='m2morocco'
CH117 ='alaoulaeurope'
CH118 ='almaghribia'
CH119 ='tamazight'
CH120 ='medi1'
CH121 ='canalalgerie'   
CH122 ='thalitha' 
CH123 ='alshrooq'   
CH124 ='alatlas'
CH125 ='a1jordan' 
CH126 ='gamarhashimi'
CH127 ='royalalbadawia'
CH128 ='roya'
CH129 ='jordansport'
CH130 ='elmehwar'
CH131 ='alahlytv'   
CH132 ='musicplus' 
CH133 ='baghdad'   
CH134 ='alfayhaa'
CH135 ='alforat' 
CH136 ='beladi'
CH137 ='alsumaria'
CH138 ='albaghdadia'
CH139 ='alsharqiya'
CH140 ='alsharqiyanews'
CH141 ='iraqya'   
CH142 ='aliraqia2' 
CH143 ='aqsasatch'   
CH144 ='Palestine'





if __name__ == '__main__':
    ADDON = xbmcaddon.Addon()
    HANDLE = int(sys.argv[1])
                  
item = xbmcgui.ListItem(ch1,ADDON.getLocalizedString(30001),iconImage=IMG+CH1+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch1+HD+EXT),item, False)
item = xbmcgui.ListItem(ch2,ADDON.getLocalizedString(30001),iconImage=IMG+CH2+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch2+HD+EXT),item, False)
item = xbmcgui.ListItem(ch3,ADDON.getLocalizedString(30001),iconImage=IMG+CH3+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch3+HD+EXT),item, False)
item = xbmcgui.ListItem(ch4,ADDON.getLocalizedString(30001),iconImage=IMG+CH4+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch4+HD+EXT),item, False)
item = xbmcgui.ListItem(ch5,ADDON.getLocalizedString(30001),iconImage=IMG+CH5+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch5+HD+EXT),item, False)
item = xbmcgui.ListItem(ch6,ADDON.getLocalizedString(30001),iconImage=IMG+CH6+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch6+HD+EXT),item, False)
item = xbmcgui.ListItem(ch7,ADDON.getLocalizedString(30001),iconImage=IMG+CH7+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch7+HD+EXT),item, False)
item = xbmcgui.ListItem(ch8,ADDON.getLocalizedString(30001),iconImage=IMG+CH8+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch8+HD+EXT),item, False)
item = xbmcgui.ListItem(ch9,ADDON.getLocalizedString(30001),iconImage=IMG+CH9+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch9+HD+EXT),item, False)
item = xbmcgui.ListItem(ch10,ADDON.getLocalizedString(30001),iconImage=IMG+CH10+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch10+HD+EXT),item, False)
item = xbmcgui.ListItem(ch11,ADDON.getLocalizedString(30001),iconImage=IMG+CH11+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch11+HD+EXT),item, False)
item = xbmcgui.ListItem(ch12,ADDON.getLocalizedString(30001),iconImage=IMG+CH12+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch12+HD+EXT),item, False)
item = xbmcgui.ListItem(ch13,ADDON.getLocalizedString(30001),iconImage=IMG+CH13+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch13+HD+EXT),item, False)
item = xbmcgui.ListItem(ch14,ADDON.getLocalizedString(30001),iconImage=IMG+CH14+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch14+HD+EXT),item, False)
item = xbmcgui.ListItem(ch15,ADDON.getLocalizedString(30001),iconImage=IMG+CH15+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch15+HD+EXT),item, False)
item = xbmcgui.ListItem(ch16,ADDON.getLocalizedString(30001),iconImage=IMG+CH16+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch16+HD+EXT),item, False)
item = xbmcgui.ListItem(ch17,ADDON.getLocalizedString(30001),iconImage=IMG+CH17+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch17+HD+EXT),item, False)
item = xbmcgui.ListItem(ch18,ADDON.getLocalizedString(30001),iconImage=IMG+CH18+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch18+HD+EXT),item, False)
item = xbmcgui.ListItem(ch19,ADDON.getLocalizedString(30001),iconImage=IMG+CH19+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch19+HD+EXT),item, False)
item = xbmcgui.ListItem(ch20,ADDON.getLocalizedString(30001),iconImage=IMG+CH20+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch20+HD+EXT),item, False)
item = xbmcgui.ListItem(ch21,ADDON.getLocalizedString(30001),iconImage=IMG+CH21+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch21+HD+EXT),item, False)
item = xbmcgui.ListItem(ch22,ADDON.getLocalizedString(30001),iconImage=IMG+CH22+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch22+HD+EXT),item, False)
item = xbmcgui.ListItem(ch23,ADDON.getLocalizedString(30001),iconImage=IMG+CH23+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch23+HD+EXT),item, False)
item = xbmcgui.ListItem(ch24,ADDON.getLocalizedString(30001),iconImage=IMG+CH24+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch24+HD+EXT),item, False)
item = xbmcgui.ListItem(ch25,ADDON.getLocalizedString(30001),iconImage=IMG+CH25+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch25+HD+EXT),item, False)
item = xbmcgui.ListItem(ch26,ADDON.getLocalizedString(30001),iconImage=IMG+CH26+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch26+HD+EXT),item, False)
item = xbmcgui.ListItem(ch27,ADDON.getLocalizedString(30001),iconImage=IMG+CH27+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch27+HD+EXT),item, False)
item = xbmcgui.ListItem(ch28,ADDON.getLocalizedString(30001),iconImage=IMG+CH28+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch28+HD+EXT),item, False)
item = xbmcgui.ListItem(ch29,ADDON.getLocalizedString(30001),iconImage=IMG+CH29+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch29+HD+EXT),item, False)
item = xbmcgui.ListItem(ch30,ADDON.getLocalizedString(30001),iconImage=IMG+CH30+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch30+HD+EXT),item, False)
item = xbmcgui.ListItem(ch31,ADDON.getLocalizedString(30001),iconImage=IMG+CH31+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch31+HD+EXT),item, False)
#item = xbmcgui.ListItem(ch32,ADDON.getLocalizedString(30001),iconImage=IMG+CH32+EXT2)
#xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch32+HD+EXT),item, True)
item = xbmcgui.ListItem(ch33,ADDON.getLocalizedString(30001),iconImage=IMG+CH33+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch33+HD+EXT),item, False)
item = xbmcgui.ListItem(ch34,ADDON.getLocalizedString(30001),iconImage=IMG+CH34+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch34+HD+EXT),item, False)
item = xbmcgui.ListItem(ch35,ADDON.getLocalizedString(30001),iconImage=IMG+CH35+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch35+HD+EXT),item, False)
item = xbmcgui.ListItem(ch36,ADDON.getLocalizedString(30001),iconImage=IMG+CH36+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch36+HD+EXT),item, False)
item = xbmcgui.ListItem(ch37,ADDON.getLocalizedString(30001),iconImage=IMG+CH37+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch37+HD+EXT),item, False)
item = xbmcgui.ListItem(ch38,ADDON.getLocalizedString(30001),iconImage=IMG+CH38+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch38+HD+EXT),item, False)
item = xbmcgui.ListItem(ch39,ADDON.getLocalizedString(30001),iconImage=IMG+CH39+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch39+HD+EXT),item, False)
item = xbmcgui.ListItem(ch40,ADDON.getLocalizedString(30001),iconImage=IMG+CH40+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch40+HD+EXT),item, False)
item = xbmcgui.ListItem(ch41,ADDON.getLocalizedString(30001),iconImage=IMG+CH41+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch41+HD+EXT),item, False)
item = xbmcgui.ListItem(ch42,ADDON.getLocalizedString(30001),iconImage=IMG+CH42+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch42+HD+EXT),item, False)
item = xbmcgui.ListItem(ch43,ADDON.getLocalizedString(30001),iconImage=IMG+CH43+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch43+HD+EXT),item, False)
item = xbmcgui.ListItem(ch44,ADDON.getLocalizedString(30001),iconImage=IMG+CH44+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch44+HD+EXT),item, False)
item = xbmcgui.ListItem(ch45,ADDON.getLocalizedString(30001),iconImage=IMG+CH45+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch45+HD+EXT),item, False)
item = xbmcgui.ListItem(ch46,ADDON.getLocalizedString(30001),iconImage=IMG+CH46+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch46+HD+EXT),item, False)
item = xbmcgui.ListItem(ch47,ADDON.getLocalizedString(30001),iconImage=IMG+CH47+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch47+HD+EXT),item, False)
item = xbmcgui.ListItem(ch48,ADDON.getLocalizedString(30001),iconImage=IMG+CH48+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch48+HD+EXT),item, False)
item = xbmcgui.ListItem(ch49,ADDON.getLocalizedString(30001),iconImage=IMG+CH49+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch49+HD+EXT),item, False)
item = xbmcgui.ListItem(ch50,ADDON.getLocalizedString(30001),iconImage=IMG+CH50+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch50+HD+EXT),item, False)
item = xbmcgui.ListItem(ch51,ADDON.getLocalizedString(30001),iconImage=IMG+CH51+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch51+HD+EXT),item, False)
item = xbmcgui.ListItem(ch52,ADDON.getLocalizedString(30001),iconImage=IMG+CH52+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch52+HD+EXT),item, False)
item = xbmcgui.ListItem(ch53,ADDON.getLocalizedString(30001),iconImage=IMG+CH53+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch53+HD+EXT),item, False)
item = xbmcgui.ListItem(ch54,ADDON.getLocalizedString(30001),iconImage=IMG+CH54+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch54+HD+EXT),item, False)
item = xbmcgui.ListItem(ch55,ADDON.getLocalizedString(30001),iconImage=IMG+CH55+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch55+HD+EXT),item, False)
item = xbmcgui.ListItem(ch56,ADDON.getLocalizedString(30001),iconImage=IMG+CH56+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch56+HD+EXT),item, False)
item = xbmcgui.ListItem(ch57,ADDON.getLocalizedString(30001),iconImage=IMG+CH57+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch57+HD+EXT),item, False)
item = xbmcgui.ListItem(ch58,ADDON.getLocalizedString(30001),iconImage=IMG+CH58+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch58+HD+EXT),item, False)
item = xbmcgui.ListItem(ch59,ADDON.getLocalizedString(30001),iconImage=IMG+CH59+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch59+HD+EXT),item, False)
item = xbmcgui.ListItem(ch60,ADDON.getLocalizedString(30001),iconImage=IMG+CH60+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch60+HD+EXT),item, False)
item = xbmcgui.ListItem(ch61,ADDON.getLocalizedString(30001),iconImage=IMG+CH61+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch61+HD+EXT),item, False)
item = xbmcgui.ListItem(ch62,ADDON.getLocalizedString(30001),iconImage=IMG+CH62+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch62+HD+EXT),item, False)
item = xbmcgui.ListItem(ch63,ADDON.getLocalizedString(30001),iconImage=IMG+CH63+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch63+HD+EXT),item, False)
item = xbmcgui.ListItem(ch64,ADDON.getLocalizedString(30001),iconImage=IMG+CH64+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch64+HD+EXT),item, False)
item = xbmcgui.ListItem(ch65,ADDON.getLocalizedString(30001),iconImage=IMG+CH65+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch65+HD+EXT),item, False)
item = xbmcgui.ListItem(ch66,ADDON.getLocalizedString(30001),iconImage=IMG+CH66+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch66+HD+EXT),item, False)
item = xbmcgui.ListItem(ch67,ADDON.getLocalizedString(30001),iconImage=IMG+CH67+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch67+HD+EXT),item, False)
item = xbmcgui.ListItem(ch68,ADDON.getLocalizedString(30001),iconImage=IMG+CH68+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch68+HD+EXT),item, False)
item = xbmcgui.ListItem(ch69,ADDON.getLocalizedString(30001),iconImage=IMG+CH69+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch69+HD+EXT),item, False)
item = xbmcgui.ListItem(ch70,ADDON.getLocalizedString(30001),iconImage=IMG+CH70+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch70+HD+EXT),item, False)
item = xbmcgui.ListItem(ch71,ADDON.getLocalizedString(30001),iconImage=IMG+CH71+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch71+HD+EXT),item, False)
item = xbmcgui.ListItem(ch72,ADDON.getLocalizedString(30001),iconImage=IMG+CH72+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch72+HD+EXT),item, False)
item = xbmcgui.ListItem(ch73,ADDON.getLocalizedString(30001),iconImage=IMG+CH73+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch73+HD+EXT),item, False)
item = xbmcgui.ListItem(ch74,ADDON.getLocalizedString(30001),iconImage=IMG+CH74+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch74+HD+EXT),item, False)
item = xbmcgui.ListItem(ch75,ADDON.getLocalizedString(30001),iconImage=IMG+CH75+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch75+HD+EXT),item, False)
item = xbmcgui.ListItem(ch76,ADDON.getLocalizedString(30001),iconImage=IMG+CH76+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch76+HD+EXT),item, False)
item = xbmcgui.ListItem(ch77,ADDON.getLocalizedString(30001),iconImage=IMG+CH77+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch77+HD+EXT),item, False)
item = xbmcgui.ListItem(ch78,ADDON.getLocalizedString(30001),iconImage=IMG+CH78+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch78+HD+EXT),item, False)
item = xbmcgui.ListItem(ch79,ADDON.getLocalizedString(30001),iconImage=IMG+CH79+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch79+HD+EXT),item, False)
item = xbmcgui.ListItem(ch80,ADDON.getLocalizedString(30001),iconImage=IMG+CH80+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch80+HD+EXT),item, False)
item = xbmcgui.ListItem(ch81,ADDON.getLocalizedString(30001),iconImage=IMG+CH81+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch81+HD+EXT),item, False)
item = xbmcgui.ListItem(ch82,ADDON.getLocalizedString(30001),iconImage=IMG+CH82+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch82+HD+EXT),item, False)
item = xbmcgui.ListItem(ch83,ADDON.getLocalizedString(30001),iconImage=IMG+CH83+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch83+HD+EXT),item, False)
item = xbmcgui.ListItem(ch84,ADDON.getLocalizedString(30001),iconImage=IMG+CH84+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch84+HD+EXT),item, False)
item = xbmcgui.ListItem(ch85,ADDON.getLocalizedString(30001),iconImage=IMG+CH85+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch85+HD+EXT),item, False)
item = xbmcgui.ListItem(ch86,ADDON.getLocalizedString(30001),iconImage=IMG+CH86+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch86+HD+EXT),item, False)
item = xbmcgui.ListItem(ch87,ADDON.getLocalizedString(30001),iconImage=IMG+CH87+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch87+HD+EXT),item, False)
item = xbmcgui.ListItem(ch88,ADDON.getLocalizedString(30001),iconImage=IMG+CH88+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch88+HD+EXT),item, False)
item = xbmcgui.ListItem(ch89,ADDON.getLocalizedString(30001),iconImage=IMG+CH89+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch89+HD+EXT),item, False)
item = xbmcgui.ListItem(ch90,ADDON.getLocalizedString(30001),iconImage=IMG+CH90+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch90+HD+EXT),item, False)
item = xbmcgui.ListItem(ch91,ADDON.getLocalizedString(30001),iconImage=IMG+CH91+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch91+HD+EXT),item, False)
item = xbmcgui.ListItem(ch92,ADDON.getLocalizedString(30001),iconImage=IMG+CH92+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch92+HD+EXT),item, False)
item = xbmcgui.ListItem(ch93,ADDON.getLocalizedString(30001),iconImage=IMG+CH93+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch93+HD+EXT),item, False)
item = xbmcgui.ListItem(ch94,ADDON.getLocalizedString(30001),iconImage=IMG+CH94+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch94+HD+EXT),item, False)
item = xbmcgui.ListItem(ch95,ADDON.getLocalizedString(30001),iconImage=IMG+CH95+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch95+HD+EXT),item, False)
item = xbmcgui.ListItem(ch96,ADDON.getLocalizedString(30001),iconImage=IMG+CH96+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch96+HD+EXT),item, False)
item = xbmcgui.ListItem(ch97,ADDON.getLocalizedString(30001),iconImage=IMG+CH97+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch97+HD+EXT),item, False)
item = xbmcgui.ListItem(ch98,ADDON.getLocalizedString(30001),iconImage=IMG+CH98+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch98+HD+EXT),item, False)
item = xbmcgui.ListItem(ch99,ADDON.getLocalizedString(30001),iconImage=IMG+CH99+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch99+HD+EXT),item, False)
item = xbmcgui.ListItem(ch100,ADDON.getLocalizedString(30001),iconImage=IMG+CH100+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch100+HD+EXT),item, False)
item = xbmcgui.ListItem(ch101,ADDON.getLocalizedString(30001),iconImage=IMG+CH101+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch101+HD+EXT),item, False)
item = xbmcgui.ListItem(ch102,ADDON.getLocalizedString(30001),iconImage=IMG+CH102+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch102+HD+EXT),item, False)
item = xbmcgui.ListItem(ch103,ADDON.getLocalizedString(30001),iconImage=IMG+CH103+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch103+HD+EXT),item, False)
item = xbmcgui.ListItem(ch104,ADDON.getLocalizedString(30001),iconImage=IMG+CH104+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch104+HD+EXT),item, False)
item = xbmcgui.ListItem(ch105,ADDON.getLocalizedString(30001),iconImage=IMG+CH105+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch105+HD+EXT),item, False)
item = xbmcgui.ListItem(ch106,ADDON.getLocalizedString(30001),iconImage=IMG+CH106+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch106+HD+EXT),item, False)
item = xbmcgui.ListItem(ch107,ADDON.getLocalizedString(30001),iconImage=IMG+CH107+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch107+HD+EXT),item, False)
item = xbmcgui.ListItem(ch108,ADDON.getLocalizedString(30001),iconImage=IMG+CH108+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch108+HD+EXT),item, False)
item = xbmcgui.ListItem(ch109,ADDON.getLocalizedString(30001),iconImage=IMG+CH109+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch109+HD+EXT),item, False)
item = xbmcgui.ListItem(ch110,ADDON.getLocalizedString(30001),iconImage=IMG+CH110+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch110+HD+EXT),item, False)
item = xbmcgui.ListItem(ch111,ADDON.getLocalizedString(30001),iconImage=IMG+CH111+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch111+HD+EXT),item, False)
item = xbmcgui.ListItem(ch112,ADDON.getLocalizedString(30001),iconImage=IMG+CH112+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch112+HD+EXT),item, False)
item = xbmcgui.ListItem(ch113,ADDON.getLocalizedString(30001),iconImage=IMG+CH113+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch113+HD+EXT),item, False)
item = xbmcgui.ListItem(ch114,ADDON.getLocalizedString(30001),iconImage=IMG+CH114+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch114+HD+EXT),item, False)
item = xbmcgui.ListItem(ch115,ADDON.getLocalizedString(30001),iconImage=IMG+CH115+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch115+HD+EXT),item, False)
item = xbmcgui.ListItem(ch116,ADDON.getLocalizedString(30001),iconImage=IMG+CH116+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch116+HD+EXT),item, False)
item = xbmcgui.ListItem(ch117,ADDON.getLocalizedString(30001),iconImage=IMG+CH117+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch117+HD+EXT),item, False)
item = xbmcgui.ListItem(ch118,ADDON.getLocalizedString(30001),iconImage=IMG+CH118+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch118+HD+EXT),item, False)
item = xbmcgui.ListItem(ch119,ADDON.getLocalizedString(30001),iconImage=IMG+CH119+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch119+HD+EXT),item, False)
item = xbmcgui.ListItem(ch120,ADDON.getLocalizedString(30001),iconImage=IMG+CH120+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch120+HD+EXT),item, False)
item = xbmcgui.ListItem(ch121,ADDON.getLocalizedString(30001),iconImage=IMG+CH121+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch121+HD+EXT),item, False)
item = xbmcgui.ListItem(ch122,ADDON.getLocalizedString(30001),iconImage=IMG+CH122+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch122+HD+EXT),item, False)
item = xbmcgui.ListItem(ch123,ADDON.getLocalizedString(30001),iconImage=IMG+CH123+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch123+HD+EXT),item, False)
item = xbmcgui.ListItem(ch124,ADDON.getLocalizedString(30001),iconImage=IMG+CH124+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch124+HD+EXT),item, False)
item = xbmcgui.ListItem(ch125,ADDON.getLocalizedString(30001),iconImage=IMG+CH125+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch125+HD+EXT),item, False)
item = xbmcgui.ListItem(ch126,ADDON.getLocalizedString(30001),iconImage=IMG+CH126+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch126+HD+EXT),item, False)
item = xbmcgui.ListItem(ch127,ADDON.getLocalizedString(30001),iconImage=IMG+CH127+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch127+HD+EXT),item, False)
item = xbmcgui.ListItem(ch128,ADDON.getLocalizedString(30001),iconImage=IMG+CH128+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch128+HD+EXT),item, False)
item = xbmcgui.ListItem(ch129,ADDON.getLocalizedString(30001),iconImage=IMG+CH129+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch129+HD+EXT),item, False)
item = xbmcgui.ListItem(ch130,ADDON.getLocalizedString(30001),iconImage=IMG+CH130+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch130+HD+EXT),item, False)
item = xbmcgui.ListItem(ch131,ADDON.getLocalizedString(30001),iconImage=IMG+CH131+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch131+HD+EXT),item, False)
item = xbmcgui.ListItem(ch132,ADDON.getLocalizedString(30001),iconImage=IMG+CH132+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch132+HD+EXT),item, False)
item = xbmcgui.ListItem(ch133,ADDON.getLocalizedString(30001),iconImage=IMG+CH133+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch133+HD+EXT),item, False)
item = xbmcgui.ListItem(ch134,ADDON.getLocalizedString(30001),iconImage=IMG+CH134+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch134+HD+EXT),item, False)
item = xbmcgui.ListItem(ch135,ADDON.getLocalizedString(30001),iconImage=IMG+CH135+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch135+HD+EXT),item, False)
item = xbmcgui.ListItem(ch136,ADDON.getLocalizedString(30001),iconImage=IMG+CH136+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch136+HD+EXT),item, False)
item = xbmcgui.ListItem(ch137,ADDON.getLocalizedString(30001),iconImage=IMG+CH137+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch137+HD+EXT),item, False)
item = xbmcgui.ListItem(ch138,ADDON.getLocalizedString(30001),iconImage=IMG+CH138+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch138+HD+EXT),item, False)
item = xbmcgui.ListItem(ch139,ADDON.getLocalizedString(30001),iconImage=IMG+CH139+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch139+HD+EXT),item, False)
item = xbmcgui.ListItem(ch140,ADDON.getLocalizedString(30001),iconImage=IMG+CH140+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch140+HD+EXT),item, False)
item = xbmcgui.ListItem(ch141,ADDON.getLocalizedString(30001),iconImage=IMG+CH141+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch141+HD+EXT),item, False)
item = xbmcgui.ListItem(ch142,ADDON.getLocalizedString(30001),iconImage=IMG+CH142+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch142+HD+EXT),item, False)
item = xbmcgui.ListItem(ch143,ADDON.getLocalizedString(30001),iconImage=IMG+CH143+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch143+HD+EXT),item, False)
item = xbmcgui.ListItem(ch144,ADDON.getLocalizedString(30001),iconImage=IMG+CH144+EXT2)
xbmcplugin.addDirectoryItem(HANDLE,(BaseUrl+ch144+HD+EXT),item, False)
xbmcplugin.endOfDirectory(HANDLE)