#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#hello_name('Bob') → 'Hello Bob!'
#hello_name('Alice') → 'Hello Alice!'
#hello_name('X') → 'Hello X!'

def hello_name(name):
  return 'Hello ' + name + '!'

#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
#make_abba('Hi', 'Bye') → 'HiByeByeHi'
#make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
#make_abba('What', 'Up') → 'WhatUpUpWhat'

def make_abba(a, b):
  return a + (b * 2) + a

#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" 
#tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with 
#tags around the word, e.g. "<i>Yay</i>".
#make_tags('i', 'Yay') → '<i>Yay</i>'
#make_tags('i', 'Hello') → '<i>Hello</i>'
#make_tags('cite', 'Yay') → '<cite>Yay</cite>'

def make_tags(tag, word):
  return '<{0}>{1}</{0}>'.format(tag, word)

#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle 
#of the out string, e.g. "<<word>>".
#make_out_word('<<>>', 'Yay') → '<<Yay>>'
#make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
#make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(out, word):
  return out[:2] + word + out[-2:] 

#Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

def extra_end(str):
  return str[-2:] * 3

#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
  end = len(str) / 2
  return str[:end]

#Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

def without_end(str):
  if len(str) >= 2:
    return str[1:-1]
  else:
    return str

#Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer 
#string on the inside. The strings will not be the same length, but they may be empty (length 0).

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  else:
    return a + b + a

#Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

def non_start(a, b):
  return a[1:] + b[1:]

#Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

def left2(str):
  return str[2:] + str[:2]

#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

def make_pi():
  return [3, 1, 4]

#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. 
#Both arrays will be length 1 or more.

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

def rotate_left3(nums):
  lista = nums[1:]
  lista.append(nums[0])
  return lista

#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

def reverse3(nums):
  return nums[::-1]

#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set 
#all the other elements to be that value. Return the changed array.

def max_end3(nums):
  maxl = max(nums[0], nums[-1])
  lista = []
  lista.append(maxl)
  lista.append(maxl)
  lista.append(maxl)
  return lista

#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, 
#just sum up the elements that exist, returning 0 if the array is length 0.

def sum2(nums):
  if len(nums) >=2:
    return sum(nums[:2])
  elif len(nums) >0:
    return sum(nums)
  else:
    return 0
  
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

def middle_way(a, b):
  return [a[1], b[1]]

#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. 
#The original array will be length 1 or more.

def make_ends(nums):
  return [nums[0], nums[-1]]

#Given an int array length 2, return True if it contains a 2 or a 3.

def has23(nums):
  return 2 in nums or 3 in nums

#When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of 
#cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number 
#of cigars. Return True if the party with the given values is successful, or False otherwise.

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return (cigars >= 40)
  else:
    return (cigars >= 40 and cigars <= 60)

#You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, 
#in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as 
#an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). 
#With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

def date_fashion(you, date):
  if you <=2 or date <= 2:
    return 0
  elif you >= 8 or date >=8:
    return 2
  else:
    return 1

#The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature 
#is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an 
#int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
  if is_summer == False:
    return temp >= 60 and temp <= 90
  else:
    return temp >= 60 and temp <= 100

#You are driving a little too fast, and a police officer stops you. Write code to compute the result, 
#encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. 
#If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is 
#your birthday -- on that day, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    bonus = 5
  else:
    bonus = 0
  
  if speed >= 81 + bonus:
    return 2
  elif speed >= 61 + bonus:
    return 1
  else:
    return 0

#Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

def sorta_sum(a, b):
  sum = a + b
  if sum >= 10 and sum <= 19:
    return 20
  return sum

#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
#return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" 
#and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends 
#it should be "off".

def alarm_clock(day, vacation):
  if vacation == 1:
    sleep = 3
  else:
    sleep = 0
  
  if day >= 1 and day <= 5:
    return str(7 + sleep) + ':00'
  else:
    if vacation == 0:
      return '10:00'
    return 'off'

#The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. 
#Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

def love6(a, b):
  return a + b == 6 or abs(a - b) == 6 or a ==6 or b == 6 

#Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, 
#in which case return True if the number is less or equal to 1, or greater or equal to 10.

def in1to10(n, outside_mode):
  if outside_mode == False:
    return n >= 1 and n <= 10
  return n <= 1 or n >= 10

#Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the 
#remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

def near_ten(num):
  return num % 10 >= 8 or num % 10 <= 2








