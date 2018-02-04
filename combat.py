from classes import *

#TODO: Class or function? Functions can end but classes have more attributes.
#	Add custom weapon choice during fight.
class fight():
	def __init__(self, agg, deaf):
		self.agg = agg
		self.deaf = deaf
	
	#def fightChoice(self):
        #	print "What do you want to do?"
        #	if raw_input("attack " + name.)
			#player.playerAttack(sword, wolf)
	def turn(self):
		flag = True
		while flag:

			if self.agg.__class__ == mob:
				self.agg.attack(self.deaf)
				print self.agg.race + " attacked you"
				print "Your hp is now " + str(self.deaf.hp)

			elif self.agg.__class__ == player:
				self.agg.playerAttack(sword, self.deaf)
                		print self.deaf.race + " hp is " + str(self.deaf.hp)

			if self.deaf.hp == 0:
				print self.deaf.race + " is dead"
				break

			if self.deaf.__class__ == mob:
				self.deaf.attack(self.agg)
                                print self.deaf.race + " attacked you"
                                print "Your hp is now " + str(self.agg.hp)

                        elif self.deaf.__class__ == player:
                                self.deaf.playerAttack(sword, self.agg)

               			print self.agg.race + " hp is " + str(self.agg.hp)

			if self.agg.hp == 0 :
				print self.agg.race + " is dead"
				break
	


			
	
#TODO: Add raw input for user
#def choice():
#	print "What do you want to do?"
#	if raw_input("attack" + )
		
player1 = player()
sword = weapon('Sword', 5, degredation = 50)
player1.pickup(sword)

wolf = mob('Wolf', 40 , 5)

#wolf.attack(player1)
#print player.hp
fight = fight(player1, wolf)

fight.turn()


