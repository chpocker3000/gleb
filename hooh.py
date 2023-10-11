def century(year):
    # Finish this :)
    if year % 100 == 0:
        return (year // 100)
    else:
        return (year // 100) +1

  def friend(x):
    #Code
    return [x for x in x if len(x) == 4]

  
def past(h, m, s):
    return (h*3600000 + m*60000 + s*1000)
