
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.


cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True

def cigar_party(cigars, is_weekend):
  if cigars >= 40 and is_weekend :
    return True
  if (cigars >= 40 and cigars <= 60 and not is_weekend):
    return True
  else:
    return False
   
  

You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).


date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1


def date_fashion(you, date):
  if (you <=2 or date<=2):
    return 0
  elif (you >=8 or date>=8 ):
    return 2
  else:
    return 1


The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.


squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
  if is_summer:
    if( temp>=60 and temp <=100 ):
      return True
    if( temp<60 ):
      return False
    if( temp>100 ):
      return False
  if not is_summer:
    if( temp>=60 and temp <=90 ):
      return True
    else:
      return False



You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.


caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed >65 and speed <= 85:
      #ticket
      return 1
    if speed > 85:
      return 2
    if speed <=65:
      return 0
    
  if not is_birthday:
    if speed >61 and speed <= 80:
      #ticket
      return 1
    if speed > 81:
      return 2
    if speed <=60:
      return 0
    
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.


sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21


def sorta_sum(a, b):
  sum = a+b
  if ( sum>=10 and sum <=19):
    return 20
  else:
    return sum


prev  |  next  |  chance
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".


alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'

def alarm_clock(day, vacation):
  if vacation:
    for day in range(1,5):
      return ("10:00")
  if(day==6 or day ==0):
    return("off")
  if not vacation:
    for day in range(1,5):
      return ("7:00")
  if(day==6 or day==0):
    return("10:00")

    
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.


love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True


def love6(a, b):
  sum = a+b
  diff = abs(a-b)
  
  if (sum == 6):
    return True
    
  if (diff == 6):
    return True

  if ( a==6 or b == 6):
    return True
  else:
    return False
    


Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.


in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True


def in1to10(n, outside_mode):
  if outside_mode:
    if( n <=1 or n >=10):
      return True
      
  if not outside_mode:
    if(n >=1 or n<=10):
      return True
    if( n <=1 or n >=10):
      return False

Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod


near_ten(12) → True
near_ten(17) → False
near_ten(19) → True


def near_ten(num):
    a = num % 10
    if  (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False



Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False

def first_last6(nums):
  last= nums[-1]
  first = nums[0]
  if (first ==6 or last == 6):
    return True
  else:
    return False

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.


same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True


def same_first_last(nums):
  length = len(nums)
  first_dig= nums[0]
  sec_dig = nums[-1]
  if ((first_dig == sec_dig) and length >1):
    return True
  else:
    return False
      


Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.


make_pi() → [3, 1, 4]


def make_pi():
  a=3
  b=1
  c=4
  return [a,b,c]

Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.


common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

def common_end(a, b):
  return (a[0]==b[0] or a[-1] == b[-1])

