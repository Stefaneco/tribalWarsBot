proxy = ""
user = ""
password = ""
world = ""
#eg "https://www.plemiona.pl/page/play/pl141"

group_def = "44654"
group_off = "44655"

#def_preset = [9000, 100, 0, 8000, 100, 0, 0, 450, 0, 5, 0]
#safety = [40000, 50000, 50000, 100]

class Village(object):
	def __init__(self, empty_list,upgrading, idd, wood, stone, iron, main, barracks, stable, garage, snob, smith, place, statue, market, wood_b, stone_b, iron_b, farm, storage, wall, storage_cap, farm_cap, workers):
		self.upgrading = upgrading
		self.idd = idd
		self.wood = wood
		self.stone = stone
		self.iron = iron

		self.buildings = empty_list

		self.main = main #0
		self.buildings.append(main)
		self.barracks = barracks #1
		self.buildings.append(barracks)
		self.stable = stable #2 
		self.buildings.append(stable)
		self.garage = garage #3
		self.buildings.append(garage) 
		self.smith = smith #4
		self.buildings.append(smith)
		self.place = place #5
		self.buildings.append(place)
		self.market = market #6
		self.buildings.append(market)
		self.wood_b = wood_b #7
		self.buildings.append(wood_b)
		self.stone_b = stone_b #8
		self.buildings.append(stone_b)
		self.iron_b = iron_b #9
		self.buildings.append(iron_b)
		self.farm = farm #10
		self.buildings.append(farm)
		self.storage = storage #11
		self.buildings.append(storage)
		self.wall = wall #12
		self.buildings.append(wall)
		self.snob = snob #13
		self.buildings.append(snob)
		self.statue = statue #14
		self.buildings.append(statue)

		self.storage_cap = storage_cap
		self.farm_cap = farm_cap
		self.workers = workers
		#bonus id?
		#traders

def add_village(empty_list,upgrading,idd, wood, stone, iron, main, barracks, stable, garage, snob, smith, place, statue, market, wood_b, stone_b, iron_b, farm, storage, wall, storage_cap, farm_cap, workers):
	supp = Village(empty_list,upgrading,idd, wood, stone, iron, main, barracks, stable, garage, snob, smith, place, statue, market, wood_b, stone_b, iron_b, farm, storage, wall, storage_cap, farm_cap, workers)
	villages.append(supp)

#dodges and attacks
attacks = 0
attack_href = list()
time_to_cancel = list()
village_url = list()
time_dodge = list()


wood_list = [[90, 113, 143, 180, 227, 286, 360, 454, 572, 720, 908, 1144, 1441, 1816, 2288, 2883, 3632, 4577, 5767, 7266, 9155, 11535, 14534, 18313, 23075, 29074, 36633, 46158, 58159, 73280], [200, 252, 318, 400, 504, 635, 800, 1008, 1271, 1601, 2017, 2542, 3202, 4035, 5084, 6406, 8072, 10170, 12814, 16146, 20344, 25634, 32298, 40696, 51277], [300, 378, 476, 600, 756, 953, 1200, 1513, 1906, 2401, 3026, 3812, 4804, 6053, 7626], [220, 277, 349, 440, 555, 699, 880, 1109, 1398, 1761, 2219, 2796, 3523, 4439, 5593, 7047, 8879, 11187, 14096, 17761], [10], [100, 126, 159, 200, 252, 318, 400, 504, 635, 800, 1009, 1271, 1601, 2018, 2542, 3203, 4036, 5085, 6407, 8073, 10172, 12817, 16149, 20348, 25639], [50, 63, 78, 98, 122, 153, 191, 238, 298, 373, 466, 582, 728, 909, 1137, 1421, 1776, 2220, 2776, 3469, 4337, 5421, 6776, 8470, 10588, 13235, 16544, 20680, 25849, 32312], [65, 83, 105, 133, 169, 215, 273, 346, 440, 559, 709, 901, 1144, 1453, 1846, 2344, 2977, 3781, 4802, 6098, 7744, 9835, 12491, 15863, 20147, 25586, 32495, 41268, 52410, 66561], [75, 94, 118, 147, 184, 231, 289, 362, 453, 567, 710, 889, 1113, 1393, 1744, 2183, 2734, 3422, 4285, 5365, 6717, 8409, 10528, 13181, 15503, 20662, 25869, 32388, 40549, 50768], [45, 59, 76, 99, 129, 167, 217, 282, 367, 477, 620, 806, 1048, 1363, 1772, 2303, 2994, 3893, 5060, 6579, 8525, 11118, 14453, 18789, 24426, 31754, 41280, 53664, 69763, 90692], [60, 76, 96, 121, 154, 194, 246, 311, 393, 498, 630, 796, 1007, 1274, 1612, 2039, 2580, 3264, 4128, 5222, 6606, 8357, 10572, 13373, 16917, 21400, 27071, 34245, 43320, 54799], [50, 63, 79, 100, 126, 159, 200, 252, 318, 400, 504, 635, 801, 1009, 1271, 1602, 2018, 2543, 3204, 4037], [15000, 30000, 60000], [220]]
stone_list = [[80, 102, 130, 166, 211, 270, 344, 438, 559, 712, 908, 1158, 1476, 1882, 2400, 3060, 3902, 4975, 6343, 8087, 10311, 13146, 16762, 21371, 27248, 34741, 44295, 56476, 72007, 91809], [170, 218, 279, 357, 456, 584, 748, 957, 1225, 1568, 2007, 2569, 3288, 4209, 5388, 6896, 8827, 11298, 14462, 18511, 23695, 30329, 38821, 49691, 63605], [240, 307, 393, 503, 644, 825, 1056, 1351, 1729, 2214, 2833, 3627, 4642, 5942, 7606], [180, 229, 293, 373, 476, 606, 773, 986, 1257, 1603, 2043, 2605, 3322, 4236, 5400, 6885, 8779, 11193, 14271, 18196], [40], [100, 127, 163, 207, 264, 337, 430, 548, 698, 890, 1135, 1447, 1846, 2353, 3000, 3825, 4877, 6218, 7928, 10109, 12889, 16433, 20952, 26714, 34060], [60, 77, 98, 124, 159, 202, 258, 329, 419, 534, 681, 868, 1107, 1412, 1800, 2295, 2926, 3731, 4757, 6065, 7733, 9860, 12571, 16028, 20436, 26056, 33221, 42357, 54005, 68857], [50, 63, 80, 101, 128, 162, 205, 259, 328, 415, 525, 664, 840, 1062, 1343, 1700, 2150, 2720, 3440, 4352, 5505, 6964, 8810, 11144, 14098, 17833, 22559, 28537, 36100, 45666], [65, 83, 106, 135, 172, 219, 279, 352, 454, 579, 738, 941, 1200, 1529, 1950, 2486, 3170, 5153, 6571, 8378, 10681, 13619, 17364, 22139, 28227, 35990, 45887, 58506, 74595], [40, 53, 70, 92, 121, 160, 212, 279, 369, 487, 642, 848, 1119, 1477, 1950, 2574, 3398, 4486, 5921, 7816, 10317, 13618, 17976, 23728, 31321, 41344, 54574, 72037, 95089, 125517], [50, 64, 81, 102, 130, 165, 210, 266, 338, 430, 546, 693, 880, 1180, 1420, 1803, 2290, 2908, 3693, 4691, 5957, 7599, 9608, 12203, 15497, 19682, 24996, 31745, 40316, 51201], [100, 127, 163, 207, 264, 337, 430, 548, 698, 890, 1135, 1447, 1846, 2353, 3000, 3825, 4877, 6218, 7928, 10109], [25000, 50000, 100000], [220]]
iron_list = [[70, 88, 111, 140, 176, 222, 280, 353, 445, 560, 706, 890, 1121, 1412, 1779, 2242, 2825, 3560, 4485, 5651, 7120, 8972, 11304, 14244, 17947, 22613, 38493, 35901, 45235, 56996], [90, 113, 143, 180, 227, 286, 360, 454, 572, 720, 908, 1144, 1441, 1816, 2288, 2883, 3632, 4577, 5767, 7266, 9155, 11535, 14534, 18313, 23075], [260, 328, 413, 520, 655, 826, 1040, 1311, 1652, 2081, 2622, 3304, 4163, 5246, 6609], [240, 302, 381, 480, 605, 762, 960, 1210, 1525, 1921, 2421, 3050, 3843, 4842, 6101, 7687, 9686, 12204, 15377, 19375], [30], [100, 126, 159, 200, 252, 318, 400, 504, 635, 800, 1009, 1271, 1601, 2018, 2542, 3203, 4036, 5085, 6407, 8073, 10172, 12817, 16149, 20348, 25639], [40, 50, 63, 77, 96, 120, 149, 185, 231, 287, 358, 446, 555, 691, 860, 1071, 1333, 1659, 2066, 2572, 3202, 3987, 4963, 6180, 7694, 9578, 11925, 14847, 23013], [40, 50, 62, 76, 95, 117, 145, 180, 224, 277, 344, 426, 529, 655, 813, 1008, 1250, 1550, 1922, 2383, 2955, 3664, 4543, 5633, 6985, 8662, 10740, 13318, 16515, 20478], [70, 87, 108, 133, 165, 205, 254, 316, 391, 485, 602, 746, 925, 1147, 1422, 1764, 2187, 2712, 3363, 4170, 5170, 6411, 7950, 9858, 12224, 15158, 18796, 23307, 28900, 35837], [30, 39, 50, 64, 83, 107, 138, 178, 230, 297, 383, 494, 637, 822, 1060, 1368, 1764, 2276, 2936, 3787, 4886, 6302, 8130, 10488, 13529, 17453, 22514, 29043, 37466, 48331], [40, 50, 62, 77, 96, 120, 149, 185, 231, 287, 358, 446, 555, 691, 860, 1071, 1333, 1659, 2066, 2572, 3202, 3987, 4963, 6180, 7694, 9578, 11925, 14847, 18484, 23013], [20, 25, 32, 40, 50, 64, 80, 101, 127, 160, 202, 254, 320, 404, 508, 641, 807, 1017, 1281, 1615], [10000, 20000, 40000], [220]]
workers_list = [[5, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 7, 8, 9, 10, 12, 15, 17, 19, 23, 27, 31, 37, 43, 51, 59, 69], [7, 1, 2, 1, 2, 2, 3, 3, 4, 4, 5, 5, 7, 8, 9, 11, 12, 15, 17, 20, 24, 27, 32, 38, 44], [8, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 7, 8, 9, 10], [20, 3, 4, 5, 5, 7, 7, 9, 10, 12, 14, 16, 20, 22, 26, 31, 36, 42, 49, 57], [0], [20, 3, 4, 5, 5, 7, 7, 9, 10, 12, 14, 16, 20, 22, 26, 31, 36, 42, 49, 57, 67, 79, 92, 107, 126], [5, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 7, 8, 9, 10, 12, 14, 16, 19, 21, 24, 29, 33, 38, 43], [10, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 8, 8, 10, 12, 13, 15, 16, 20, 22, 25, 28, 33, 37, 42, 48, 55], [10, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 10, 11, 13, 15, 18, 21, 25, 28, 34, 39, 46, 54, 63, 74, 86, 100, 118, 138], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 7, 8, 9, 10, 12, 15], [80, 14, 16], [10]]
villages = list()
build_preset = list()

def get_settings():
	for x in villages:
		build_preset.append('eko')
