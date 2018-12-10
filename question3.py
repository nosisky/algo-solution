def solution(s):
  sets = dict(zip('({[', ')}]'))
  collector = []
  for bracket in s:
    if(bracket in sets):
      collector.append(sets[bracket])
    elif bracket not in(sets.values()):
      return "Invalid input"
    elif (bracket != collector.pop()):
      return False
  print(collector)
  return not collector


print(solution("()[]{}"))
