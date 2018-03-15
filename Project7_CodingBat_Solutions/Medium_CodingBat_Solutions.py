#We want to make a row of bricks that is goal inches long. We have a number of small bricks 
#(1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal 
#by choosing from the given bricks. This is a little harder than it looks and can be done without 
#any loops. See also: Introduction to MakeBricks

def make_bricks(small, big, goal):
  if big == 0:
    return small >= goal
  if goal % 5 == 0 and goal/5 <= big:
    return True
    
  if goal // 5 <= big:
    return (goal % 5) <= small
  else:
    return (goal // 5 - big) * 5 + goal % 5 <= small
  return False
  
#  for i in range(big + 1):
#    for j in range(small + 1):
#      if i*5 + j*1 == goal:
#        return True
#  return False

#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another 
#of the values, it does not count towards the sum.

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c

#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not 
#count towards the sum and values to its right do not count. So for example, if b is 13, then both 
#b and c do not count.

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  return a + b + c

#Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 
#13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a 
#separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen 
#rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper 
#below and at the same indent level as the main no_teen_sum().

def no_teen_sum(a, b, c):
  def fix_teen(n):
    if n in (13, 14, 17, 18, 19):
      return 0
    return n
  
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

#For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 
#or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost 
#digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. 
#To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper 
#entirely below and at the same indent level as round_sum().

def round_sum(a, b, c):
  def round10(num):
    ldigit = num % 10
    if num < 5:
      return 0
    elif num >= 5 and num < 10:
      return 10
    elif ldigit < 5:
      return int(num/10) * 10
    elif num >= 5:
      return int(num/10) * 10 + 10
  return round10(a) + round10(b) + round10(c)
    
#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the 
#other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

def close_far(a, b, c):
  def close(num, num1):
    return abs(num1 - num) <= 1
  def far(num, num1, num2):
    return abs(num - num1) >= 2 and abs(num - num2) >= 2
  if close(a, b) == True:
    return far(c, a, b)
  elif close(a, c) == True:
    return far(b, a, c)
  return False
    
#We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
#Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  if big == 0:
    if small >= goal:
      return goal/small
  if goal % 5 == 0 and goal/5 <= big:
    return 0
    
  if goal // 5 <= big:
    if (goal % 5) <= small:
      return goal % 5
  else:
    if (goal // 5 - big) * 5 + goal % 5 <= small:
      return (goal // 5 - big) * 5 + goal % 5
  return -1

#Given a string, return a string where for every char in the original, there are two chars.

def double_char(str):
  string = ''
  for char in str:
    string += char * 2
  return string

#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  count = 0
  for i in range(len(str) - 1):
    if str[i:i+2] == 'hi':
      count += 1
  return count

#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
  cat = 0
  dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'cat': cat += 1
    if str[i:i+3] == 'dog': dog += 1
  return cat == dog

#Return the number of times that the string "code" appears anywhere in the given string, 
#except we'll accept any letter for the 'd', so "cope" and "cooe" count.

def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count

#Given two strings, return True if either of the strings appears at the very end of the other 
#string, ignoring upper/lower case differences (in other words, the computation should not be 
#"case sensitive"). Note: s.lower() returns the lowercase version of a string.

def end_other(a, b):
  lena = len(a)
  lenb = len(b)
  
  return b.lower() in a[-lenb:].lower() or a.lower() in b[-lena:].lower()

#Return True if the given string contains an appearance of "xyz" where the xyz is not directly 
#preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
  
  for i in range(len(str)-2):
    if str[i:i+3] == 'xyz' and not str[i-1] == '.':
      return True
  return False

#Return the number of even ints in the given array. Note: the % "mod" operator computes the 
#remainder, e.g. 5 % 2 is 1.

def count_evens(nums):
  count = 0
  for element in nums:
    if element % 2 == 0:
      count += 1
  return count

#Given an array length 1 or more of ints, return the difference between the largest and 
#smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions 
#return the smaller or larger of two values.

def big_diff(nums):
  max_number = max(nums)
  min_number = min(nums)
  return max_number - min_number

#Return the "centered" average of an array of ints, which we'll say is the mean average of 
#the values, except ignoring the largest and smallest values in the array. If there are multiple 
#copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int 
#division to produce the final average. You may assume that the array is length 3 or more.

def centered_average(nums):
  newlist = sorted(nums)[1:-1]
  sum = 0
  for i in newlist:
    sum += i
  return sum / len(newlist)

#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 
#13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
  for i in nums:
	  if i == 13:
		  try:
			  del nums[nums.index(i)+1]
			  del nums[nums.index(i)]
		  except:
			  del nums[nums.index(i)]
  if len(nums) == 0 or nums == [13]:
    return 0
  else:
    return sum(nums)
  
#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
#extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
    x = 0
    while x < len(nums):
        if nums[x] == 6:
            y = x + 1
            while y < len(nums):
                if nums[y] == 7:
                    del nums[x : y+1]
                    x = 0
                    break
                y += 1
        x += 1
    return sum(nums)

#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

def has22(nums):
  if len(nums) == 1:
    return False
  for i in range(len(nums)+1):
    try:
      if nums[i] == 2:
        if i>0:
          if nums[i-1] == 2 or nums[i+1] == 2:
            return True
    except:
      pass
  return False


  


