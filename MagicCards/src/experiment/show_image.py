from experiment.cards_and_questions import Cards
from psychopy import visual
from general.config_hardware import WIN
from random import randrange

def show_cardimage(card_number):  # Presenting the scan of the chosen card or a random other card
    randnum = randrange(0, 5)
    if randnum == 1: # Defining the probability for erroneosly showing a random cards image
        randcard = randrange(1, 22)  # choosing a random card
        image_number = randcard
    else:
        image_number = card_number

    ## presenting the card ##
    card_image = Cards[image_number]['path']
    img = visual.ImageStim(WIN, image=card_image, size=(240, 360))  # All images of cards are roughly 1200 x 1800 pixel
    img.draw(WIN)
    WIN.flip()