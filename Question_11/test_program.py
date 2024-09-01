
from relaxation import Relaxation
from adventure import Adventure


advnture = Adventure(destination='Turkey' ,price=2500 , sea_activites=['Hiking','Rafting'])
relaxation = Relaxation(destination='Hurghada' ,price=3000 , spa_services=['Massage','Yoga'])

advnture.display_details()
relaxation.display_details()