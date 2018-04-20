# Rhye's and Fall of Civilization - Barbarian units and cities

from CvPythonExtensions import *
import CvUtil
import PyHelpers	# LOQ
#import Popup
#import cPickle as pickle
from RFCUtils import utils
from Consts import *
from StoredData import data

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer	# LOQ

# Spawning cities (Leoreth)
# Year, coordinates, owner, name, population, unit type, unit number, religions, forced spawn
tMinorCities = (
(-4000, (72, 43), iIndependent2, 'Kanes', 2, iArcher, 2), 	# Hattians
(-3600, (69, 30), iIndependent2, 'Mero&#235;', 3, iMedjay, 1), 	# Meroe
(-3600, (69, 32), iIndependent2, 'Niwt-Rst', 1, iArcher, 1), 	# Upper Egypt
(-3600, (69, 35), iIndependent2, 'Ineb-Hedj', 1, iArcher, 1), 	# Lower Egypt
(-3000, (69, 43), iIndependent, 'Wilusha', 1, iArcher, 2),	# Troy
(-2700, (73, 40), iIndependent2, 'Tsor', 2, iArcher, 2), 	# Phoenicians
(-2700, (79, 40), iIndependent2, 'Shushan', 1, iArcher, 1), 	# Susa
(-2600, (69, 39), iIndependent2, 'Knossos', 2, iMilitia, 1), 	# Minoans
#(-2500, (77, 42), iIndependent2, 'Ninua', 2, iMilitia, 3), 	# Assyrian Empire
(-2070, (104, 45), iIndependent, 'Zou', 2, -1, -1), 	# Qufu
(-2070, (102, 47), iIndependent2, 'Zhongdu', 2, iSpearman, 1),	# Beijing
(-2000, (85, 47), iIndependent, 'Afrasiyab', 1, iArcher, 1), 	# Samarkand
#(-2000, (92, 39), iIndependent, 'Varanasi', 1, iMilitia, 1), 	# Varanasi
(-1800, (75, 44), iIndependent, 'Rhizos', 1, iChariot, 2),	# Colchis
(-1800, (76, 46), iIndependent, 'Aia', 1, iChariot, 3),	# Colchis
(-1800, (58, 43), iIndependent, 'Nuragic', 1, iArcher, 1),	# Nuragic
(-1600, (70, 41), iIndependent, 'Halikarnassos', 1, iArcher, 2),	# Ankara
(-1500, (73, 38), iIndependent, 'Yerushalayim', 3, iArcher, 2),	# Jerusalem
(-900, (90, 40), iIndependent, 'Indraprastha', 2, iArcher, 1),	# Panchala
(-760, (59, 47), iCeltia, 'Melpum', 2, iArcher, 2),		# Milan
(-733, (61, 40), iGreece, 'Syrakousai', 2, -1, -1),		# Magna Graecia
(-733, (62, 42), iGreece, 'Poseidonia', 2, -1, -1),		# Magna Graecia
(-650, (90, 37), iIndependent, 'Ujjain', 2, iArcher, 1),	# Avanti
(-550, (82, 38), iPersia, 'Parsa', 1, iArcher, 2),	# Parsa
(-550, (95, 37), iIndependent2, 'Tosali', 2, iArcher, 2),	# Kalinga
(-550, (87, 42), iIndependent2, 'Taxila', 2, iArcher, 1),	# Taxila
(-550, (81, 34), iPersia, 'Kryptos Limen', 2, iArcher, 2),	# Musqat
(-495, (105, 43), iIndependent2, 'Yuecheng', 1, iArcher, 2), 	# Nanjing
(-350, (72, 48), iGreece, 'Chersonesos', 2, iArcher, 2),	# Crimaia
(-325, (92, 33), iIndependent2, 'Kanchipuram', 2, iWarElephant, 2),	# Madras
(-300, (105, 49), iBarbarian, 'Simiyan hoton', 2, -1, -1),	# Shenyang
(-300, (91, 30), iIndependent2, 'Tanjapuri', 3, iWarElephant, 3),	# Thanjavur
(-281, (75, 44), iBarbarian, 'Trapezon', 2, iChariot, 5),	# Pontic Kingdom
(-257, (101, 37), iIndependent2, 'Co Loa', 2, iWarElephant, 1), 	# Hanoi
(-214, (105, 39), iIndependent2, 'Panyu', 2, iAxeman, 2), 	# Guangzhou
(-190, (77, 44), iIndependent2, 'Artashat', 1, -1, -1),			# Artaxata
(-100, (95, 47), iBarbarian, 'Dunhuang', 2, iArcher, 1),		# Dunhuang
(-100, (19, 35), iNative, 'Danibaan', 2, iArcher, 1),	# Monte Alb�n
(-75, (89, 46), iBarbarian, 'Kashgar', 2, iArcher, 1),		# Kashgar
(-80, (53, 48), iCeltia, 'Burdigala', 2, -1, -1),			# Bordeaux
(-80, (56, 47), iCeltia, 'Lugodunon', 2, -1, -1),			# Lyon
(-80, (55, 50), iCeltia, 'Lutetia', 2, -1, -1),				# Paris
(-18, (109, 46), iIndependent, 'Hancheng', 2, iCrossbowman, 2),		# Seoul
(100, (89, 34), iIndependent2, 'Pratisthan', 2, iWarElephant, 2),	# Satahavana
(100, (18, 37), iBarbarian, 'Tolan', 2, iJaguar, 2),		# Teotihuacan
(100, (76, 30), iIndependent, "Sana'a", 2, -1, -1),			# Sana'a
(107, (98, 36), iIndependent2, 'Pagan', 2, -1, -1),			# Pagan
(350, (65, 45), iIndependent, 'Singidun', 2, iHeavySpearman, 2),	# Beograd
(470, (53, 51), iIndependent2, 'Caen', 2, -1, -1),	# Caen
(610, (92, 43), iBarbarian, 'Kyunglung', 1, iKhampa, 1),		# Lhasa
(680, (51, 37), iIndependent, 'Marrakus', 1, iCrossbowman, 1),	# Marrakesh
(700, (30, 20), iNative, 'Tiwanaku', 1, -1, -1),			# Tihuanaco
(800, tVienna, iIndependent, 'Vindobona', 1, iCrossbowman, 1),	# Wien
(830, (59, 54), iIndependent, 'Hamburg', 2, iCrossbowman, 1),	# Hamburg
(862, (70, 56), iIndependent, 'Novgorod', 2, iHeavySpearman, 2),# Novgorod
(866, (101, 37), iBarbarian, 'Hanoi', 2, -1, -1),			# Hanoi
(880, (65, 48), iIndependent2, 'Buda', 3, iHorseArcher, 5),		# Budapest
(900, (24, 26), iNative, 'Tucume', 1, iArcher, 2),			# Tucume
(900, (25, 23), iNative, 'Chan Chan', 2, iArcher, 2),		# Chan Chan
(910, (50, 45), iIndependent2, 'Le&#243;n', 1, iHeavySpearman, 2),			# Leon
(943, (52, 58), iIndependent2, 'Scuin', 1, iLongbowman, 2),		# Kingdom of Alba
(990, (49, 56), iCeltia, '&#193;th Cliath', 1, -1, -1),			# Dublin
(1000, (61, 63), iIndependent2, 'Nidaros', 1, iHuscarl, 1),	# Trondheim
(1000, (71, 17), iNative, 'Quelimane', 1, iImpi, 1),		# Quelimane
(1100, (71, 20), iNative, 'Mombasa', 1, iImpi, 1),		# Mombasa
(1200, (77, 55), iBarbarian, 'Qazan', 2, iHorseArcher, 1),		# Kazan
(1255, (65, 55), iBarbarian, 'K&#246;nigsberg', 2, iLancer, 3),		# Kazan
(1400, (104, 33), iIndependent, 'Saigon', 5, iCrossbowman, 3),	# Saigon
(1483, (62, 20), iNative, 'Mbanza Kongo', 1, iPombos, 1),	# Mbanza Kongo
(1744, (77, 34), iArabia, 'Al-Diriyah', 3, iMusketman, 3),	# Nadj
)

# do some research on dates here
tMinorStates = (
	(633, 1400, (96, 43), [iArcher, iSwordsman]),	# Tibet
	(-75, 600, (89, 46), [iHorseman]),		# Kashgar early
	(600, 1600, (89, 46), [iHorseArcher]),		# Kashgar late
	(-75, 600, (85, 47), [iHorseman]),		# Samarkand early
	(600, 1600, (85, 47), [iHorseArcher]),		# Samarkand late
	(-300, 600, (91, 31), [iArcher, iSwordsman, iWarElephant]), # Chola
	(-300, 600, (92, 33), [iArcher, iSwordsman, iWarElephant]), # Chola
	(-300, 900, (105, 49), [iHorseArcher, iSwordsman]), # Jurchen
	(1100, 1500, (60, 44), [iPikeman, iCrossbowman]), # Rome late
	(0, 1100, (60, 44), [iSpearman, iArcher]), # Rome early
)

#handicap level modifier
iHandicapOld = (gc.getGame().getHandicapType() - 1)

class Barbs:
		
	def checkTurn(self, iGameTurn):
		
		#handicap level modifier
		iHandicap = gc.getHandicapInfo(gc.getGame().getHandicapType()).getBarbarianSpawnModifier()
		
		# Leoreth: buff certain cities if independent / barbarian (imported from SoI)
		if iGameTurn % 20 == 10:
			for tMinorState in tMinorStates:
				iStartYear, iEndYear, tPlot, lUnitList = tMinorState
				if utils.isYearIn(iStartYear, iEndYear):
					x, y = tPlot
					plot = gc.getMap().plot(x, y)
					iOwner = plot.getOwner()
					if plot.isCity() and plot.getNumUnits() < 4 and iOwner >= iNumPlayers:
						iUnit = utils.getRandomEntry(lUnitList)
						utils.makeUnit(iUnit, iOwner, tPlot, 1)

		if utils.isYearIn(-3000, -850):
			if iHandicap >= 0:
				self.checkSpawn(iBarbarian, iWarrior, 1, (76, 46), (99, 53), self.spawnMinors, iGameTurn, 5, 0)
			
			self.checkSpawn(iBarbarian, iWolf, 1, (75, 54), (104, 64), self.spawnNatives, iGameTurn, 5, 2)
			self.checkSpawn(iBarbarian, iBear, 1, (75, 54), (104, 64), self.spawnNatives, iGameTurn, 5, 4)
			self.checkLimitedSpawn(iBarbarian, iLion, 1, 5, (60, 10), (72, 28), self.spawnNatives, iGameTurn, 5, 1)
			self.checkLimitedSpawn(iBarbarian, iPanther, 1, 5, (60, 10), (72, 28), self.spawnNatives, iGameTurn, 5, 3)

		#Hyksos
		if utils.isYearIn(-1800, -1500):
			self.checkSpawn(iBarbarian, iWarChariot, 2 + iHandicap, (67, 36), (71, 37), self.spawnInvaders, iGameTurn, 8 - iHandicap, 4, ["TXT_KEY_ADJECTIVE_HYKSOS"])
		
		
		#celts
		if utils.isYearIn(-650, 200):
			self.checkSpawn(iCeltia, iGallicWarrior, 1, (49, 46), (65, 52), self.spawnMinors, iGameTurn, 6, 0)
			#if iHandicap >= 0:
			#	self.checkSpawn(iCeltia, iAxeman, 1, (49, 46), (65, 52), self.spawnMinors, iGameTurn, 8, 5, ["TXT_KEY_ADJECTIVE_GAUL"])

		#norse
		if utils.isYearIn(-650, 550):
			self.checkSpawn(iBarbarian, iGalley, 1, (50, 49), (61, 55), self.spawnPirates, iGameTurn, 20, 0, ["TXT_KEY_ADJECTIVE_NORSE"])
			
		#mongolia
		if utils.isYearIn(-210, 300):
			self.checkSpawn(iBarbarian, iHorseman, 3 + iHandicap, (94, 48), (104, 54), self.spawnNomads, iGameTurn, 8-iHandicap, 0, ["TXT_KEY_ADJECTIVE_XIONGNU"])
		elif utils.isYearIn(300, 900):
			iNumUnits = 2 + iHandicap
			self.checkSpawn(iBarbarian, iHorseArcher, iNumUnits, (91, 50), (104, 54), self.spawnNomads, iGameTurn, 7-iHandicap, 0, ["TXT_KEY_ADJECTIVE_GOKTURK", "TXT_KEY_ADJECTIVE_UIGHUR"])
		elif utils.isYearIn(900, 1100):
			iNumUnits = 1 + iHandicap
			self.checkSpawn(iBarbarian, iKeshik, iNumUnits, (94, 48), (104, 54), self.spawnInvaders, iGameTurn, 6, 0, ["TXT_KEY_ADJECTIVE_JURCHEN", "TXT_KEY_ADJECTIVE_KHITAN"])
			
		#tibet
		if utils.isYearIn(-350, 200):
			self.checkSpawn(iBarbarian, iLightSwordsman, 1 + iHandicap, (92, 41), (99, 45), self.spawnMinors, iGameTurn, 10-iHandicap, 3, ["TXT_KEY_ADJECTIVE_TIBETAN"])
		elif utils.isYearIn(200, 600):
			self.checkSpawn(iBarbarian, iSwordsman, 1 + iHandicap, (92, 41), (99, 45), self.spawnMinors, iGameTurn, 10-iHandicap, 3, ["TXT_KEY_ADJECTIVE_TIBETAN"])
		elif utils.isYearIn(200, 630):
			self.checkSpawn(iBarbarian, iSwordsman, 1 + iHandicap, (92, 41), (99, 45), self.spawnMinors, iGameTurn, 10-iHandicap, 3, ["TXT_KEY_ADJECTIVE_TIBETAN"])

		# indo aryans
		#if utils.isYearIn(-2100, -1000):
		#	self.checkSpawn(iBarbarian, iChariot, iHandicap, (86, 37), (88, 43), self.spawnInvaders, iGameTurn, 10 - iHandicap, 4, ["TXT_KEY_ADJECTIVE_INDO_ARYAN"])
		
		# Deccan barbarians
		if utils.isYearIn(-300, 1200):
			iUnit = iArcher
			iStrength = iHandicap
			if iGameTurn >= getTurnForYear(-500): iUnit = iAxeman
			if iGameTurn >= getTurnForYear(0): iStrength += 1
			if iGameTurn >= getTurnForYear(200): iUnit = iSwordsman
			
			self.checkSpawn(iBarbarian, iUnit, iStrength, (87, 30), (96, 37), self.spawnInvaders, iGameTurn, 8-iHandicap, 0, ["Hindi"])
			
		# elephants in india pre-tibet
		if utils.isYearIn(-210, 620):
			self.checkSpawn(iBarbarian, iWarElephant, 1, (86, 31), (100, 41), self.spawnInvaders, iGameTurn, 8-iHandicap, 4)

		#Indo-Scythians
		if utils.isYearIn(-200, 400):
			self.checkSpawn(iBarbarian, iHorseman, 2, (84, 40), (90, 43), self.spawnNomads, iGameTurn, 8-iHandicap, 4, ["TXT_KEY_ADJECTIVE_INDO_SCYTHIAN"])

		#Kushana
		if utils.isYearIn(30, 375):
			self.checkSpawn(iBarbarian, iAsvaka, 3+iHandicap, (84, 40), (90, 43), self.spawnInvaders, iGameTurn, 8, 3, ["TXT_KEY_ADJECTIVE_KUSHANA"])

		#Hephtalites
		if utils.isYearIn(440, 670):
			self.checkSpawn(iBarbarian, iHorseArcher, 2+iHandicap, (84, 40), (90, 43), self.spawnInvaders, iGameTurn, 5-iHandicap, 2, ["TXT_KEY_ADJECTIVE_HEPHTHALITE"])

		# Holkans in classical Mesoamerica
		if utils.isYearIn(600, 1000):
			self.checkSpawn(iBarbarian, iHolkan, 1, (17, 31), (25, 37), self.spawnUprising, iGameTurn, 4, 2)
			
		#pirates in Mediterranean
		if utils.isYearIn(-210, 50):
			self.checkSpawn(iBarbarian, iWarGalley, 1, (49, 37), (72, 44), self.spawnPirates, iGameTurn, 8, 0)
		#pirates in Barbary coast
		if not gc.getPlayer(iMoors).isAlive():
			if utils.isYearIn(-50, 700):
				self.checkSpawn(iBarbarian, iWarGalley, 1, (46, 30), (62, 39), self.spawnPirates, iGameTurn, 18, 0)
			elif utils.isYearIn(700, 1400):
				self.checkSpawn(iBarbarian, iWarGalley, 1, (46, 30), (62, 39), self.spawnPirates, iGameTurn, 8, 0)
		#pirates in Indian ocean
		#if utils.isYearIn(-650, 700):
		#	self.checkSpawn(iBarbarian, iWarGalley, 1, (72, 20), (91, 36), self.spawnPirates, iGameTurn, 18, 0)
		if utils.isYearIn(700, 1700):
			self.checkSpawn(iBarbarian, iHeavyGalley, 1, (72, 20), (91, 36), self.spawnPirates, iGameTurn, 10, 0)

		# Leoreth: Barbarians in Anatolia (Hittites), replace Hattusas spawn
		#if utils.isYearIn(-2000, -800):
		#	self.checkSpawn(iBarbarian, iHuluganni, 1 + iHandicap, (68, 42), (74, 45), self.spawnInvaders, iGameTurn, 16, 0, ["TXT_KEY_ADJECTIVE_HITTITE"])

		#barbarians in europe
		if utils.isYearIn(210, 470):
			self.checkSpawn(iBarbarian, iAxeman, 3 + iHandicap, (50, 45), (63, 52), self.spawnInvaders, iGameTurn, 6, 0, ["TXT_KEY_ADJECTIVE_GERMANIC"])
			self.checkSpawn(iBarbarian, iAxeman, 2 + iHandicap, (64, 49), (69, 55), self.spawnInvaders, iGameTurn, 7, 2, ["TXT_KEY_ADJECTIVE_GERMANIC"])
		# Leoreth: begins 100 AD instead of 50 AD
		#if utils.isYearIn(100, 470):
		#	self.checkSpawn(iBarbarian, iSwordsman, 3, (58, 45), (70, 55), self.spawnInvaders, iGameTurn, 8, 5, ["TXT_KEY_ADJECTIVE_GERMANIC"])
		# Migration period:
		if utils.isYearIn(375, 568):
			self.checkSpawn(iBarbarian, iAxeman, 4 + iHandicap, (49, 41), (55, 46), self.spawnInvaders, iGameTurn, 5, 4, ["TXT_KEY_ADJECTIVE_VISIGOTHIC"])
			self.checkSpawn(iBarbarian, iSwordsman, 4 + iHandicap, (49, 41), (55, 46), self.spawnInvaders, iGameTurn, 5, 2, ["TXT_KEY_ADJECTIVE_VISIGOTHIC"])
			self.checkSpawn(iBarbarian, iHorseArcher, 3, (55, 49), (65, 53), self.spawnInvaders, iGameTurn, 5, 0, ["TXT_KEY_ADJECTIVE_HUNNIC"])

		#citis: Lombards in Italy
		if utils.isYearIn(568, 843):
			self.checkSpawn(iBarbarian, iHeavySwordsman, 4 + iHandicap, (60, 40), (63, 45), self.spawnInvaders, iGameTurn, 3, 2, ["TXT_KEY_ADJECTIVE_LOMBARD"])

		#Leoreth: barbarians in Balkans / Black Sea until the High Middle Ages (Bulgarians, Cumans, Pechenegs)
		if utils.isYearIn(680, 1000):
			self.checkSpawn(iBarbarian, iHorseArcher, 3 + iHandicap, (66, 45), (69, 48), self.spawnNomads, iGameTurn, 6, 2, ["TXT_KEY_ADJECTIVE_AVAR", "TXT_KEY_ADJECTIVE_BULGAR"])
		if utils.isYearIn(900, 1200):
			self.checkSpawn(iBarbarian, iHorseArcher, 3 + iHandicap, (68, 48), (78, 50), self.spawnInvaders, iGameTurn, 8, 5, ["TXT_KEY_ADJECTIVE_CUMAN"])
		if utils.isYearIn(1200, 1400):
			self.checkSpawn(iBarbarian, iHorseArcher, 3 + iHandicap, (64, 45), (69, 49), self.spawnMinors, iGameTurn, 6, 2, ["TXT_KEY_ADJECTIVE_BULGAR"])
		
		if utils.getHumanID() == iByzantium:
			if utils.isYearIn(680, 1400):
				self.checkSpawn(iBarbarian, iHorseArcher, 3 + iHandicap, (64, 45), (69, 49), self.spawnInvaders, iGameTurn, 6, 5, ["TXT_KEY_ADJECTIVE_BULGAR"])
		
		#barbarians in central asia
		#if utils.isYearIn(-2500, -609):
			#self.checkSpawn(iBarbarian, iVulture, 2 + iHandicap, (72, 38), (77, 43), self.spawnNomads, iGameTurn, 8-iHandicap, 4, ["TXT_KEY_ADJECTIVE_ASSYRIAN"])
		#el
		if utils.isYearIn(-250, 300):
			self.checkSpawn(iBarbarian, iHorseman, 2 + iHandicap, (79, 41), (84, 49), self.spawnInvaders, iGameTurn, 7-iHandicap, 2, ["TXT_KEY_ADJECTIVE_PARTHIAN"])
		elif utils.isYearIn(300, 700):
			#if utils.getScenario() == i3000BC:  #late start condition
			self.checkSpawn(iBarbarian, iHorseArcher, 4 + iHandicap, (82, 43), (86, 48), self.spawnNomads, iGameTurn, 8-iHandicap, 2, ["TXT_KEY_ADJECTIVE_HEPHTHALITE"])
		elif utils.isYearIn(700, 1040):
			#if utils.getScenario() == i3000BC:  #late start condition
			self.checkSpawn(iBarbarian, iHorseArcher, 2 + iHandicap, (78, 42), (90, 52), self.spawnNomads, iGameTurn, 6-iHandicap, 2, ["TXT_KEY_ADJECTIVE_TURKIC"])

		# late Central Asian barbarians
		iSteppeUnit = iKeshik
		iExtra = iHandicap
		
		if utils.isYearIn(1200, 1600):
			if not utils.getAreaCitiesCiv(iMongolia, utils.getPlotList((70, 48), (80, 59))):
				self.checkSpawn(iBarbarian, iSteppeUnit, 1 + iExtra, (74, 47), (81, 47), self.spawnNomads, iGameTurn, 10-iHandicap, 5, ["TXT_KEY_ADJECTIVE_TATAR", "TXT_KEY_ADJECTIVE_NOGAI"])
		if utils.isYearIn(1400, 1700):
			if utils.getAreaCities(utils.getPlotList((80, 47), (88, 53))):
				self.checkSpawn(iBarbarian, iSteppeUnit, 1 + iExtra, (80, 47), (88, 53), self.spawnNomads, iGameTurn, 10-2*iHandicap, 2, ["TXT_KEY_ADJECTIVE_UZBEK", "TXT_KEY_ADJECTIVE_KAZAKH"])
			
		#barbarians in Elam
		if utils.isYearIn(-1600, -1000):
			self.checkSpawn(iBarbarian, iChariot, 1, (81, 37), (87, 45), self.spawnMinors, iGameTurn, 9-iHandicap, 0, ["TXT_KEY_ADJECTIVE_ELAMITE"])

		#barbarians in north africa
		if utils.isYearIn(-210, 50):
			self.checkSpawn(iBarbarian, iNumidianCavalry, 1, (54, 31), (67, 35), self.spawnNomads, iGameTurn, 9-iHandicap, 3, ["TXT_KEY_ADJECTIVE_BERBER"])
		elif utils.isYearIn(50, 900):
			if utils.getScenario() == i3000BC:  #late start condition
				self.checkSpawn(iBarbarian, iNumidianCavalry, 1 + iHandicap, (54, 31), (67, 35), self.spawnNomads, iGameTurn, 10-iHandicap, 5, ["TXT_KEY_ADJECTIVE_BERBER"])
		elif utils.isYearIn(900, 1800):
			self.checkSpawn(iBarbarian, iCamelArcher, 1, (54, 27), (67, 35), self.spawnNomads, iGameTurn, 10-iHandicap, 4, ["TXT_KEY_ADJECTIVE_BERBER"])
			
		#camels in arabia
		#if utils.isYearIn(190, 550):
		#	self.checkSpawn(iBarbarian, iCamelArcher, 1, (73, 30), (82, 36), self.spawnNomads, iGameTurn, 9-iHandicap, 7, ["TXT_KEY_ADJECTIVE_BEDOUIN"])
		if utils.isYearIn(-800, 1300) and self.includesActiveHuman([iEgypt, iArabia]):
			iNumUnits = iHandicap
			if utils.getScenario() == i3000BC: iNumUnits += 1
			self.checkSpawn(iBarbarian, iMedjay, iNumUnits, (66, 28), (71, 34), self.spawnUprising, iGameTurn, 12, 4, ["TXT_KEY_ADJECTIVE_NUBIAN"])
		if utils.isYearIn(450, 1600):
			if utils.getScenario() == i3000BC:
				self.checkSpawn(iNative, iImpi, 2 + iHandicap, (60, 10), (72, 27), self.spawnNatives, iGameTurn, 10, 4)
			else:
				self.checkSpawn(iNative, iImpi, 2 + iHandicap, (60, 10), (72, 27), self.spawnNatives, iGameTurn, 15, 4)
		elif utils.isYearIn(1600, 1800):
			self.checkSpawn(iNative, iPombos, 2 + iHandicap, (60, 10), (72, 27), self.spawnNatives, iGameTurn, 10, 4)
			
		#west africa
		if utils.isYearIn(450, 1700):
			if iGameTurn < getTurnForYear(1300):
				sAdj = ["TXT_KEY_ADJECTIVE_GHANAIAN"]
			else:
				sAdj = ["TXT_KEY_ADJECTIVE_SONGHAI"]
			self.checkSpawn(iNative, iImpi, 2, (48, 22), (63, 29), self.spawnMinors, iGameTurn, 16, 10, sAdj)
			
		if utils.isYearIn(1200, 1700):
			self.checkSpawn(iBarbarian, iFarari, 1, (48, 26), (65, 37), self.spawnMinors, iGameTurn, 16, 4, sAdj)

		#American natives
		if utils.isYearIn(600, 1100):
			self.checkCampUnitSpawn(iNative, iDogSoldier, 1 + iHandicap, (15, 38), (24, 47), 5)
			if utils.getScenario() == i3000BC:  #late start condition
				self.checkCampUnitSpawn(iNative, iJaguar, 3, (15, 38), (24, 47), 5)
			else:  #late start condition
				self.checkCampUnitSpawn(iNative, iJaguar, 2, (15, 38), (24, 47), 5)
		if utils.isYearIn(1300, 1600):
			self.checkCampUnitSpawn(iNative, iDogSoldier, 2 + iHandicap, (15, 38), (24, 47), 20)
		if utils.isYearIn(1400, 1800):
			self.checkCampUnitSpawn(iNative, iDogSoldier, 1 + iHandicap, (11, 44), (33, 51), 20)
		if utils.isYearIn(1300, 1600):
			if iGameTurn % 18 == 0:
				if not gc.getMap().plot(27, 29).isUnit():
					utils.makeUnitAI(iDogSoldier, iNative, (27, 29), UnitAITypes.UNITAI_ATTACK, 2 + iHandicap)
			elif iGameTurn % 18 == 9:
				if not gc.getMap().plot(30, 13).isUnit():
					utils.makeUnitAI(iDogSoldier, iNative, (30, 13), UnitAITypes.UNITAI_ATTACK, 2 + iHandicap)

		if self.includesActiveHuman([iAmerica, iEngland, iFrance, iAustralia]):
			if utils.isYearIn(1700, 1900):
				self.checkCampUnitSpawn(iNative, iMountedBrave, 1 + iHandicap, (15, 44), (24, 52), 20)

			if utils.isYearIn(1500, 1850):
				self.checkCampUnitSpawn(iNative, iMohawk, 1, (24, 46), (30, 51), 20)
				
			# Rabbits in Australia
			if iGameTurn >= getTurnForYear(1860):
				self.checkSpawn(iBarbarian, iRabbit, 2 + iHandicap, (103, 10), (118, 22), self.spawnRabbits, iGameTurn, 8, 4)

		if utils.isYearIn(600, 1900):
			iMaxCamps = 1
			if data.iFirstNewWorldColony >= 0:
				iMaxCamps += 2
				if self.includesActiveHuman([iAmerica, iEngland, iFrance]):
					iMaxCamps += 1
			if iGameTurn >= getTurnForYear(1750):
				iMaxCamps += 1
				if self.includesActiveHuman([iAmerica, iEngland, iFrance]):
					iMaxCamps += 1
			
			if iGameTurn < getTurnForYear(1400):
				self.checkCampSpawn(iNative, iCampUnit, (15, 38), (24, 47), False, iGameTurn, 10, data.iSeed % 10, iMaxCamps, 7)
			elif iGameTurn < getTurnForYear(1700):
				self.checkCampSpawn(iNative, iCampUnit, (11, 44), (33, 51), False, iGameTurn, 10, data.iSeed % 10, iMaxCamps, 9)
			else:
				self.checkCampSpawn(iNative, iCampUnit, (11, 44), (33, 51), True, iGameTurn, 10, data.iSeed % 10, iMaxCamps, 14)

		#pirates in the Caribbean
		if utils.isYearIn(1600, 1800):
			self.checkSpawn(iNative, iPrivateer, 1, (24, 32), (35, 46), self.spawnPirates, iGameTurn, 5, 0)
		#pirates in Asia
		if utils.isYearIn(1500, 1900):
			self.checkSpawn(iNative, iPrivateer, 1, (72, 24), (110, 36), self.spawnPirates, iGameTurn, 8, 0)

		if iGameTurn < getTurnForYear(tMinorCities[len(tMinorCities)-1][0])+10:
			self.foundMinorCities(iGameTurn)

		if iGameTurn == getTurnForYear(tBirth[iInca]):
			if utils.getHumanID() == iInca:
				utils.makeUnit(iAucac, iNative, (24, 26), 1)
				utils.makeUnit(iAucac, iNative, (25, 23), 1)
				
	def foundMinorCities(self, iGameTurn):
		for i in range(len(tMinorCities)):
			iYear, tPlot, iPlayer, sName, iPopulation, iUnitType, iNumUnits = tMinorCities[i]
			if iGameTurn < getTurnForYear(iYear): return
			if iGameTurn > getTurnForYear(iYear)+10: continue
			if iPlayer == utils.getHumanID(): continue
			
			if data.lMinorCityFounded[i]: continue
			
			x, y = tPlot
			plot = gc.getMap().plot(x, y)
			if plot.isCity(): continue
			
			# special cases
			if not self.canFoundCity(sName): continue
			
			lReligions = []
			lBuildings = []
			iCulture = 10 * (gc.getGame().getCurrentEra() + 1)
			bForceSpawn = True
			
			if sName == 'Kyiv': lReligions = [iOrthodoxy, iCatholicism]
			if iPlayer == iCeltia and utils.getScenario() != i3000BC: iPlayer = iIndependent
			if sName == 'Buda': bForceSpawn = True
			if sName == 'Zou' or sName == 'Zhongdu' or sName == 'Fenghao' or sName == 'Yuecheng':
				lBuildings = [iLibrary, iPaganTemple]
			if sName == 'Ninua' or sName == 'Pratisthan' or 'Aia' or 'Rhizos':
				lBuildings = [iPaganTemple]
			if sName == 'Nuragic':
				lBuildings = [iPaganTemple, iMonument, iLibrary]
			if sName == 'Kolkata':
				lBuildings = [iPaganTemple, iLibrary]
			if sName == 'Tsor':
				lBuildings = [iJewishTemple, iMonument]
				lReligions = [iJudaism]
			if sName == 'Syrakousai':
				lBuildings = [iPaganTemple, iHarbor]
			if sName in ['Lugodunon', 'Burdigala', 'Lutetia']:
				lBuildings = [iDun]
			if sName in ['Hancheng']:
				lBuildings = [iLibrary, iHarbor, iWalls]
			if sName in ['Uruk']:
				lBuildings = [iGranary, iSmokehouse, iPaganTemple]
			if sName in ['Yerushalayim']:
				lBuildings = [iPaganTemple, iLibrary]
			if sName in ['Mero&#235;']:
				lBuildings = [iObelisk, iGranary]
			if sName in ['Singidun', 'Le&#243;n', 'Scuin']:
				lBuildings = [iOrthodoxTemple, iOrthodoxMonastery, iBarracks, iWalls, iCastle]
			if sName in ['Novgorod']:
				lReligions = [iOrthodoxy]
				lBuildings = [iOrthodoxTemple, iWalls, iCastle, iGranary, iMarket]
			if sName in ['K&#246;nigsberg']:
				lBuildings = [iCatholicChurch, iCatholicMonastery, iBarracks, iWalls, iCastle]
			
			if not self.isFreePlot(tPlot, bForceSpawn): continue
			
			utils.evacuate(tPlot)
		
			if self.foundCity(iPlayer, tPlot, sName, iPopulation, iUnitType, iNumUnits, lReligions, lBuildings, iCulture):
				data.lMinorCityFounded[i] = True
		
	def canFoundCity(self, sName):
		if sName == 'Kanchipuram' and utils.getHumanID() == iTamils: return False
		elif sName == 'Tanjapuri' and gc.getPlayer(iTamils).isAlive(): return False
		#elif sName == 'Hamburg' and (utils.getHumanID() == iHolyRome or data.iSeed % 4 == 0): return False
		#elif sName == 'L&#252;beck' and (utils.getHumanID() == iHolyRome or data.iSeed % 4 != 0): return False
		elif sName == 'Rasa' and gc.getPlayer(iTibet).isAlive(): return False
		elif sName == 'Quelimane' and gc.getPlayer(iSwahili).isAlive(): return False
		elif sName == 'Mombasa' and gc.getPlayer(iSwahili).isAlive(): return False
		#elif sName == 'Marrakus' and utils.getScenario() != i3000BC: return False
		
		return True
	
	def foundCity(self, iPlayer, tPlot, sName, iPopulation, iUnitType = -1, iNumUnits = -1, lReligions = [], lBuildings = [], iCulture = 1):
		pPlayer = gc.getPlayer(iPlayer)
		x, y = tPlot
		plot = gc.getMap().plot(x, y)
		plot.setOwner(iPlayer)
		pPlayer.found(x, y)
		
		if plot.isCity():
			city = gc.getMap().plot(x, y).getPlotCity()
			
			city.setName(sName, False)
			city.setPopulation(iPopulation)
			
			plot.changeCulture(iPlayer, iCulture, True)
			city.changeCulture(iPlayer, iCulture, True)
			
			if iNumUnits > 0 and iUnitType > 0:
				utils.makeUnit(iUnitType, iPlayer, tPlot, iNumUnits)
				
			for iReligion in lReligions:
				if gc.getGame().isReligionFounded(iReligion):
					city.setHasReligion(iReligion, True, False, False)
					
			for iBuilding in lBuildings:
				city.setHasRealBuilding(iBuilding, True)
			
			return True
		
		return False
					
	def clearUnits(self, iPlayer, tPlot): # Unused
		lHumanUnits = []
		lOtherUnits = []
	
		for (x, y) in utils.surroundingPlots(tPlot):
			plot = gc.getMap().plot(x, y)
			
			for iUnit in range(plot.getNumUnits()):
				unit = plot.getUnit(iUnit)
				
				if unit.getOwner() == utils.getHumanID():
					lHumanUnits.append(unit)
				else:
					lOtherUnits.append(unit)
						
		capital = gc.getPlayer(utils.getHumanID()).getCapitalCity()
		for unit in lHumanUnits:
			unit.setXY(capital.getX(), capital.getY())
			
		for unit in lOtherUnits:
			utils.makeUnit(unit.getUnitType(), iPlayer, tPlot, 1)
			unit.kill(False, iBarbarian)
				
	def isFreePlot(self, tPlot, bIgnoreCulture = False):
		x, y = tPlot
		plot = gc.getMap().plot(x, y)
		
		# no cultural control over the tile
		if plot.isOwned() and plot.getOwner() < iNumPlayers and not bIgnoreCulture:
			return False
				
		# no city in adjacent tiles
		for (i, j) in utils.surroundingPlots(tPlot):
			currentPlot = gc.getMap().plot(i, j)
			if currentPlot.isCity(): return False
						
		return True
			
	def checkRegion(self, tCity): # Unusued
		cityPlot = gc.getMap().plot(tCity[0], tCity[1])
		iNumUnitsInAPlot = cityPlot.getNumUnits()
##		print iNumUnitsInAPlot
		
		#checks if the plot already belongs to someone
		if cityPlot.isOwned():
			if cityPlot.getOwner() != iBarbarian:
				return (False, -1)
		
##		#checks if there's a unit on the plot
		if iNumUnitsInAPlot > 0:
			for i in range(iNumUnitsInAPlot):
				unit = cityPlot.getUnit(i)
				iOwner = unit.getOwner()
				if iOwner == iBarbarian:
					return (False, tCity[3]+1)
	
		#checks the surroundings and allows only AI units
		for (x, y) in utils.surroundingPlots(tCity[0], tCity[1]):
			currentPlot=gc.getMap().plot(x,y)
			if currentPlot.isCity():
				return (False, -1)
			iNumUnitsInAPlot = currentPlot.getNumUnits()
			if iNumUnitsInAPlot > 0:
				for i in range(iNumUnitsInAPlot):
					unit = currentPlot.getUnit(i)
					iOwner = unit.getOwner()
					pOwner = gc.getPlayer(iOwner)
					if pOwner.isHuman():
						return (False, tCity[3]+1)
		return (True, tCity[3])
	
	
	
	def killNeighbours(self, tCoords): # Unused
		'Kills all units in the neigbbouring tiles of plot (as well as plot itself) so late starters have some space.'
		for (x, y) in utils.surroundingPlots(tCoords):
			killPlot = CyMap().getPlot(x, y)
			for i in range(killPlot.getNumUnits()):
				unit = killPlot.getUnit(0)	# 0 instead of i because killing units changes the indices
				unit.kill(False, iBarbarian)
	
	# Leoreth: check region for number of units first
	def checkLimitedSpawn(self, iPlayer, iUnitType, iNumUnits, iMaxUnits, tTL, tBR, spawnFunction, iTurn, iPeriod, iRest, lAdj=[]):
		if iTurn % utils.getTurns(iPeriod) == iRest:
			lAreaUnits = utils.getAreaUnits(iPlayer, tTL, tBR)
			if len(lAreaUnits) < iMaxUnits:
				self.checkSpawn(iPlayer, iUnitType, iNumUnits, tTL, tBR, spawnFunction, iTurn, iPeriod, iRest, lAdj)
	
	# Leoreth: new ways to spawn barbarians
	def checkSpawn(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, spawnFunction, iTurn, iPeriod, iRest, lAdj=[]):
		if len(lAdj) == 0:
			sAdj = ""
		else:
			sAdj = utils.getRandomEntry(lAdj)
		
		if iTurn % utils.getTurns(iPeriod) == iRest:
			spawnFunction(iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj)
	
	def possibleTiles(self, tTL, tBR, bWater=False, bTerritory=False, bBorder=False, bImpassable=False, bNearCity=False):
		tArea = utils.getPlotList(tTL, tBR)
		lCities = utils.getAreaCities(tArea)
		bIndy = True
		for city in lCities:
			iOwner = city.getOwner()
			if iOwner not in [iBarbarian, iIndependent, iIndependent2, iNative]:
				bIndy = False
				break
		if len(lCities) == 0:
			bIndy = False
		if bIndy:
			return []
		return [tPlot for tPlot in tArea if self.possibleTile(tPlot, bWater, bTerritory, bBorder, bImpassable, bNearCity)]

	def possibleTile(self, tPlot, bWater, bTerritory, bBorder, bImpassable, bNearCity):
		x, y = tPlot
		plot = gc.getMap().plot(x, y)
		lSurrounding = utils.surroundingPlots(tPlot)
		
		# never on peaks
		if plot.isPeak(): return False
		
		# only land or water
		if bWater != plot.isWater(): return False
		
		# only inside territory if specified
		if not bTerritory and plot.getOwner() >= 0: return False
		
		# never directly next to cities
		if [(i, j) for (i, j) in lSurrounding if gc.getMap().plot(i, j).isCity()]: return False
		
		# never on tiles with units
		if plot.isUnit(): return False
		
		# never in marsh (impassable)
		if plot.getFeatureType() == iMarsh: return False
		
		# allow other impassable terrain (ocean, jungle)
		if not bImpassable:
			if plot.getTerrainType() == iOcean: return False
			if plot.getFeatureType() == iJungle: return False
		
		# restrict to borders if specified
		if bBorder and not [(i, j) for (i, j) in lSurrounding if gc.getMap().plot(i, j).getOwner() != plot.getOwner()]: return False
		
		# near a city if specified (next to cities excluded above)
		if bNearCity and not [(i, j) for (i, j) in utils.surroundingPlots(tPlot, 2, lambda (a, b): not gc.getMap().plot(a, b).isCity())]: return False
		
		# not on landmasses without cities
		if not bWater and gc.getMap().getArea(plot.getArea()).getNumCities() == 0: return False
		
		return True
	
	def spawnPirates(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj=""):
		'''Leoreth: spawns all ships at the same coastal spot, out to pillage and disrupt trade, can spawn inside borders'''
		
		lPlots = self.possibleTiles(tTL, tBR, bWater=True, bTerritory=False)
		tPlot = utils.getRandomEntry(lPlots)
		
		if tPlot:
			utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_PIRATE_SEA, iNumUnits, sAdj)
	
	def spawnNatives(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj=""):
		'''Leoreth: outside of territory, in jungles, all dispersed on several plots, out to pillage'''
		
		lPlots = self.possibleTiles(tTL, tBR, bTerritory=False, bImpassable=True)
		
		for i in range(iNumUnits):
			tPlot = utils.getRandomEntry(lPlots)
			if not tPlot: break
			
			lPlots.remove(tPlot)
			utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK, 1, sAdj)
	
	def spawnMinors(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj=""):
		'''Leoreth: represents minor states without ingame cities
				outside of territory, not in jungles, in groups, passive'''
				
		lPlots = self.possibleTiles(tTL, tBR, bTerritory=False)
		tPlot = utils.getRandomEntry(lPlots)
		
		if tPlot:
			utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK, iNumUnits, sAdj)
	
	def spawnNomads(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj=""):
		'''Leoreth: represents aggressive steppe nomads etc.
			    outside of territory, not in jungles, in small groups, target cities'''
		
		lPlots = self.possibleTiles(tTL, tBR, bTerritory=False)
		tPlot = utils.getRandomEntry(lPlots)
		
		if tPlot:
			utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK, iNumUnits, sAdj)

	def spawnInvaders(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj=""):
		'''Leoreth: represents large invasion forces and migration movements
			    inside of territory, not in jungles, in groups, target cities'''
			    
		lPlots = self.possibleTiles(tTL, tBR, bTerritory=True, bBorder=True)
		tPlot = utils.getRandomEntry(lPlots)
		
		if tPlot:
			utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK, iNumUnits, sAdj)
	
	def spawnUprising(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj=""):
		''' Leoreth: represents uprisings of Natives against colonial settlements, especially North America
			     spawns units in a free plot in the second ring of a random target city in the area
			     (also used for units from warring city states in classical Mesoamerica)'''
		
		lPlots = self.possibleTiles(tTL, tBR, bTerritory=True, bNearCity=True)
		tPlot = utils.getRandomEntry(lPlots)
		
		if tPlot:
			utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_ATTACK, iNumUnits, sAdj)

	
	def spawnRabbits(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, sAdj=""):
		''' Merijn: inside territory, dispersed over several plots, pillaging'''
		lPlots = self.possibleTiles(tTL, tBR, bTerritory=True, bNearCity=True)
		
		for i in range(iNumUnits):
			tPlot = utils.getRandomEntry(lPlots)
			if not tPlot: break
			
			lPlots.remove(tPlot)
			utils.makeUnitAI(iUnitType, iPlayer, tPlot, UnitAITypes.UNITAI_PILLAGE, 1, sAdj)
	
	# Merijn: Camp functions	
	def checkCampSpawn(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, bInvasion, iTurn, iPeriod, iRest, iMaxCamps, iStrength):
		if iTurn % utils.getTurns(iPeriod) == iRest:
			unitList = PyPlayer(iPlayer).getUnitsOfType(iCampUnit)
			lPlotList = utils.getPlotList(tTL, tBR)
			
			iCount = 0
			if unitList:
				for unit in unitList:
					x = unit.getX()
					y = unit.getY()
					if (x, y) in lPlotList:
						iCount += 1
			
			if iCount < iMaxCamps:
				self.placeCamp(iPlayer, iUnitType, iNumUnits, tTL, tBR, bInvasion, iStrength)
	
	def checkCampUnitSpawn(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, iChance):
		unitList = PyPlayer(iPlayer).getUnitsOfType(iCampUnit)
		lPlotList = utils.getPlotList(tTL, tBR)
		
		if unitList:
			for unit in unitList:
				if gc.getGame().getSorenRandNum(100, 'Random entry') < iChance:
					x = unit.getX()
					y = unit.getY()
					if (x, y) in lPlotList:
						for i in range(iNumUnits):
							utils.makeUnitAI(iUnitType, iPlayer, (x, y), UnitAITypes.UNITAI_ATTACK, 1)
	
	def placeCamp(self, iPlayer, iUnitType, iNumUnits, tBR, tTL, bInvasion, iStrength):
		lPlots = self.possibleTiles(tTL, tBR, bTerritory=bInvasion)
		
		for i in range(iNumUnits):
			tPlot = utils.getRandomEntry(lPlots)
			if not tPlot: break
			
			lPlots.remove(tPlot)
			
			unit = gc.getPlayer(iPlayer).initUnit(iUnitType, tPlot[0], tPlot[1], UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
			unit.setBaseCombatStr(iStrength)
	
			
	def includesActiveHuman(self, lPlayers):
		return utils.getHumanID() in lPlayers and tBirth[utils.getHumanID()] <= gc.getGame().getGameTurnYear()

	# Merijn: Camp functions
	def checkCampSpawn(self, iPlayer, iUnitType, tTL, tBR, bInvasion, iTurn, iPeriod, iRest, iMaxCamps, iStrength):
		#CyInterface().addMessage(utils.getHumanID(), False, iDuration/2, "Camp spawn check", "", 0, "", ColorTypes(iWhite), -1, -1, True, True)
		if iTurn % utils.getTurns(iPeriod) == iRest:
			iNumCamps = len(PyPlayer(iPlayer).getUnitsOfType(iCampUnit))
			if iNumCamps < iMaxCamps:
				self.placeCamp(iPlayer, iUnitType, tTL, tBR, bInvasion, iStrength)
				
			# code that allows multiple camp areas (currently unused)
			# campList = PyPlayer(iPlayer).getUnitsOfType(iCampUnit)
			# lPlotList = utils.getPlotList(tTL, tBR)
			
			# iNumCamps = 0
			# if campList:
				# for camp in campList:
					# x = camp.getX()
					# y = camp.getY()
					# if (x, y) in lPlotList:
						# iNumCamps += 1
						
			# if iNumCamps < iMaxCamps:
				# self.placeCamp(iPlayer, iUnitType, tTL, tBR, bInvasion, iStrength)

	def checkCampUnitSpawn(self, iPlayer, iUnitType, iNumUnits, tTL, tBR, iChance):
		campList = PyPlayer(iPlayer).getUnitsOfType(iCampUnit)
		lPlotList = utils.getPlotList(tTL, tBR)
		
		if campList:
			for camp in campList:
				x = camp.getX()
				y = camp.getY()
				if (x, y) in lPlotList:
					if gc.getGame().getSorenRandNum(100, 'Random entry') < iChance:
						utils.makeUnitAI(iUnitType, iPlayer, (x, y), UnitAITypes.UNITAI_ATTACK, iNumUnits)
						CyInterface().addMessage(utils.getHumanID(), False, iDuration/2, "Camp units spawn", "", 0, "", ColorTypes(iLime), -1, -1, True, True)
							
	def placeCamp(self, iPlayer, iUnitType, tTL, tBR, bInvasion, iStrength):
		lPlots = self.possibleTiles(tTL, tBR)
		if not lPlots and bInvasion:
			lPlots = self.possibleTiles(tTL, tBR, bTerritory=True)

		tPlot = utils.getRandomEntry(lPlots)
		if tPlot:
			camp = gc.getPlayer(iPlayer).initUnit(iUnitType, tPlot[0], tPlot[1], UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
			camp.setBaseCombatStr(iStrength)
