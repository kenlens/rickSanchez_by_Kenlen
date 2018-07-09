def setup():
    size (880, 980)                 # window size
    fill(205, 183, 158)             # skin tone
    ellipse(430, 550, 450, 640)     # x coordinate, y coordinate, width, height # head 
    fill(95, 158, 160)              # unibrow color
    ellipse(440, 400, 388, 100)     # unibrow
    fill(255, 255, 255)
    stroke(0, 0, 0)                 # outline of eye
    ellipse(330, 550, 180, 200)     # left white eye
    fill(255, 255, 255)          
    ellipse(535, 550, 180, 200)     # right white eye
    fill(165, 42, 42)
    ellipse(430, 750, 250, 150)     # mouth
    fill(0, 0, 0)
    ellipse(330, 600, 50, 50)       # left pupil
    fill(0, 0, 0)
    ellipse(550, 600, 50, 50)       # right pupil
    fill(205, 183, 158)
    arc(200, 550, 80, 100, 0, PI+QUARTER_PI, OPEN) 
    fill(95, 158, 160)
    beginShape()
    vertex(80, 80)
    vertex(100, 100)
    vertex(150, 200) 
    endShape()
