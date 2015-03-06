#!/usr/bin/python
from random import randint

# kemi x sherbime ku secili ka nje peshe te caktuar ne sistem 
# dhe duhen shprendare midis N nyjeve
# menyra me e hajrit qe me vajti ne mendje eshte kjo qe kam shpjeguar me poshte

#1 -  mblidhet shuma e peshave te sherbimeve
#2 -  pjestohet per nr e nyjeve
#3 -  radhiten sherbimet sipas peshes
#4 -  nis shprendarja nepermjet nyjeve


# nr i nyjeve N

#index	 weight 	type

#0	 1			ping
#1	 2			pop_check
#2	 2			smtp_check
#3	 2			blacklist
#4	 3			http_status
#5	 3			http_content
#6	 3			http_title
#7	 10			http_load


# marrim sherbimet ( kto i kam gjeneruar random)

# (0, 3)
# (1, 2)
# (2, 3)
# (3, 10)
# (4, 10)
# (5, 3)
# (6, 2)
# (7, 2)

# i rendisim

# (1, 2)
# (6, 2)
# (7, 2)
# (0, 3)
# (2, 3)
# (5, 3)
# (3, 10)
# (4, 10)

# llogarisim shprendarjen per N=3 nyje

# totali 6 + 9 + 20 = 35
# 35 / 3 = 11.6 =~ 12

# nyja e fundit ose do kete pak me shume/pak


#target: (varianti 1)
# 13		 	13				9
# --------------------------------

# duke nisur qe nga fundit heqim te medhajat
# dhe shprendajme

# 10			10				3
# 3 			 3 				3
# -				 -				2
# - 			 -				2
# --------------------------------
# 13			13				9
# DONE

#target: (varianti 2)
# 12		 	12				11
# --------------------------------

# 10			10				3
# 3 			 3 				3
# -				 -				2
# - 			 -				2
# --------------------------------
# 13			13				9
# DONE


services = []
s_sorted = []

total_weight = 0

N = 2


# gjenerojme ca sherbime random

for i in range(0,30):
	tmp = randint(1,9)
	#print "Got random nr: ",tmp
	if tmp == 1:
		#print i," ",1
		services.append([i,1])
		total_weight += 1 
	if tmp > 1 and tmp <= 5:
		#print i," ",2
		services.append([i,2])
		total_weight += 2 
	if tmp > 5 and tmp <= 7:
		#print i," ",3
		services.append([i,3])
		total_weight += 3 
	if tmp > 7:
		#print i," ",10
		services.append([i,10])
		total_weight += 10 

for k, v in sorted(services, key=lambda(k, v): v): 
	#print(k, v)
	s_sorted.append([k, v])


print "Total weight of the nodes: ",total_weight
print "Total number of services: ",len(services)
print "Total number of nodes: ",N

ratio = total_weight / N
print "Ratio: ",ratio
#print "Rounded ratio",int(ratio)

nodes = []
node_weight = []

for nr in range(0,N):
	nodes.append([])
	node_weight.append(0)
	
node_index = 0


print "(over) Populating the nodes "
while total_weight != 0:
	for el in reversed(s_sorted):
		if node_index > (N-1):
			node_index = 0
		if node_weight[node_index] > ratio-1:	# its a tweak, dont ask why I need this
			for ix in range(0,N):
				if node_weight[ix] < ratio:
					node_index = ix
					break
		nodes[node_index].append(el[1])
		node_weight[node_index] += el[1]
		#print "Current weight for node with index:",node_index," ",node_weight[node_index]
		total_weight -= el[1]
		node_index += 1
		#print "Service Index ",el[0]," Service weight: ",el[1]

#print nodes

tmp = 0
for nn in nodes:
	for elem in nn:
		tmp += elem
	print tmp
	tmp = 0