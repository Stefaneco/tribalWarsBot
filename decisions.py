import config

#Monkas coding

def check(building,village):
	free_space=village.farm_cap-village.workers
	if config.workers_list[building][village.buildings[building]+1]>free_space:
		return (10)
	elif config.village.storage_cap<config.wood_list[building][village.buildings[building]+1] or config.village.storage_cap<config.stone_list[building][village.buildings[building]+1] or config.village.storage_cap<config.iron_list[building][village.buildings[building]+1]:
		return (11)
	elif config.wood_list[building][village.buildings[building]+1]>village.wood or config.stone_list[building][village.buildings[building]+1]>village.stone or config.iron_list[building][village.buildings[building]+1]>village.iron:
		return (1000)
	else return(building)

orders=list()
def main():
	number=0
	for village in config.build_preset:
		if village==eko:
			orders.append(eko(number))
		number+=1
def eco(index):
	village=config.villages[index]
	x=village.wood_b-village.stone_b
	if wood_b == stone_b and wood_b - main>15:
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
	elif village.wood_b == village.stone_b == 30 and village.iron_b<30:
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
		return check(12):
	
