from Consts import *

# Peak that change to hills during the game, like Bogota
lPeakExceptions = [(31, 13), (32, 19), (88, 47), (40, 66)]

def isReborn(iPlayer):
	return gc.getPlayer(iPlayer).isReborn()
	
def getOrElse(dDictionary, key, default):
	if key in dDictionary: return dDictionary[key]
	return default
	
def getArea(iPlayer, tRectangle, dExceptions, bReborn=None, dChangedRectangle={}, dChangedExceptions={}):
	if bReborn is None: bReborn = isReborn(iPlayer)
	tBL, tTR = tRectangle[iPlayer]
	lExceptions = getOrElse(dExceptions, iPlayer, [])
	
	if bReborn:
		if iPlayer in dChangedRectangle:
			tBL, tTR = dChangedRectangle[iPlayer]
			lExceptions = getOrElse(dChangedExceptions, iPlayer, [])
	
	left, bottom = tBL
	right, top = tTR		
	return [(x, y) for x in range(left, right+1) for y in range(bottom, top+1) if (x, y) not in lExceptions]

def getCapital(iPlayer, bReborn=None):
	if bReborn is None: bReborn = isReborn(iPlayer)
	if bReborn and iPlayer in dChangedCapitals:
		return dChangedCapitals[iPlayer]
	return tCapitals[iPlayer]
	
def getRespawnCapital(iPlayer, bReborn=None):
	if iPlayer in dRespawnCapitals: return dRespawnCapitals[iPlayer]
	return getCapital(iPlayer, bReborn)
	
def getNewCapital(iPlayer, bReborn=None):
	if iPlayer in dNewCapitals: return dNewCapitals[iPlayer]
	return getRespawnCapital(iPlayer, bReborn)
	
def getBirthArea(iPlayer):
	return getArea(iPlayer, tBirthArea, dBirthAreaExceptions)
	
def getBirthRectangle(iPlayer, bExtended = None):
	if bExtended is None: bExtended = isExtendedBirth(iPlayer)
	if iPlayer in dChangedBirthArea and bExtended:
		return dChangedBirthArea[iPlayer]
	return tBirthArea[iPlayer]
	
def getBirthExceptions(iPlayer):
	if iPlayer in dBirthAreaExceptions: return dBirthAreaExceptions[iPlayer]
	return []
	
def getCoreArea(iPlayer, bReborn=None):
	return getArea(iPlayer, tCoreArea, dCoreAreaExceptions, bReborn, dChangedCoreArea, dChangedCoreAreaExceptions)
	
def getNormalArea(iPlayer, bReborn=None):
	return getArea(iPlayer, tNormalArea, dNormalAreaExceptions, bReborn, dChangedNormalArea, dChangedNormalAreaExceptions)

def getBroaderArea(iPlayer, bReborn=None):
	return getArea(iPlayer, tBroaderArea, {}, dChangedBroaderArea)
	
def getRespawnArea(iPlayer):
	if iPlayer in dRespawnArea: return getArea(iPlayer, dRespawnArea, {})
	return getNormalArea(iPlayer)
	
def getRebirthArea(iPlayer):
	if iPlayer in dRebirthArea: return getArea(iPlayer, dRebirthArea, dRebirthAreaExceptions)
	return getBirthArea(iPlayer)
	
def updateCore(iPlayer):
	lCore = getCoreArea(iPlayer)
	
	for x in range(iWorldX):
		for y in range(iWorldY):
			plot = gc.getMap().plot(x, y)
			if plot.isWater() or (plot.isPeak() and (x, y) not in lPeakExceptions): continue
			plot.setCore(iPlayer, (x, y) in lCore)
			
def isForeignCore(iPlayer, tPlot):
	x, y = tPlot
	plot = gc.getMap().plot(x, y)
	for iLoopPlayer in range(iNumPlayers):
		if iLoopPlayer == iPlayer: continue
		if plot.isCore(iLoopPlayer):
			return True
	return False
	
def isExtendedBirth(iPlayer):
	if gc.getGame().getActivePlayer() == iPlayer: return False
	
	# add special conditions for extended AI flip zones here
	if iPlayer == iOttomans and pByzantium.isAlive(): return False
	
	return True
			
def init():
	for iPlayer in range(iNumPlayers):
		updateCore(iPlayer)
	
### Capitals ###

tCapitals = (
(69, 33), # Thebes
(76, 40), # Babylon
(87, 40), # Harappa
(25, 23), # Caral
(66, 31), # Kerma
(100, 44), # Chang'an
(67, 41), # Athens
(94, 40), # Pataliputra
(73, 40), # Sur
(62, 49), # Hallstatt
(4, 18), # Tonga
(82, 38), # Persepolis
(60, 44), # Rome
(22, 35), # Tikal
(95, 47), # Dunhuang
(91, 30), # Thanjavur
(72, 30), # Aksum
(101, 37), # Co Loa (Hanoi)
(18, 37), # Tenotihuacan (Tollan)
(4, 59), # Naparyaarmiut
(27, 47), # Erie
(109, 46), # Seoul
(30, 20), # Tiwanaku
(68, 45), # Constantinople
(27, 22), # Cerro Pátapo
(113, 45), # Kyoto
(60, 59), # Oslo
(88, 49), # Orduqent
(75, 33), # Mecca
(96, 43), # Lhasa
(100, 26), # Palembang
(99, 38), # Pagan (Ava, Mandalay)
(77, 48), # Balanjar
(64, 30), # Njimi
(51, 41), # Cordoba
(52, 44), # Madrid
(55, 50), # Paris
(82, 34), # Muscat
(103, 32), # Angkor
(27, 29), # Bacata
(76, 30), # Sana'a
(53, 54), # London
(59, 51), # Frankfurt
(69, 52), # Kiev
(65, 48), # Buda
(109, 33), # Tondo (Manila)
(24, 25), # Chan Chan
(72, 19), # Kilwa
(69, 35), # Cairo
(51, 30), # Djenne
(65, 51), # Krakow
(68, 16), # Great Zimbabwe
(49, 43), # Lisboa
(28, 22), # Cuzco
(59, 46), # Florence
(59, 26), # Benin City
(99, 51), # Karakorum
(18, 37), # Tenochtitlan
(90, 40), # Delhi
(70, 43), # Sogut
(73, 54), # Moskow
(101, 33), # Ayutthaya
(62, 20), # Mbanza Kongo
(63, 59), # Stockholm
(57, 53), # Amsterdam
(106,52), # Changchun
(62, 53), # Berlin
(27, 46), # Washington
(34, 11), # Buenos Aires
(41, 18), # Rio de Janeiro
(118, 13),# Sydney
(68, 15), # Pretoria
(30, 52), # Montreal
(73, 38), # Jerusalem
)

dChangedCapitals = {
iNubia : (68, 29),	# Sennar
iChina : (102, 47),	# Beijing
iIndia : (90, 40),	# Delhi
iCarthage : (58, 39),	# Carthage
iPersia : (81, 41),	# Esfahan (Iran)
iYuezhi : (86, 43),	# Bagram (Kabul)
iMississippi : (23, 45), # Cahokia
iKazakh : (84, 52), # Astana
iMaya : (27, 29),	# Bogota (Colombia)
iTamils : (90, 30),	# Vijayanagara
iChad : (64, 28), #N'Djamena
iKhmer : (101, 37),	# Hanoi
iHolyRome : (62, 49),	# Vienna
}

# new capital locations if changed during the game
dNewCapitals = {
iJapan : (116, 46),	# Tokyo
#iVikings : (63, 59),	# Stockholm
iHolyRome : (62, 49),	# Vienna
iItaly : (60, 44),	# Rome
iMongolia : (102, 47),	# Khanbaliq
iOttomans : (68, 45),	# Istanbul
}

# new capital locations on respawn
dRespawnCapitals = {
iChina : (102, 47),	# Beijing
iIndia : (90, 40),	# Delhi
iPersia : (81, 41),	# Esfahan
iKazakh : (84, 50), # Sozak, Turkistan
iEthiopia : (72, 28),	# Addis Ababa
iJapan : (116, 46),	# Tokyo
#iVikings : (63, 59),	# Stockholm
iTurks : (84, 41),	# Herat
iIndonesia : (104, 25),	# Jakarta
iChad : (61, 29),	#Ngazargamu
iMoors : (51, 37),	# Marrakesh
iHolyRome : (62, 49),	# Vienna
iInca : (26, 22),	# Lima
iItaly : (60, 44),	# Rome
iMughals : (85, 37),	# Karachi
iOttomans : (68, 45),	# Istanbul
}

### Birth Area ###

tBirthArea = (
((66, 30), 	(70, 36)), 	# Egypt
((75, 39), 	(77, 42)), 	# Babylonia
((85, 37), 	(88, 41)), 	# Harappa
((25, 23), (25, 23)), 	# Norte Chico
((66, 25), 	(69, 31)), 	# Nubia
((99, 43), 	(107, 47)), 	# China
((65, 39), 	(70, 45)), 	# Greece
((87, 36), 	(96, 40)), 	# India
((71, 39), 	(74, 41)), 	# Carthage
((50, 46),	(66, 51)),	# Celtia
((3, 17), 	(7, 22)), 	# Polynesia
((79, 37), 	(85, 44)), 	# Persia
((58, 41), 	(63, 47)), 	# Rome
((20, 35), 	(23, 37)), 	# Maya
((95, 46),	(99, 48)),	# Yuezhi
((90, 27), 	(93, 32)), 	# Tamils
((70, 27),	(73, 30)),	# Ethiopia
((100, 35),	(104, 39)),	# Vietnam
((15, 36), 	(20, 41)), 	# Teotihuacan
((3, 57), (9, 65)), # Inuit
((24, 46),	(27, 48)), 	# Mississippi
((107, 45), (110, 49)), 	# Korea
((29, 17), (31, 20)),	# Tiwanaku
((64, 38), 	(74, 45)), 	# Byzantium
((27, 20),	(28, 22)),	# Wari
((111, 41), (116, 49)), 	# Japan
((58, 56), 	(64, 62)), 	# Vikings
((79, 45),	(98, 52)),	# Turks
((67, 30), 	(80, 40)), 	# Arabia
((92, 41), 	(98, 45)), 	# Tibet
((98, 24), 	(107, 31)), 	# Indonesia
((97, 37),	(100, 39)),	# Burma
((73, 47),	(77, 51)),	# Khazars
((63, 27), 	(65, 33)), # Chad
((51, 37), 	(58, 43)), 	# Moors
((49, 43), 	(53, 46)), 	# Spain
((51, 46), 	(57, 52)), 	# France
((79, 32),	(82, 35)),	# Oman
((102, 31),	(104, 35)),	# Khmer
((25, 29), (28, 31)),	# Muisca
((74, 29),	(80, 32)),	# Yemen
((52, 53),	(54, 57)),	# England
((58, 48), 	(64, 54)), 	# Holy Rome
((68, 48),	(73, 52)),	# Kievan Rus
((63, 46),	(66, 49)),	# Hungary
((107, 30),	(111, 36)),	# Philippines
((24, 24),	(25, 26)),	# Chimu
((70, 14),	(74, 23)),	# Swahili
((66, 31),	(71, 37)),	# Mamluks
((50, 29), 	(55, 32)), 	# Mali
((63, 50), 	(67, 55)), 	# Poland
((64, 15),	(69, 18)),	# Zimbabwe
((44, 42), 	(50, 44)), 	# Portugal
((26, 20), 	(29, 24)), 	# Inca
((58, 45), 	(63, 47)), 	# Italy
((55, 24),	(61, 28)),	# Nigeria
((87, 46), 	(105, 54)), 	# Mongolia
((15, 36), 	(20, 41)), 	# Aztecs
((86, 38), 	(91, 43)), 	# Mughals
((69, 41), 	(76, 48)), 	# Ottomans
((71, 50), 	(74, 58)), 	# Russia
((100, 31),	(102, 35)),	# Thailand
((61, 19), 	(65, 22)), 	# Congo
((61, 56),	(67, 62)),	# Sweden
((56, 52), 	(58, 54)), 	# Holland
((104, 48),	(110, 55)),	# Manchuria
((58, 49), 	(65, 55)), 	# Germany
((25, 43), 	(32, 50)), 	# America
((31, 3), 	(35, 13)), 	# Argentina
((36, 15), 	(43, 27)), 	# Brazil
((112, 9),	(120, 19)),	# Australia
((66, 13),	(69, 17)),	# Boer
((20, 50), 	(35, 60)), 	# Canada
((72, 37), 	(74, 39)), 	# Israel
)

dChangedBirthArea = {
iCarthage : ((57, 37), (59, 39)),
iPersia :	((74, 37), 	(85, 44)), 	# includes Assyria and Anatolia
iCeltia:	((47, 55),	(54, 60)),
iMississippi :	((22, 42), (25, 48)),
iSpain : 	((49, 43), 	(55, 46)), 	# includes Catalonia
iEngland : 	((50, 53), 	(54, 60)),
iInca : 	((26, 19), 	(31, 24)),
iMongolia : 	((81, 45), 	(105, 54)), 	# 6 more west, 1 more south
iOttomans : 	((67, 41), 	(76, 48)), 	# 2 more west
iArgentina : 	((29, 3), 	(35, 13)), 	# includes Chile
iBoers :	((63, 10),	(69, 17)),	# More of South Africa
iKazakh :	((79, 50),	(89, 54)),
}

dBirthAreaExceptions = {
iBabylonia : [(78, 41), (78, 42)],
iHarappa : [(85, 41), (88, 37), (88, 38)],
iChina : [(106, 47)],
iGreece : [(64, 45), (65, 45), (66, 45)],
iPersia : [(85, 37), (85, 38), (85, 39), (72, 39), (72, 40), (72, 41), (73, 41), (74, 41), (75, 41), (76, 41), (77, 41), (78, 41), (73, 40), (74, 40), (75, 40), (76, 40), (77, 40), (78, 40), (73, 39), (74, 39), (75, 39), (76, 39), (77, 39), (78, 39), (73, 38), (74, 38), (75, 38), (76, 38), (77, 38), (72, 37), (73, 37), (74, 37), (75, 37), (76, 37), (77, 37), (78, 37)],
iCeltia : [(50, 46), (51, 46), (52, 46)],
iRome : [(58, 41), (58, 42), (58, 43)],
iTamils : [(90, 33), (90, 34), (91, 34)],
iTurks : [(95, 45), (96, 45), (97, 45)],
iVietnam : [(103, 39), (104, 38), (104, 39)],
iInuit : [(6, 60), (7, 61), (7, 62), (8, 62), (8, 63), (9, 61), (9, 62), (9, 63), (9, 64)],
iMississippi : [(26, 46), (27, 46)],
iTiwanaku : [(29, 17), (29, 18)],
iArabia : [(82, 34), (73, 40), (71, 36), (72, 37), (67, 30), (68, 30), (69, 30), (70, 30), (71, 30), (72, 30), (72, 31), (72, 32), (71, 32)],
iTibet : [(98, 42)],
iIndonesia : [(100, 31), (100, 30), (101, 29), (101, 30)],
iBurma : [(97, 37), (100, 34)],
iKhazars : [(73, 50), (73, 51), (74, 51), (75, 51), (77, 51), (73, 48), (73, 47), (74, 47), (75, 47), (76, 47), (77, 47)],
iMoors : [(58, 43), (58, 42)],
iSpain : [(49, 41), (49, 42), (49, 43), (49, 44), (50, 43), (50, 44), (50, 42)],
iFrance : [(55, 46), (57, 46), (56, 45), (57, 45), (58, 48), (58, 49), (58, 50), (53, 46), (52, 46), (51, 46), (57, 46), (56, 52), (57, 52)],
iOman : [(79, 34), (79, 35), (81, 32), (82, 32), (82, 33), (80, 35), (82, 35)],
iKhmer : [(103, 35), (104, 33), (104, 34), (104, 35)],
iYemen : [(80, 32), (75, 32), (74, 32), (74, 31), (75, 31), (74, 29)],
iHolyRome : [(64, 51), (64, 52), (64, 53), (64, 54)],
iKievanRus : [(73, 51), (73, 52), (69, 48), (70, 48), (70, 49), (71, 48), (73, 48)],
iHungary : [(63, 48), (63, 49), (64, 46), (65, 46), (66, 46)],
iPoland : [(63, 50), (64, 50)],
iItaly : [(63,47), (63,46)],
iMongolia : [(99, 47), (100, 47), (101, 47), (102, 47), (103, 47), (99, 46), (100, 46), (101, 46), (102, 46), (103, 46), (104, 46), (99, 45), (100, 45), (101, 45), (102, 45), (103, 45), (104, 45), (105, 45), (106, 45)],
iMughals : [(92, 43), (93, 42), (93, 43), (94, 42), (94, 43)],
iOttomans : [(74, 48), (75, 48), (76, 48), (75, 47), (75, 48), (76, 41)],
iRussia : [(68, 58), (69, 58), (70, 58), (65, 55), (66, 55), (66, 56)],
iSweden : [(61, 56), (61, 57), (61, 59), (61, 60), (61, 61), (61, 62), (62, 61), (62, 62), (63, 62), (63, 56), (64, 56), (65, 56), (66, 56), (67, 56), (66, 57), (67, 57), (66, 58), (67, 58), (67, 60)],
iNetherlands : [(57, 51), (58, 51)],
iManchuria : [(107, 48), (108, 48), (108, 49), (109, 48), (109, 49), (110, 48), (110, 49)],
iGermany : [(62, 49), (62, 50), (63, 49), (63, 50), (64, 49), (64, 50), (64, 51), (65, 49), (65, 50), (65, 51), (66, 49), (66, 50), (66, 51), (58, 52), (58, 53), (62, 51), (63, 51), (64, 53), (61, 49), (61, 50), (64, 52), (58, 54), (65, 52), (65, 53)],
iAmerica : [(25, 48), (25, 49), (25, 50), (26, 48), (26, 49), (27, 49), (27, 50), (28, 50), (29, 50), (30, 50)],
iArgentina : [(35, 4), (35, 12), (35, 13), (36, 12), (36, 13)],
iBrazil : [(36, 15), (36, 16)],
iBoers : [(63, 13), (63, 14), (63, 15), (63, 16), (63, 17), (64, 13), (64, 14), (64, 15), (64, 16), (64, 17), (65, 13), (65, 14), (65, 15), (65, 16), (65, 17)],
iCanada : [(20, 50), (21, 50), (22, 50), (23, 50), (24, 50), (25, 50), (29, 50), (30, 50), (31, 50), (32, 50), (20, 51), (21, 51), (22, 51), (23, 51), (24, 51), (32, 51), (35, 53), (35, 54), (34, 55), (34, 56), (33, 56), (33, 57)],
}

### Core Area ###

tCoreArea = (
((67, 32),	(69, 36)),	# Egypt
((75, 39),	(77, 42)),	# Babylonia
((85, 37),	(88, 41)),	# Harappa
((25, 23), (25, 23)), 	# Norte Chico
((66, 29),	(70, 31)),	# Nubia
((99, 43),	(107, 47)),	# China
((64, 39),	(70, 45)),	# Greece
((90, 38),	(96, 40)),	# India
((73, 39),	(74, 41)),	# Phoenicia
((56, 47),	(62, 50)),	# Celtia
((4, 18),	(6, 21)),	# Polynesia
((79, 37),	(85, 44)),	# Persia
((59, 41),	(63, 47)),	# Rome
((21, 35),	(23, 37)),	# Maya
((95, 46),	(99, 48)),	# Yuezhi
((90, 27),	(93, 32)),	# Tamils
((70, 27),	(73, 30)),	# Ethiopia
((100, 35),	(104, 38)),	# Vietnam
((17, 36),	(19, 37)),	# Teotihuacan
((3, 57),	(123, 65)), # Inuit
((24, 46),	(27, 48)), 	# Mississippi
((108, 45),	(110, 48)),	# Korea
((29, 18),	(31, 20)),	# Tiwanaku
((64, 40),	(72, 46)),	# Byzantium
((27, 20),	(28, 22)),	# Wari
((112, 45),	(116, 47)),	# Japan
((58, 56),	(64, 62)),	# Vikings
((81, 44),	(89, 51)),	# Turks
((72, 33),	(78, 42)),	# Arabia
((92, 42),	(98, 45)),	# Tibet
((98, 24),	(107, 30)),	# Indonesia
((98, 35),	(99, 38)),	# Burma
((73, 47),	(77, 50)),	# Khazars
((61, 28), 	(64, 32)), # Chad
((51, 37),	(53, 42)),	# Moors
((49, 43),	(53, 46)),	# Spain
((51, 46),	(57, 51)),	# France
((79, 32),	(82, 35)),	# Oman
((100, 32),	(103, 36)),	# Khmer
((27, 29),	(27, 29)),	# Muisca
((75, 30),	(79, 33)),	# Yemen
((52, 53),	(54, 57)),	# England
((58, 49),	(63, 52)),	# HolyRome
((69, 48),	(73, 52)),	# Kievan Rus
((63, 45),	(66, 49)),	# Hungary
((108, 30),	(110, 36)),	# Philippines
((24, 24),	(25, 28)),	# Chimu
((70, 16),	(72, 23)),	# Swahili
((67, 32),	(71, 36)),	# Mamluks
((50, 29), 	(55, 32)), 	# Mali
((63, 50),	(67, 55)),	# Poland
((65, 15),	(69, 17)),	# Zimbabwe
((44, 42),	(50, 44)),	# Portugal
((26, 20),	(28, 22)),	# Inca
((58, 45),	(62, 47)),	# Italy
((56, 25),	(61, 28)),	# Nigeria
((95, 47),	(105, 52)),	# Mongolia
((16, 35),	(19, 38)),	# Aztecs
((86, 38),	(91, 43)),	# Mughals
((69, 42),	(76, 46)),	# Ottomans
((68, 49),	(75, 59)),	# Russia
((100, 32),	(103, 36)),	# Thailand
((61, 19),	(65, 22)),	# Congo
((61, 56),	(68, 63)),	# Sweden
((56, 52),	(58, 54)),	# Netherlands
((104, 48),	(108, 54)),	# Manchuria
((58, 49),	(65, 55)),	# Germany
((23, 45),	(32, 50)),	# America
((31, 6),	(35, 12)),	# Argentina
((37, 15),	(41, 22)),	# Brazil
((112, 10),	(118, 18)),	# Australia
((62, 10),	(70, 17)),	# Boer
((27, 50),	(35, 52)),	# Canada
((72, 37), 	(73, 39)), 	# Israel
)

dChangedCoreArea = {
iChina : 	((99, 42),	(107, 47)),
iGreece :	((65, 39), 	(69, 42)),
iIndia : 	((88, 33),	(91, 38)),
iPhoenicia:	((54, 37),	(60, 39)),
iPersia:	((79, 38), 	(82, 42)), 	# Iran
iCeltia:	((48, 55),	(53, 60)), # Ireland
iMaya : 	((24, 26),	(31, 32)),	# Colombia
iYuezhi :	((83, 41),	(86, 48)),	# Kushan
iMississippi :	((22, 42), (24, 48)),
iByzantium :	((67, 44),	(69, 46)),
iJapan : 	((111, 41),	(116, 49)),
iTurks : 	((79, 37),	(85, 44)),
iArabia :	((73, 30),	(82, 36)),
iKazakh :	((79, 49), (89, 54)),
iMoors : 	((51, 37),	(56, 39)),
iSpain : 	((49, 40),	(55, 46)),
iEngland : 	((50, 53),	(54, 60)),
iHolyRome : 	((61, 46),	(66, 51)),
iItaly : 	((58, 40),	(63, 47)),
iMongolia : 	((95, 46),	(106, 52)),
iAztecs : 	((16, 35),	(19, 40)),	# Mexico
iMughals : 	((86, 37),	(94, 43)),
iOttomans : 	((67, 42),	(76, 47)),
iManchuria :	((100, 46),	(108, 54)),
iGermany : 	((58, 49),	(63, 55)),
}

dCoreAreaExceptions = {
iHarappa : [(85, 41), (88, 37), (88, 38)],
iNubia : [(70, 30), (70, 29)],
iChina : [(99, 46), (99, 47), (104, 43), (105, 43), (106, 43), (107, 43), (105, 44), (106, 44), (106, 47)],
iGreece : [(64, 45), (65, 45)],
iPersia : [(85, 37), (85, 38), (85, 39)],
iCeltia : [(56, 49), (56, 50), (56, 51), (57, 51), (58, 51),(59, 51), (60, 51), (63, 47), (63, 51), (62, 50), (57, 50)],
iYuezhi : [(97, 48), (98, 48), (99, 48), (99, 47)],
iByzantium : [(71, 40)],
iInuit : [(6, 60), (7, 61), (7, 62), (8, 62), (8, 63), (9, 61), (9, 62), (9, 64), (10, 60), (10, 61), (10, 63), (10, 64), (11, 57), (11, 59), (11, 60), (11, 61), (11, 62), (11, 63), (12, 57), (12, 58), (12, 60), (12, 61), (12, 62), (12, 63), (13, 59), (13, 60), (13, 61), (13, 62), (13, 63), (13, 64), (13, 65), (14, 57), (14, 58), (14, 59), (14, 60), (14, 61), (14, 64), (14, 65), (15, 57), (15, 58), (15, 59), (15, 60), (15, 61), (15, 64), (15, 65), (16, 57), (16, 58), (16, 59), (16, 61), (16, 62), (16, 64), (16, 65), (17, 57), (17, 59), (17, 62), (17, 63), (17, 64), (17, 65), (18, 57), (18, 59), (18, 61), (18, 62), (18, 63), (19, 57), (19, 58), (19, 59), (19, 60), (19, 61), (19, 62), (19, 63), (19, 65), (20, 58), (20, 59), (20, 60), (20, 61), (20, 62), (20, 63), (20, 65), (21, 57), (21, 58), (21, 59), (21, 61), (21, 62), (21, 63), (22, 57), (22, 58), (22, 59), (22, 60), (22, 61), (22, 62), (23, 57), (23, 58), (23, 59), (23, 60), (23, 61), (23, 62), (23, 65), (24, 60), (24, 61), (24, 62), (25, 61), (25, 62), (25, 63), (25, 65), (26, 62), (26, 63), (26, 64), (27, 61), (29, 57), (29, 58), (29, 59), (29, 60), (30, 57), (30, 58), (30, 59), (30, 60), (30, 62), (30, 65), (31, 57), (31, 58), (31, 62), (31, 63), (31, 64), (31, 65), (32, 57), (32, 58), (32, 61), (32, 62), (32, 63), (32, 64), (33, 57), (33, 61), (33, 65), (34, 63), (34, 64), (38, 63), (38, 64), (38, 65), (39, 61), (39, 62), (39, 63), (39, 64), (39, 65), (40, 60), (40, 61), (40, 62), (40, 63), (40, 64), (40, 65), (41, 60), (41, 61), (41, 62), (41, 63), (41, 64), (41, 65), (42, 63), (42, 64), (42, 65), (44, 64), (45, 62), (45, 63), (46, 63), (47, 63), (48, 57), (49, 57), (49, 58), (51, 58), (51, 59), (51, 60), (52, 57), (52, 58), (52, 59), (52, 60), (53, 57), (53, 59), (58, 59), (58, 61), (59, 57), (59, 59), (59, 61), (60, 59), (60, 60), (60, 62), (61, 58), (61, 59), (61, 60), (61, 61), (61, 63), (62, 57), (62, 59), (62, 60), (62, 61), (62, 62), (63, 57), (63, 58), (63, 59), (63, 60), (63, 61), (63, 62), (63, 64), (64, 61), (64, 62), (64, 63), (65, 62), (65, 63), (65, 64), (65, 65), (66, 57), (66, 59), (66, 60), (66, 61), (66, 62), (66, 63), (66, 64), (66, 65), (67, 57), (67, 59), (67, 61), (67, 62), (67, 63), (67, 64), (67, 65), (68, 57), (68, 59), (68, 60), (68, 61), (68, 62), (68, 63), (68, 64), (69, 57), (69, 58), (69, 59), (69, 60), (69, 61), (69, 63), (69, 64), (70, 57), (70, 59), (70, 60), (70, 61), (70, 63), (71, 57), (71, 58), (71, 60), (72, 57), (72, 58), (72, 59), (72, 60), (72, 61), (72, 62), (73, 57), (73, 58), (73, 59), (73, 60), (73, 61), (73, 62), (74, 57), (74, 58), (74, 59), (74, 60), (74, 61), (75, 57), (75, 58), (75, 59), (75, 60), (75, 61), (75, 62), (76, 57), (76, 58), (76, 59), (76, 60), (76, 61), (76, 62), (76, 64), (76, 65), (77, 57), (77, 58), (77, 59), (77, 60), (77, 61), (77, 62), (77, 65), (78, 57), (78, 58), (78, 59), (78, 60), (78, 61), (78, 62), (78, 63), (79, 57), (79, 58), (79, 59), (79, 60), (79, 61), (79, 62), (80, 57), (80, 58), (80, 59), (80, 60), (80, 61), (80, 62), (80, 63), (81, 60), (81, 61), (81, 62), (81, 63), (82, 57), (82, 58), (82, 59), (82, 60), (82, 62), (82, 63), (83, 57), (83, 58), (83, 59), (83, 60), (83, 61), (83, 62), (84, 57), (84, 58), (84, 59), (84, 60), (84, 61), (84, 62), (84, 63), (84, 64), (84, 65), (85, 57), (85, 58), (85, 59), (85, 60), (85, 61), (85, 62), (86, 57), (86, 58), (86, 59), (86, 60), (86, 61), (86, 62), (86, 63), (86, 64), (86, 65), (87, 57), (87, 58), (87, 59), (87, 60), (87, 61), (87, 62), (87, 63), (87, 64), (87, 65), (88, 57), (88, 58), (88, 59), (88, 60), (88, 61), (88, 62), (88, 63), (88, 64), (88, 65), (89, 57), (89, 58), (89, 59), (89, 60), (89, 61), (89, 62), (89, 63), (89, 64), (89, 65), (90, 57), (90, 58), (90, 59), (90, 60), (90, 61), (90, 62), (90, 63), (90, 64), (90, 65), (91, 57), (91, 58), (91, 59), (91, 60), (91, 61), (91, 63), (91, 64), (91, 65), (92, 57), (92, 58), (92, 59), (92, 60), (92, 61), (92, 62), (92, 63), (93, 57), (93, 58), (93, 59), (93, 60), (93, 61), (93, 62), (93, 63), (93, 64), (93, 65), (94, 57), (94, 58), (94, 59), (94, 60), (94, 61), (94, 62), (94, 63), (94, 64), (94, 65), (95, 57), (95, 58), (95, 59), (95, 60), (95, 61), (95, 62), (95, 63), (95, 64), (96, 57), (96, 58), (96, 59), (96, 60), (96, 61), (96, 62), (96, 63), (96, 64), (97, 57), (97, 58), (97, 59), (97, 60), (97, 61), (97, 62), (97, 63), (97, 64), (98, 57), (98, 58), (98, 59), (98, 60), (98, 61), (98, 62), (98, 63), (98, 64), (99, 57), (99, 58), (99, 59), (99, 60), (99, 61), (99, 62), (99, 63), (99, 64), (99, 65), (100, 57), (100, 58), (100, 59), (100, 60), (100, 61), (100, 62), (100, 63), (100, 64), (100, 65), (101, 57), (101, 58), (101, 59), (101, 60), (101, 61), (101, 62), (101, 63), (101, 64), (101, 65), (102, 57), (102, 59), (102, 60), (102, 61), (102, 62), (102, 63), (102, 64), (103, 57), (103, 58), (103, 59), (103, 60), (103, 61), (103, 62), (103, 64), (104, 57), (104, 58), (104, 59), (104, 60), (104, 61), (104, 63), (104, 64), (105, 57), (105, 58), (105, 59), (105, 60), (105, 62), (105, 63), (105, 64), (105, 65), (106, 57), (106, 58), (106, 59), (106, 61), (106, 62), (106, 63), (106, 64), (106, 65), (107, 57), (107, 58), (107, 59), (107, 61), (107, 62), (107, 63), (107, 64), (107, 65), (108, 57), (108, 58), (108, 59), (108, 60), (108, 61), (108, 62), (108, 63), (108, 64), (108, 65), (109, 57), (109, 58), (109, 59), (109, 61), (109, 62), (109, 64), (110, 58), (110, 61), (110, 63), (110, 64), (110, 65), (111, 58), (111, 60), (111, 61), (111, 63), (111, 64), (111, 65), (112, 59), (112, 60), (112, 62), (112, 63), (112, 64), (112, 65), (113, 59), (113, 60), (113, 62), (113, 63), (113, 64), (114, 59), (114, 61), (114, 62), (114, 63), (114, 64), (115, 60), (115, 61), (115, 62), (115, 63), (115, 64), (116, 61), (116, 62), (116, 63), (116, 64), (117, 61), (117, 62), (117, 63), (117, 64), (118, 57), (118, 58), (118, 62), (118, 63), (118, 64), (119, 57), (119, 58), (119, 59), (119, 60), (119, 61), (119, 62), (119, 63), (119, 64), (120, 59), (120, 60), (120, 61), (120, 62), (120, 63), (121, 61), (121, 62), (122, 60)],
iMississippi : [(26, 46), (27, 46)],
iTurks : [(84, 36), (84, 37), (85, 36), (85, 37), (85, 38), (85, 39), (88, 44)],
iArabia : [(72, 42), (73, 42), (74, 42), (77, 33), (78, 33), (77, 34), (78, 34), (76, 35), (77, 35), (78, 35), (76, 36), (77, 36), (78, 36), (76, 37), (77, 37), (78, 37)],
iTibet : [(98, 42)],
iIndonesia : [(100, 30), (101, 29), (101, 30)],
iBurma : [(98, 38)],
iKhazars : [(73, 50)],
iSpain : [(49, 43), (49, 44), (50, 43), (50, 44)],
iFrance : [(51, 46), (52, 46), (55, 46), (57, 46)],
iOman : [(79, 34), (79, 35)],
iMuisca : [(26, 29)],
iYemen : [(76, 33), (77, 33), (78, 33), (79, 33)],
iHolyRome : [(61, 52), (62, 52), (63, 52)],
iKievanRus : [(73, 51), (73, 52)],
iHungary : [(63, 48), (63, 49)],
iMamluks : [(71, 32)],
iSwahili : [(70, 22)],
iPoland : [(63, 50), (64, 50)],
iMongolia : [(102, 47), (103, 47)],
iMughals : [(86, 43)],
iRussia : [(68, 49), (68, 59), (69, 49), (69, 59), (70, 59), (71, 49)],
iSweden : [(61, 60), (61, 61), (61, 63), (62, 62), (65, 56), (66, 56), (66, 57), (67, 56), (67, 57), (67, 63), (68, 56), (68, 57), (68, 61), (68, 62), (68, 63)],
iManchuria : [(107, 48), (108, 48), (108, 49)],
iGermany : [(58, 52), (58, 53), (58, 54), (61, 49), (61, 50), (62, 49), (62, 50), (62, 51), (63, 49), (63, 50), (63, 51), (64, 49), (64, 50), (64, 51), (64, 52), (64, 53), (65, 49), (65, 51), (65, 52), (65, 53)],
iAmerica : [(23, 50), (27, 50), (29, 50), (30, 50)],
iArgentina : [(35, 12)],
iBoers : [(62, 16), (62, 17), (63, 15), (63, 16), (63, 17), (64, 15), (64, 16), (64, 17)],
iCanada : [(29, 50), (30, 50), (31, 50), (32, 50), (32, 51)],
}

dChangedCoreAreaExceptions = {
iChina : [(99, 46), (99, 47), (106, 47)],
iGreece : [(64, 45), (65, 45), (66, 46)],
iCeltia : [(51, 55), (52, 55), (52, 56), (52, 57), (53, 55), (53, 56), (53, 57), (54, 56), (54, 67)],
iMaya : [(30, 26), (30, 27), (30, 28), (30, 29), (31, 26), (31, 27)], # Colombia
iYuezhi : [(83, 41), (85, 48), (86, 48)],
iKazakh : [(79, 52), (80, 52), (81, 52), (82, 52), (79, 53), (80, 53), (81, 53), (82, 53), (79, 54), (80, 54), (81, 54), (82, 54)], # Khazar Respawn
iSpain : [(49, 41), (49, 42), (49, 43), (49, 44), (50, 42), (50, 43), (50, 44), (55, 46)],
iHolyRome : [(61, 51), (64, 51), (65, 51), (66, 51)],
iItaly : [(63, 46), (63, 47)],
iAztecs : [(19, 40)], # Mexico
iMughals : [(92, 43), (93, 43), (94, 42), (94, 43)],
iOttomans : [(67, 42), (70, 42), (71, 42), (73, 42), (74, 42), (75, 42)],
iManchuria : [(100, 50), (100, 51), (100, 52), (101, 52), (101, 53), (101, 54), (102, 52), (102, 53), (102, 54), (103, 51), (103, 52), (104, 46), (106, 47), (107, 48), (108, 47), (108, 48), (108, 49)],
iGermany : [(58, 52), (58, 53), (58, 54), (61, 49), (61, 50), (62, 49), (62, 50), (62, 51), (63, 49), (63, 50), (63, 51)],
}

### Normal Area ###

tNormalArea = (
((65, 30), 	(72, 37)), 	# Egypt
((74, 38), 	(79, 44)), 	# Babylonia
((84, 35), 	(88, 42)), 	# Harappa
((25, 23), (25, 23)), 	# Norte Chico
((66, 27), 	(71, 31)), 	# Nubia
((99, 39), 	(108, 50)), 	# China
((64, 39), 	(68, 44)), 	# Greece
((89, 38), 	(96, 42)), 	# India
((72, 39), 	(74, 41)), 	# Carthage
((48, 55), 	(49, 58)), 	# Celtia
((3, 15), 	(13, 21)), 	# Polynesia
((79, 37), 	(86, 46)), 	# Persia
((57, 40), 	(63, 47)), 	# Rome
((20, 32), 	(23, 37)), 	# Maya
((95, 46),	(99, 48)),	# Yuezhi
((90, 28), 	(93, 34)), 	# Tamils
((68, 25), 	(77, 30)), 	# Ethiopia
((101, 35), 	(104, 39)), 	# Vietnam
((15, 35), 	(20, 40)), 	# Teotihuacan
((3, 57), (5, 61)), # Inuit
((24, 46),	(27, 48)), 	# Mississippi
((108, 45), 	(110, 49)), 	# Korea
((29, 17), (31, 20)),	# Tiwanaku
((64, 40), 	(72, 45)), 	# Byzantium
((27, 20),	(28, 22)),	# Wari
((111, 41), 	(116, 52)), 	# Japan
((58, 56), 	(67, 65)), 	# Vikings
((79, 44),	(103, 52)),	# Turks
((72, 30), 	(82, 38)), 	# Arabia
((92, 41), 	(98, 45)), 	# Tibet
((98, 24), 	(113, 31)), 	# Indonesia
((98, 35), 	(99, 39)), 	# Burma
((74, 47), 	(80, 50)), 	# Khazar
((62, 28), 	(65, 33)), # Chad
((51, 37), 	(58, 43)), 	# Moors
((49, 40), 	(55, 46)), 	# Spain
((51, 46), 	(58, 52)), 	# France
((80, 32), 	(82, 35)), 	# Oman
((98, 26), 	(103, 37)), 	# Khmer
((27, 29), (27, 29)),	# Muisca
((76, 30), 	(79, 31)), 	# Yemen
((50, 53), 	(54, 60)), 	# England
((58, 48), 	(65, 54)), 	# Holy Rome
((68, 48),	(72, 52)),	# Kievan Rus
((64, 47),	(66, 49)),	# Hungary
((107, 30),	(111, 36)),	# Philippines
((24, 24),	(25, 26)),	# Chimu
((69, 12),	(77, 23)),	# Swahili
((65, 30), 	(72, 37)), 	# Mamluks
((48, 28), 	(57, 34)), 	# Mali
((63, 50), 	(69, 55)), 	# Poland
((64, 15),	(69, 18)),	# Zimbabwe
((44, 41), 	(50, 44)), 	# Portugal
((24, 14), 	(30, 29)), 	# Inca
((57, 40), 	(63, 47)), 	# Italy
((55, 25),	(61, 28)),	# Nigeria
((92, 48), 	(104, 54)), 	# Mongolia
((15, 35), 	(20, 40)), 	# Aztecs
((86, 37), 	(94, 43)), 	# Mughals
((68, 42), 	(78, 49)), 	# Ottomans
((68, 49), 	(83, 62)), 	# Russia
((99, 31), 	(103, 37)), 	# Thailand
((61, 19), 	(65, 22)), 	# Congo
((58, 55), 	(68, 66)), 	# Sweden
((56, 51), 	(58, 54)), 	# Holland
((104, 48),	(110, 55)),	# Manchuria
((59, 48), 	(66, 55)), 	# Germany
((11, 43), 	(31, 49)), 	# America
((31,  3), 	(36, 15)), 	# Argentina
((32, 14), 	(43, 28)), 	# Brazil
((101, 6),	(123, 23)), # Australia
((60, 8),	(72, 17)),	# Boers
(( 8, 50), 	(37, 67)), 	# Canada
((72, 37), 	(73, 39)), 	# Israel
)

dChangedNormalArea = {
iIndia : 	((96, 42),	(97, 42)),
iCarthage : 	((71, 39),	(74, 41)),
iMississippi :	((22, 42), (25, 48)),
iMaya : 	((24, 26),	(29, 32)), # Colombia
iKhazars : ((79, 50),	(89, 54)),
iArabia : 	((73, 30),	(82, 38)),
iHolyRome : 	((61, 46),	(66, 50)),
}

dNormalAreaExceptions = {
iEgypt : [(72, 37), (70, 30), (71, 30), (72, 30)],
iHarappa : [(84, 41), (84, 42), (84, 43), (85, 41), (85, 42), (85, 43), (86, 43)],
iChina : [(99, 49), (100, 49), (101, 49), (99, 50), (100, 50), (101, 50), (102, 50), (100, 39), (101, 39)],
iIndia : [(93, 42), (94, 42), (95, 42), (96, 42)],
iPolynesia : [(13, 21)],
iPersia : [(86, 39), (86, 38), (86, 37)],
iRome : [(62, 47), (63, 47), (63, 46)],
iYuezhi : [(97, 48), (98, 48), (99, 47), (99, 48)],
iEthiopia : [(76, 30), (77, 30)],
iMississippi : [(26, 46), (27, 46)],
iJapan : [(111, 52), (112, 52), (111, 51)],
iVikings : [(65, 56), (66, 56), (67, 56), (66, 57), (67, 57)],
iTurks : [(88, 44), (93, 44), (94, 44), (95, 44), (96, 44), (97, 44), (98, 44), (95, 45), (96, 45), (97, 45), (100, 44), (101, 44), (102, 44), (103, 44), (100, 45), (101, 45), (102, 45), (103, 45), (99, 46), (101, 46), (102, 46), (103, 46), (99, 47), (100, 47), (101, 47), (102, 47), (103, 47), (99, 48), (100, 48), (101, 48), (102, 48), (103, 48), (100, 49), (101, 49), (102, 49), (103, 49)],
iArabia : [(81, 38), (82, 38), (82, 37)],
iSpain : [(49, 44), (49, 43), (49, 42), (49, 41)],
iFrance : [(51, 46), (52, 46), (53, 46), (58, 47), (58, 46), (58, 51), (58, 52), (57, 52)],
iOman : [(73, 30), (84, 36)],
iYemen : [(73, 30), (84, 36)],
iPoland : [(63, 50), (64, 50)],
iItaly : [(62, 47), (63, 47), (63, 46)],
iMongolia : [(92, 52), (92, 53), (92, 54), (93, 54), (94, 54), (100, 48), (101, 48), (102, 48), (103, 48), (104, 48)],
iAztecs : [(20, 35)],
iRussia : [(80, 49), (68, 62), (68, 61), (68, 60), (68, 59)],
iArgentina : [(35, 12), (35, 13), (36, 12), (36, 13), (36, 14), (36, 15)],
iCanada : [(11,50), (12,50), (13,50), (14,50), (16,50), (17,50), (18,50), (19,50), (20,50), (21,50), (22,50), (23,50), (24,50), (25,50), (29,50), (30,50), (31,50), (32,50), (32,51), (8,59), (8,60), (8,61), (8,62), (8,63), (8,64), (8,65), (9,59), (9,60), (9,61), (9,62), (9,63), (9,64), (9,65), (37,66), (37,67)],
}

dChangedNormalAreaExceptions = {
iChina : [(99, 49), (100, 49), (101, 49), (99, 50), (100, 50), (101, 50), (102, 50)],
}

### Broader Area ###

tBroaderArea = (
((60, 26), 	(74, 38)), 	# Egypt
((72, 37), 	(78, 44)), 	# Babylonia
((90, 40), 	(90, 40)), 	# Harappa
((25, 23), (25, 23)), 	# Norte Chico
((66, 29), 	(69, 31)), 	# Nubia
((95, 39), 	(108, 50)), 	# China
((62, 39), 	(77, 47)), 	# Greece
((85, 28), 	(99, 43)), 	# India
((71, 39), 	(74, 41)), 	# Carthage
((48, 55), 	(54, 60)), 	# Celtia
((1, 15), 	(17, 38)), 	# Polynesia
((70, 37), 	(87, 49)), 	# Persia
((49, 35), 	(73, 50)), 	# Rome
((19, 30), 	(26, 37)), 	# Maya
((95, 46),	(99, 48)),	# Yuezhi
((90, 28), 	(93, 34)), 	# Tamils
((67, 21), 	(77, 30)), 	# Ethiopia
((101, 35), 	(104, 39)), 	# Vietnam
((14, 32), 	(24, 43)), 	# Teotihuacan
((3, 57), (5, 61)), # Inuit
((24, 46),	(27, 48)), 	# Mississippi
((106, 45), 	(110, 52)), 	# Korea
((29, 17), (31, 20)),	# Tiwanaku
((58, 34), 	(74, 45)), 	# Byzantium
((27, 20),	(28, 22)),	# Wari
((110, 40), 	(116, 56)), 	# Japan
((58, 56), 	(71, 65)), 	# Vikings
((79, 44),	(103, 52)),	# Turks
((64, 30), 	(85, 44)), 	# Arabia
((92, 41), 	(98, 45)), 	# Tibet
((98, 24), 	(113, 31)), 	# Indonesia
((97, 37),	(100, 39)),	# Burma
((76, 47),	(77, 50)),	# Khazar
((63, 28), 	(64, 32)), # Chad
((51, 37), 	(58, 43)), 	# Moors
((49, 38), 	(55, 46)), 	# Spain
((49, 44), 	(61, 52)), 	# France
((79, 32),	(82, 35)),	# Oman
((97, 25), 	(105, 39)), 	# Khmer
((27, 29), (27, 29)),	# Muisca
((75, 30),	(79, 32)),	# Yemen
((48, 53), 	(54, 60)), 	# England
((58, 43), 	(64, 54)), 	# Holy Rome
((68, 48),	(73, 52)),	# Kievan Rus
((63, 46),	(66, 49)),	# Hungary
((107, 30),	(111, 36)),	# Philippines
((24, 24),	(25, 26)),	# Chimu
((69, 12),	(77, 23)),	# Swahili
((60, 26), 	(74, 38)), 	# Mamluks
((48, 26), 	(59, 34)), 	# Mali
((63, 50), 	(67, 55)), 	# Poland
((64, 15),	(69, 18)),	# Zimbabwe
((49, 40), 	(51, 45)), 	# Portugal
((24, 14), 	(30, 27)), 	# Inca
((57, 47), 	(65, 47)), 	# Italy
((55, 25),	(61, 28)),	# Nigeria
((82, 44), 	(110, 62)), 	# Mongolia
((14, 32), 	(24, 43)), 	# Aztecs
((86, 37), 	(94, 43)), 	# Mughals
((68, 42), 	(86, 49)), 	# Ottomans
((65, 48), 	(92, 59)), 	# Russia
((97, 25), 	(105, 39)), 	# Thailand
((61, 19), 	(65, 22)), 	# Congo
((58, 55), 	(68, 66)), 	# Sweden
((56, 51), 	(58, 54)), 	# Holland
((104, 48),	(110, 55)),	# Manchuria
((55, 46), 	(67, 57)), 	# Germany
((10, 42), 	(37, 56)), 	# America
((29,  3), 	(36, 15)), 	# Argentina
((32, 14), 	(43, 28)), 	# Brazil
((112, 10),	(118, 20)), # Australia
((60, 8),	(72, 17)),	# Boers
(( 8, 50), 	(37, 67)), 	# Canada
((72, 37), 	(73, 39)), 	# Israel
)

dChangedBroaderArea = {
iMississippi :	((22, 42), (25, 48)),
iMaya :		((33, 32),	(33, 32)),	# Colombia
iByzantium : 	((64, 38),	(74, 45)),
iHolyRome :	((61, 46),	(66, 50)),
iMughals :	((84, 37),	(94, 43)),
}

### Respawn area ###

dRespawnArea = {
iEgypt :	((65, 30),	(71, 38)),
iChina :	((99, 39),	(107, 47)),
iIndia :	((88, 33),	(96, 41)),
iByzantium :	((65, 40),	(69, 46)),
iTurks :	((81, 41),	(86, 48)),
iMoors :	((48, 34),	(58, 39)),
iInca :		((25, 16),	(33, 25)),
iMughals :	((85, 37),	(88, 43)),
}

### Rebirth area ###

dRebirthPlot = {
iPersia : (81, 41),	# Esfahan (Iran)
iMaya : (27, 29),	# Bogota (Colombia)
iAztecs : (18, 37),	# Mexico City (Mexico)
}

dRebirthArea = {
iPersia :	((78, 38),	(86, 43)),	# Iran
iMaya :		((23, 25), 	(31, 32)),	# Colombia
iAztecs :	((11, 34), 	(23, 48)),	# Mexico
}

dRebirthAreaExceptions = {
iAztecs : [(17, 48), (18, 48), (19, 48), (20, 48), (21, 48), (22, 48), (23, 48), (18, 47), (19, 47), (20, 47), (21, 47), (22, 47), (23, 47), (18, 46), (19, 46), (20, 46), (21, 46), (22, 46), (23, 46), (21, 45), (22, 45), (23, 45), (22, 44), (23, 44), (22, 43), (23, 43), (23, 42), (22, 35), (21, 34), (22, 34), (23, 34)],
}