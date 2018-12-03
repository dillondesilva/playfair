frequencies = {}

def calcMean (dataset):
  fx = 0
  for entry in frequencies:
    fx += entry * frequencies[entry]
  
  mean = fx / len(frequencies) 
  return mean

def calcMedian (dataset):
  // This is a stub

def calcMode (dataset):
  // This is a stub

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