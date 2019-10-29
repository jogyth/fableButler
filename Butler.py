# Noen grunnvariabler
leftArm = 'CNM'
rightArm = 'GTM'
wheels = 'UQI'

# Litt basic config ved oppstart
def config():
  api.setSpeed(50,50, rightArm)
  api.setSpeed(50,50, leftArm)
  api.setTorque(50,50, rightArm)
  api.setTorque(50,50, leftArm)
  api.setAccurate('default', 'default', rightArm)
  api.setAccurate('default', 'default', leftArm)
  api.setPos(-45, -90, rightArm)
  api.setPos(45, -90, leftArm)
  api.setFaceEmotion('Neutral')

# Funksjon for bevegelse 
def drive():
  while True:
    # Anti-kræsj
    avstand = api.getSpinSensorReading('proximity', 2 , wheels)
    if int(avstand) in range(1, 90):
      api.print("Fare for kræsj - vent 10 sekunder")      
      api.setSpinSpeed(0,0, wheels) 
      api.setColor([100, 0, 0], 'Hub')
      blink()
      api.setFaceEmotion('Angry')
      api.wait(10)
      api.setColor([20, 100, 20], 'Hub')
      api.setFaceEmotion('Surprised')
      api.print("Nå kan du kjøre igjen")

    # Ansikt
    # Får ikke kamera i min telefon til å streame.
    # Har googlet problemet, men finner ingen løsningsforslag
    #if api.detectedMotion(2):
      #api.setFaceEmotion('Happy')
      #api.playSound("laugh.wav", 'Face')
      #api.wait(3)
      #api.setFaceEmotion('Neutral')      
      #api.print("Ser deg!")
      
    # Hjul
    if api.isPressed('up'):
      api.setSpinSpeed(-50, 50, wheels)
    elif api.isPressed('down'):
      api.setSpinSpeed(50, -50, wheels)
    elif api.isPressed('left'):
      api.setSpinSpeed(-50, -50, wheels)
    elif api.isPressed('right'):
      api.setSpinSpeed(50, 50, wheels)
      
    # Armer
    elif api.isPressed('a'):
      api.setPos(90,-90, leftArm)
      api.setPos(-90,-90, rightArm)
    elif api.isPressed('z'):
      api.setPos(-45, -90, rightArm)
      api.setPos(45, -90, leftArm)    
    elif api.isPressed('w'):
      wave()
    elif api.isPressed('s'):
      serve()     
    else:
      api.setSpinSpeed(0, 0, wheels)        
      api.setPos(90,-90, leftArm)
      api.setPos(-90,-90, rightArm)        
      
def serve():
    api.print('Server noe godt')
    api.setPos(0,20, leftArm)
    api.wait(4) # Her må du forsyne Fable med en marshmellow i klypa
    api.setPos(90,20, leftArm)
    api.setFaceEmotion('Happy')
    api.playSound("boing.wav", 'Face')
    api.wait(15)
    api.setPos(90,-90, leftArm)
    api.wait(2)
    api.setFaceEmotion('Neutral')
      
def blink():
    i = 0
    while i < 25:
      api.setColor([100,0,0], wheels)
      api.wait(0.2)
      api.setColor([20,100,20], wheels)
      api.wait(0.2)
      i += 1
      
def wave():
    api.print("Vink")
    i = 0
    while i < 7:
      api.setPos(45, 90, leftArm)
      api.wait(0.4)
      api.setPos(45, 60, leftArm)
      api.wait(0.4)
      i += 1    


# Kjør hovedprogram
while True:
  config()
  drive() 
  

