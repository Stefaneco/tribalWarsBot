import config


def check(building,village):
	free_space=village.farm_cap-village.workers
	if config.workers_list[building][village.buildings[building]]>free_space:
		return (10, village.idd)
	elif village.storage_cap<config.wood_list[building][village.buildings[building]] or village.storage_cap<config.stone_list[building][village.buildings[building]] or village.storage_cap<config.iron_list[building][village.buildings[building]]:
		return (11, village.idd)
	elif config.wood_list[building][village.buildings[building]]>village.wood or config.stone_list[building][village.buildings[building]]>village.stone or config.iron_list[building][village.buildings[building]]>village.iron:
		return (100)
	else:
		return(building, village.idd)


def main():
	config.build_preset = list()
	config.get_settings()
	orders=list()
	number=0
	for village in config.build_preset:
		if config.villages[number].upgrading==False:
			if village=='eko':
				orders.append(eco(number))
		else:
			orders.append(100)
		number+=1
	return orders
'''
def eko(index):
	village=config.villages[index]
	x=village.wood_b-village.stone_b
	if village.wood_b == village.stone_b and village.wood_b - village.main>15:
		return check(0,village)
	elif x==0:
		if village.wood>village.stone and village.stone_b<30:
			return check(8,village)
		elif village.wood_b<30:
		 	return check(7,village)
	elif x<0 and village.wood_b<30:
		return check(7,village)
	elif x>0 and village.stone_b<30:
		return check(8,village)
	elif village.wood_b == village.stone_b and village.wood_b-village.iron_b>2 and village.iron_b<30:
		return check(9,village)
	elif village.wood_b == village.stone_b and village.stone_b == 30 and village.iron_b<30:
		print('rrr')
		return check(9,village)
	elif village.barracks<10:
		return check(1,village)
	elif village.farm<20:
		return check(10,village)
	elif village.smith<10:
		return check(4,village)
	elif village.stable<10:
		return check(2,village)
	elif village.garage<5:
		return check(3,village)
	elif village.barracks<25:
		return check(1,village)
	elif village.storage<20:
		return check(11,village)
	elif village.farm<30:
		return check(10,village)
	elif village.storage<30:
		return check(11,village)
	elif village.stable<15:
		return check(2,village)
	elif village.main<20:
		return check(0,village)
	elif village.smith<20:
		return check(4,village)
	elif village.market<10:
		return check(6,village)
	elif village.snob<1:
		return check(13,village)
	elif village.wall<20:
		return check(12,village)
	print('...')
	return 100
'''	

def eco(index):
	village=config.villages[index]
	x=village.wood_b-village.stone_b
	if x==0 and village.wood_b - village.main>15:
		return check(0, village)
	elif x==0 and village.wood_b - village.iron_b>4:
		return check(9,village)
	elif x>0 and village.stone_b<30:
		return check(8, village)
	elif x<0 and village.wood_b<30:
		return check(7,village)
	elif village.iron_b<30:
		return check(9,village)
	elif village.barracks<10:
		return check(1,village)
	elif village.farm<20:
		return check(10,village)
	elif village.smith<10:
		return check(4,village)
	elif village.stable<10:
		return check(2,village)
	elif village.garage<5:
		return check(3,village)
	elif village.barracks<25:
		return check(1,village)
	elif village.storage<20:
		return check(11,village)
	elif village.farm<30:
		return check(10,village)
	elif village.storage<30:
		return check(11,village)
	elif village.stable<15:
		return check(2,village)
	elif village.main<20:
		return check(0,village)
	elif village.smith<20:
		return check(4,village)
	elif village.market<10:
		return check(6,village)
	elif village.snob<1:
		return check(13,village)
	elif village.wall<20:
		return check(12,village)
	return 100
