def solution(n):
  count = 0
  collector = []
  binary_number = format(n, 'b')

  for i in str(binary_number):
    if(i == "0"):
       count += 1
    elif(i != "0" and count != 0):
      collector.append(count)
      count = 0

  if(len(collector)):
    print(max(collector))
  else:
    print(0)
  
  solution(20)
