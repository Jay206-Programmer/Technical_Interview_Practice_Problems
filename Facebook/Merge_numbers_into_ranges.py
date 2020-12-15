
#* Asked by Facebook

#? Given a list of sorted numbers, build a list of strings displaying numbers,
#? Where each string is first and last number of linearly increasing numbers.

#! Example:

#? Input: [0,1,2,2,5,7,8,9,9,10,11,15]
#? Output: ['0 -> 2','5 -> 5','7 -> 11','15 -> 15']

#! Note that numbers will not be lower than 0, also numbers may repeat

def truncateList(lst):
  
  if len(lst) == 0: return list()
  
  num = lst[0]
  next_num = num+1
  start_num = num
  final_lst = list()
  i = 1
  
  while i < len(lst):
    if lst[i] == num or lst[i] == next_num:
      pass
    else:
      final_lst.append(f"{start_num} -> {num}") 
      start_num = lst[i]
      
    num = lst[i]
    next_num = num + 1
    i+=1
  else:
    final_lst.append(f"{start_num} -> {num}") 
      
  return final_lst

print(truncateList([0,1,2,2,5,7,8,9,9,10,11,15]))
# ['0 -> 2', '5 -> 5', '7 -> 11', '15 -> 15']