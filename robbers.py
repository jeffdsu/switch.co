#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getHitList (valuables) : 
	"""Returns the list of hits that should be taken"""
	hitlist = []
	maxHitCount = len(a) / 2 if len(a) % 2 == 0 else (len(a)+1)/2
	hitworthPerHouse = [0] * len(valuables)

	for i in xrange ( 0, len(valuables) ) :
		if valuables[i] != 'x' :
			hitworthPerHouse [i] = valuables[i]
			hitworthPerHouse [i] = hitworthPerHouse [i] - valuables[i+1] if i < (len(valuables) - 1)  else hitworthPerHouse [i]
			hitworthPerHouse [i] = hitworthPerHouse [i] - valuables[i-1] if i > 0 else hitworthPerHouse [i]

		
	for i in xrange (0, maxHitCount) :
		print hitworthPerHouse
		hit = searchForBestHit(hitworthPerHouse)
		hitlist.append (hit)
		hitHouseUpdateHitWorth(hitworthPerHouse, valuables, hit)

	return hitlist
def comparewithX (a) :
	if a == 'x' : 
		print a
		return 
def searchForBestHit (hitworthPerHouse) :
	"""Gets index of best hit"""
	#return hitworthPerHouse.index(max(hitworthPerHouse, cmp=comparewithX))
	maxindex = -1
	foundint = False
	for i in xrange ( 0, len(hitworthPerHouse) ) :
		if hitworthPerHouse[i] != 'x':
			if foundint == False:
				maxvalue = hitworthPerHouse [i]
				maxindex = i
				foundint = True
			elif foundint == True and  maxvalue < hitworthPerHouse [i] :
				maxvalue = hitworthPerHouse [i]
				maxindex = i
	return maxindex


def hitHouseUpdateHitWorth (hitworthPerHouse, valuables, houseIndex) :
	"""Updates the hit worth after cops come"""
	if houseIndex < 0 or houseIndex >= len(valuables) : 
		return 
	hitworthPerHouse [houseIndex] = 'x'
	if (houseIndex + 1) < len(valuables) :
		hitworthPerHouse [houseIndex+1] = 'x'
	if (houseIndex - 1) >= 0 :
		hitworthPerHouse [houseIndex-1] = 'x'
	if (houseIndex+2) < len(valuables) and hitworthPerHouse [houseIndex+2] != 'x':
		hitworthPerHouse [houseIndex+2] = hitworthPerHouse [houseIndex+2] + valuables [houseIndex+1]
	if (houseIndex-2) >=0 and hitworthPerHouse [houseIndex-2] != 'x':
		hitworthPerHouse [houseIndex-2] = hitworthPerHouse [houseIndex-2] + valuables [houseIndex-1]

def getBestHitTotal (valuables) :
	"""Returns the sum up the hit total value"""
	hitlist = getHitList(valuables)
	print hitlist
	totalHitWorth = 0
	for h in hitlist :
		if h >= 0 :
			totalHitWorth = totalHitWorth + a[h]
	return totalHitWorth
 
totalHitWorth = 0
a = [20, 10, 50, 5, 1]
#a = [20, 50, 10, 1, 5]
#a = [30, 50, 20, 1]
#a = [30, 50, 20, 1, 2]
#a = [30, 50, 50, 1, 2]
#a = [30, 50, 50, 1, 2, 50, 50, 50]
#a = [20, 50, 20, 20, 50, 20]

print "Best Hit : " + str(getBestHitTotal(a))


