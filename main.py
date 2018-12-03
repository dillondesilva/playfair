frequencies = {}

# Calculating the mean
def calcMean (dataset):
  fx = 0
  for entry in frequencies:
    fx += entry * frequencies[entry]
  
  mean = fx / len(frequencies) 
  return mean

def calcMedian (dataset):
  // This is a stub

# Calculating Mode
def calcMode (dataset):
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




def calcRange (dataset):
  // This is a stub

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