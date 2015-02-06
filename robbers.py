#!/usr/bin/env python
# -*- coding: utf-8 -*-



def findOptimalRobbingHitandHitIt (valuables) :
	"""Returns the most optimal hit for robbers to take,  returns 0 when no more work can be done."""


	#-- first find how much each hit is worth.  this includes the money lost from the neigboaring houses
	maxvalue = -1
	maxindex = 0
	hitworthPerHouse = [0] * len(valuables)
	for i in xrange ( 0, len(valuables) ) :
		if valuables[i] != 'x' :
			hitworthPerHouse [i] = valuables[i]
			hitworthPerHouse [i] = hitworthPerHouse [i] - valuables[i+1] if i < (len(valuables) - 1) and valuables[i+1] != 'x' else hitworthPerHouse[i]
			hitworthPerHouse [i] = hitworthPerHouse [i] - valuables[i-1] if i > 0 and valuables[i-1] !='x' else hitworthPerHouse[i]


			#-- keep track of the maxvalue so I can hit the house afterwards
			if i == 0 :
				maxvalue = hitworthPerHouse [i]
			elif maxvalue < hitworthPerHouse [i] :
				maxvalue = hitworthPerHouse [i]
				maxindex = i


	if maxindex >= 0:
		#hit the house
		hitValue = hitHouseAndSendTheCops (valuables, maxindex)
		if hitValue > 0 :
			return hitValue
	return 0
	


def hitHouseAndSendTheCops (valuables, houseIndex) :
	"""Returns value of hit while sending the cops to clear the neighboring houeses"""
	t = valuables [houseIndex]
	valuables [houseIndex] = 'x'
	if houseIndex > 0 :
		valuables [houseIndex - 1] = 'x'
	if houseIndex < (len(valuables) - 1) :
		 valuables [houseIndex + 1] = 'x'
	return t
#def findBestValueDumbWay (valuables) :
#	for i in xrange ( 0, len(valuables) ) :



totalHitWorth = 0
a = [20, 10, 50, 5, 1]
a = [20, 50, 10, 1, 5]
a = [30, 50, 20, 1]
a = [30, 50, 20, 1, 2]
a = [30, 50, 50, 1, 2]
a = [30, 50, 50, 1, 2, 50, 50, 50]
#no matter what, the max amount houses that can be hit is len / 2
for i in xrange(0, len(a) / 2 if len(a) % 2 == 0 else (len(a)+1)/2 ) :
	totalHitWorth = totalHitWorth + findOptimalRobbingHitandHitIt(a)

print "Best Hit : " + str(totalHitWorth)


