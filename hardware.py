

def getProbeNames():
  return ['probe1', 'probe2']

def getProbe(probeName):
  if probeName == 'probe1':
    return {
      'name': 'probe1',
      'c': 60,
      'f': 140
    }
  elif probeName == 'probe2':
    return {
      'name': 'probe2',
      'c': 70,
      'f': 158
    }
  else:
    return None



def getHeaterNames():
  return ['heater1', 'heater2']

def getHeater(heaterName):
  if heaterName == 'heater1':
    return {
      'name': 'heater1',
      'status': 'on'
    }
  elif heaterName == 'heater2':
    return {
      'name': 'heater2',
      'status': 'off'
    }
  else:
    return None

def setHeater(name, status):
  if name == 'heater1':
    print('heater1 set to :', status)
  elif name == 'heater2':
    print('heater2 set to :', status)
  else:
    print('Invalid heater name (', name, ')')
  



def getPropellorNames():
  return ['properllor1', 'properllor2']

def getPropellor(name):
  if name == 'properllor1':
    return {
      'name': 'properllor1',
      'status': 'on'
    }
  elif name == 'properllor2':
    return {
      'name': 'properllor2',
      'status': 'off'
    }
  else:
    return None

def setPropellor(name, status):
  if name == 'propellor1':
    print('propellor1 set to :', status)
  elif name == 'propellor2':
    print('propellor2 set to :', status)
  else:
    print('Invalid propellor name (', name, ')')
  

def getLCDLineCount():
  return 2

def getLCDLineWidth():
  return 16

def setLCDText(line, value):
  if line >= 1 and line <= getLCDLineCount():
    truncated = value[:getLCDLineWidth()]
    print('LCD line', line, 'set to:', truncated)
  else:
    print('LCD line', line, 'not set to:', value)



def getBuzzer():
  return {
    'frequency': 0
  }

def setBuzzer(frequency):
  if frequency == 0:
    print('Buzzer set to "off"')
  else:
    print('Buzzer frequency :', frequency) 
