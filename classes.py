##############################################################################################
#The base classes are being stored here. It's all a bit messy at the moment, early stages.
#
#

#Class:		Object
#Attributes:	name
#Kwargs:	degredation, by default = 100
class obj:
	def __init__(self, name, **kwargs):
		self.name = name
		if kwargs.get('degredation'):

			self.deg = kwargs.get('degredation')

		else:

			self.deg = 100


#Clases:	Weapon
#Attributes:	obj +
#		atk,	 attack value
#TODO:		Add probability of attack hitting however this may also be based on the play skill and mob skill.
#TODO:		Add attack class so one weapon can have many attacks, e.g. sword -> stab or slash

class weapon(obj):
	def __init__(self, name,  atk, **kwargs):
		obj.__init__(self, name, **kwargs)
		self.atk = atk
	
	def attack(self, mob):
		print "Attacking " + mob.race + " with " + self.name
		mob.hp -= self.atk
		self.deg -= 2
		print mob.race + " hp is " + str(mob.hp)



#class attack:
#	def __init__(self, name ,damage, prob):
#		self.name  = name
#		self.damamge = damamge
#		self.prob = prob

#Class:		Inventory
#Attributes:	size , how many inventory slots.
#

class inventory:
	def __init__(self, size):
		self.size = size
		self.inv = {}
		for i in range(size):
			self.inv[i] = []

	def add(self, item):
		flag = False
		for i in range(self.size):
			if self.inv[i] == [] and flag == False:
				self.inv[i].append(item)
				flag = True
			else:
				pass

	def check(self):
		for i in range(self.size):
			if self.inv[i] == []:
				print "Empty slot"
			else:
				print str(i) + self.inv[i][0].name	



#Class		entity, player/creature base class
#Attributes	race
#		hp (hitpoints)
class entity:
	def __init__(self, race, hp):
		self.race = race
		self.hp = hp



class mob(entity):
	def __init__(self, race, hp, atk):
		entity.__init__(self, race, hp)
		self.atk = atk
		#self.deaf = deaf

class player(entity):
	
	def __init__(self):
		entity.__init__(self, 'Human', 100)

		self.inventory = inventory(10)
	
	def pickup(self, item):
		self.inventory.add(item)
	
	def playerAttack(self, weapon, mob):
		weapon.attack(mob)


#Little demo of a player picking up and attacking a wolf with a sword.

player = player()
sword = weapon('Sword', 5, degredation = 50)
player.pickup(sword)
player.inventory.check()
wolf = mob('Wolf', 40, 5)

player.playerAttack(sword, wolf)

#sword.attack(wolf)
#print wolf.hp
##print sword.deg	
