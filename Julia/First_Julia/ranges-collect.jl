
collect(1:5)

collect(1.5:5.5)

#if we want to have diferent step put another colon 
collect(1.5:.5:5.5)

collect(0:10:100)

#reverse array 
collect(100:-20:0)

#store 
c1 = collect(100:-20:0)
c1

#pickup one element from arrey
#access elemet in arrey
c1[3]
c1[end]
c1[end-1]

#access a range from arrey
c1[2:5]
c1[[2,3,4,5]]
c1[2:end]
