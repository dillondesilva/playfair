# Playfair

## Concept

Users can enter a numerical data set and the program returns the mean, median, range, mode, upper quartile, lower quartile and interquartile

## NOTE: MINOR ERROR WITH STANDARD DEVIATION. FIXES OCCURING SOON
## How to use (for Laymen)

- Copy the following source code
```python
import math

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

# Calculating the quartile medians
def calcQMedian (vals):
  n = len( vals)
  if n < 1:
    return None
  if n % 2 == 1:
    return sorted(vals)[n//2]
  else:
    return sum(sorted(vals)[n//2-1:n//2+1])/2.0

# Calculating Mode
def calcMode ():
  mode = []
  current_modal_level = None
  for entry in frequencies:
    if frequencies[entry] > 1 and frequencies[entry] > current_modal_level:
      mode = [entry]
      current_modal_leve4l = entry
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

# Calculating Upper Quartile
def calcUppQuartile ():
  list_of_vals = []
  for entry in frequencies:
    for num in range(0, frequencies[entry]):
      list_of_vals.append(entry)

  mid_idx = int(math.ceil(len(list_of_vals) / 2))
  return(sorted(list_of_vals[mid_idx:]))

# Calculating Lower Quartile
def calcLowQuartile ():
  list_of_vals = []
  for entry in frequencies:
    for num in range(0, frequencies[entry]):
      list_of_vals.append(entry)
  mid_idx = int(math.ceil(len(list_of_vals) / 2))
  return(sorted(list_of_vals[0:mid_idx]))

# Calculating Mean for Standard Deviation
def calcMeanDev (vals):
  fx = 0
  sum_of_f = 0
  for entry in vals:
    fx += entry
    sum_of_f += 1 
  
  mean = fx / sum_of_f
  return mean

# Calculating Inter Quartile
def calcInterQuartile ():
  q3 = calcQMedian(calcUppQuartile())
  q1 = calcQMedian(calcLowQuartile())
  iqr = q3 - q1
  return iqr

raw_data = raw_input("New numerical entry: ")

# Calculating standard deviation
def calcStandardDev ():
  mean = calcMean()

  list_of_vals = []
  new_vals = []
  for entry in frequencies:
    for num in range(0, frequencies[entry]):
      list_of_vals.append(entry) 
  
  for val in list_of_vals:
    new_vals.append((val - mean) ** 2)

  sd = calcMeanDev(new_vals)
  return sd


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
print('Upper Quartile:', calcUppQuartile())
print('Lower Quartile:', calcLowQuartile())
print('Interquartile Range:', calcInterQuartile())
print('Standard Deviation:', calcStandardDev())
```
- Go to this website: https://trinket.io/python
- Erase any existing content from the box
- Paste the source code into the box
- Press the run/play button
- If you look at the bottom right of the screen, it shows 
you where you can enter values