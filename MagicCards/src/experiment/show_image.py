from experiment.cards_and_questions import Cards
from psychopy import visual
from general.config_hardware import WIN
import experiment.config_experiment as config_experiment
from random import randrange

def show_cardimage(card_number):  # Presenting the scan of the chosen card or a random other card
    randnum = randrange(1, 101)
    if randnum in range(1, ((100 - config_experiment.PERCENTAGECORRECTCARD) + 1)): # If random number (from 1 to 100) is in range defined for erroneosly showing a random cards image
        randcard = randrange(1, (config_experiment.NUMOFIMAGES + 1))  # choosing a random card within the range of images
        image_number = randcard
    else:
        image_number = card_number  # show the card actually chosen

    ## presenting the card ##
    card_image = Cards[image_number]['path']
    img = visual.ImageStim(WIN, image=card_image, size=(12, 23))  # All images of cards are roughly 1200 x 1800 pixel
    img.draw(WIN)
    WIN.flip()
    return image_number
