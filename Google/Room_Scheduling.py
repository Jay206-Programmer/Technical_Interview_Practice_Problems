
#* Asked in Google

#? You are give a tuple representing the time of tuples representing the time intervals
#? for the lectures, intervals may be overlapped.

#? Return the number of rooms required.

#! Example

#? Input: [(30,75),(0,50),(60,150)]
#? Output: 2 
#!Two rooms will be required

def findRooms(lst):
  lst.sort()
  
  rooms = 0
  i = 0
  
  while i < len(lst)-1:
    j=i+1
    flag= True
    while j < len(lst):
      if lst[i][1] >= lst[j][0]:
        flag= False
        break
      j+=1
    if not flag:
      rooms += 1
    i+=1
  return rooms

print(findRooms([(30,75),(0,50),(60,150)]))