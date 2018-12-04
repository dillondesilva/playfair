from __future__ import division
frequencies = {}

# Calculating the mean
def calcMean ():
  fx = 0
  sum_of_f = 0
  for entry in frequencies:
    fx += entry * frequencies[entry]
    sum_of_f += frequencies[entry]  
  
  mean = fx / sum_of_f
  return mean

# Calculating the median
def calcMedian ():
  list_of_vals = []
  for entry in frequencies:
    for item in entry:
      list_of_vals.append(entry)
    
  n = len(list_of_vals)
  if n < 1:
    return None
  if n % 2 == 1:
    return sorted(list_of_vals)[n//2]
  else:
    return sum(sorted(list_of_vals)[n//2-1:n//2+1])/2.0

# Calculating Mode
def calcMode ():
  mode = []
  current_modal_level = None
  for entry in frequencies:
    if frequencies[entry] > 1 and frequencies[entry] > current_modal_level:
      mode = [entry]
      current_modal_level = entry
    elif frequencies[entry] > 1 and frequencies[entry] == current_modal_level:
      mode.append(entry)
      current_modal_level = entry

  return mode

# Highest score minus lowest score
def calcRange ():
  max = 0
  min = None
  for entry in frequencies:
    if entry > max:
      max = entry
    if min == None:
      min = entry
    elif entry < min:
      min = entry

  range = max - min
  return range

def calcUppQuartile (dataset):
  # This is a stub
  return ''

def calcLowQuartile (dataset):
  return ''
  # This is a stub

def calcInterQuartile (dataset):
  # This is a stub
  return ''

raw_data = raw_input("New numerical entry: ")

while raw_data:
  if raw_data != '':
    raw_data = int(raw_data)
    if raw_data in frequencies:
      frequencies[raw_data] += 1
    else:
      frequencies[raw_data] = 1

  raw_data = raw_input("New numerical entry: ")

print('Mean:', calcMean())
print('Median:', calcRange())
print('Mode:', calcMode())
print('Range:', calcRange())
