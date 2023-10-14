def number_to_string(num):
    # Return a string of the number here!
       return str(num)
 
def get_sum(a,b):
     return sum(list(range(a, b+1))) if a < b else sum(list(range(b, a+1)))
   
def maps(a):
  result= [];
  for num in a:
    result.append(2 * num);
  return result;
 
  def make_upper_case(s):
    # Code here
    return s.upper()

def remove_smallest(numbers):
    arr = numbers[:]
    return numbers and arr.pop(arr.index(min(arr))) and arr

def xo(s):
    return ( True if s.lower().count('x') == s.lower().count('o') else False )
