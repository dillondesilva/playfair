frequencies = {}

# Calculating the mean
def calcMean ():
  fx = 0
  for entry in frequencies:
    fx += entry * frequencies[entry]
  
  mean = fx / len(frequencies) 
  return mean

def calcMedian ():
  // This is a stub

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
  // This is a stub

def calcLowQuartile (dataset):
  // This is a stub

def calcInterQuartile (dataset):
  // This is a stub

raw_data = int(input('New numerical entry: '))

while raw_data:
  if raw_data in frequencies:
    frequencies[raw_data] += 1
  else:
    frequencies[raw_data] = 1

  raw_data = int(input('New numerical entry: '))