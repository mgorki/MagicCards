"""Contains the two dictionaries Cards and Questions:

The Cards dictionary contains information about all cards presented to participants, namely:
- card's number (ID),
- path where a scan of the according card is stored,
- questions (identified by their IDs) which are asked if the respective card is chosen and
- questions (identified by their IDs) to which the answer ist "yes" concerning the respective card.

The Questions dictionary contains:
- questions number (ID) and
- the actual text (always a single word to which the answer is yes or no) in which the questions consist.

In sum these dictionaries define the questions to be asked concerning any single card and to which questions the correct answer is yes.
Furthermore they contain information to make any single card (scan) clearly identifiable by its number (ID)."""


################Cards (Dictionary)###############
#List of cards, their respective id's and the questions (identified by their id's) to which the answer ist "yes" concerning the respective card.
Cards = {1: {
        "card_number": 1,
        "path": "../resources/images/card_1.jpg",
        #"path": "../../MagicCards/resources/images/card_1.jpg",
        "questions_asked": [1, 2, 3, 14, 15, 16, 17, 28, 29, 30], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [3, 4, 5, 14, 16, 18, 29, 33]
    },
    2: {
        "card_number": 2,
        "path": "../resources/images/card_2.jpg",
        "questions_asked": [1, 3, 10, 11, 12, 17, 23, 24, 30, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 4, 9, 14, 15, 16, 18, 19, 23, 24, 29, 33]
    },
    3: {
        "card_number": 3,
        "path": "../resources/images/card_3.jpg",
        "questions_asked": [1, 2, 4, 7, 8, 9, 12, 13, 23, 27], # PLACEHOLDER, has to be adjusted in the final experiment!
         "questions_yes": [7, 9, 14, 15, 16, 18, 23]
    },
    4: {
        "card_number": 4,
        "path": "../resources/images/card_4.jpg",
        "questions_asked": [7, 4, 8, 9, 10, 13, 15, 17, 22, 27], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 4, 9, 12, 16, 17, 18]
    },
    5: {
        "card_number": 5,
        "path": "../resources/images/card_5.jpg",
        "questions_asked": [2, 4, 5, 9, 18, 19, 21, 26, 27, 32], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [4, 6, 14, 16, 18, 19, 21, 25, 28, 29] #15?
    },
    6: {
        "card_number": 6,
        "path": "../resources/images/card_6.jpg",
        "questions_asked": [3, 5, 6, 9, 10, 12, 16, 20, 21, 24], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [9, 10, 16, 18, 19, 20, 21, 24, 25, 26] #8?
    },
    7: {
        "card_number": 7,
        "path": "../resources/images/card_7.jpg",
        "questions_asked": [1, 2, 3, 4, 12, 16, 22, 28, 29, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 4, 12, 14, 17, 24, 28, 29, 33]
    },
    8: {
        "card_number": 8,
        "path": "../resources/images/card_8.jpg",
        "questions_asked": [3, 6, 8, 10, 17, 22, 25, 28, 31, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 7, 8, 10, 13, 14, 15, 17, 22, 25, 26, 28] #16? 19?
    },
    9: {
        "card_number": 9,
        "path": "../resources/images/card_9.jpg",
        "questions_asked": [1, 3, 5, 8, 12, 16, 23, 24, 26, 31], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 2, 8, 10, 12, 15, 16, 24, 26]
    },
    10: {
        "card_number": 10,
        "path": "../resources/images/card_10.jpg",
        "questions_asked": [2, 7, 11, 13, 15, 18, 19, 21, 25, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 2, 3, 7, 14, 16, 18, 19, 24]
    },
    11: {
        "card_number": 11,
        "path": "../resources/images/card_11.jpg",
        "questions_asked": [1, 3, 7, 10, 11, 14, 23, 25, 28, 29], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 8, 14, 15, 16, 13, 23, 24, 25, 26, 29] #4?
    },
    12: {
        "card_number": 12,
        "path": "../resources/images/card_12.jpg",
        "questions_asked": [3, 5, 6, 7, 9, 10, 16, 24, 26, 28], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 3, 14, 15, 16, 19, 24] #18?
    },
    13: {
        "card_number": 13,
        "path": "../resources/images/card_13.jpg",
        "questions_asked": [3, 6, 8, 14, 18, 21, 22, 21, 32, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [8, 14, 15, 18, 26, 31, 32]
    },
    14: {
        "card_number": 14,
        "path": "../resources/images/card_14.jpg",
        "questions_asked": [2, 3, 4, 8, 14, 20, 22, 27, 29, 30], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [3, 7, 8, 14, 15, 16, 19, 20, 27]
    },
    15: {
        "card_number": 15,
        "path": "../resources/images/card_15.jpg",
        "questions_asked": [3, 11, 12, 15, 18, 21, 22, 26, 28, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 3, 8, 11, 14, 15, 16, 18, 19, 24, 31]
    },
    16: {
        "card_number": 16,
        "path": "../resources/images/card_16.jpg",
        "questions_asked": [3, 6, 10, 13, 16, 18, 24, 25, 30, 32], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 3, 8, 14, 15, 18, 20, 24, 25]
    },
    17: {
        "card_number": 17,
        "path": "../resources/images/card_17.jpg",
        "questions_asked": [6, 10, 12, 13, 15, 19, 24, 27, 28, 29], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 2, 9, 10, 16, 18, 22, 24, 25, 27]
    },
    18: {
        "card_number": 18,
        "path": "../resources/images/card_18.jpg",
        "questions_asked": [3, 5, 9, 14, 17, 18, 25, 28, 32, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [4, 5, 6, 8, 14, 15, 25, 26, 28]
    },
    19: {
        "card_number": 19,
        "path": "../resources/images/card_19.jpg",
        "questions_asked": [2, 4, 13, 18, 20, 26, 27, 29, 32, 33], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [11, 13, 14, 15, 16, 18, 23, 26, 32]
    },
    20: {
        "card_number": 20,
        "path": "../resources/images/card_20.jpg",
        "questions_asked": [1, 2, 5, 14, 19, 20, 22, 25, 30, 31], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 2, 14, 16, 24, 30] #17?
    },
    21: {
        "card_number": 21,
        "path": "../resources/images/card_21.jpg",
        "questions_asked": [1, 6, 7, 9, 11, 16, 24, 28, 31, 32], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 11, 14, 15, 16, 18, 24]
    },
    22: {
        "card_number": 22,
        "path": "../resources/images/card_22.jpg",
        "questions_asked": [1, 7, 10, 12, 13, 14, 17, 18, 23, 32], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [7, 15, 16, 23] #15?
    },
    23: {
        "card_number": 23,
        "path": "../resources/images/card_23.jpg",
        "questions_asked": [1, 2, 3, 4, 14, 19, 22, 24, 26, 29], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 4, 14, 16, 19, 24, 26, 29] #2? 15?
    },
    24: {
        "card_number": 24,
        "path": "../resources/images/card_24.jpg",
        "questions_asked": [1, 3, 4, 9, 10, 17, 19, 22, 25, 27], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 10, 14, 15, 17, 22, 24, 25, 26, 28]  # 8, 16, 29?
    },
    25: {
        "card_number": 25,
        "path": "../resources/images/card_25.jpg",
        "questions_asked": [1, 4, 5, 7, 9, 10, 16, 17, 18, 28], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 4, 7, 16, 17, 18]  # 1, 17?
    },
    26: {
        "card_number": 26,
        "path": "../resources/images/card_26.jpg",
        "questions_asked": [1, 5, 8, 12, 13, 14, 15, 16, 18, 30], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [8, 14, 15, 16, 18, 26]
    },
    27: {
        "card_number": 27,
        "path": "../resources/images/card_27.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": [1, 2, 7, 8, 18]  # 10?
    },
    28: {
        "card_number": 23,
        "path": "../resources/images/card_28.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": []
    },
    29: {
        "card_number": 23,
        "path": "../resources/images/card_29.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": []
    },
    30: {
        "card_number": 23,
        "path": "../resources/images/card_30.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": []
    },
    31: {
        "card_number": 23,
        "path": "../resources/images/card_31.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": []
    },
    32: {
        "card_number": 23,
        "path": "../resources/images/card_32.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": []
    },
    33: {
        "card_number": 23,
        "path": "../resources/images/card_33.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": []
    },
    34: {
        "card_number": 23,
        "path": "../resources/images/card_34.jpg",
        "questions_asked": [], # PLACEHOLDER, has to be adjusted in the final experiment!
        "questions_yes": []
    },
}


################Questions (Dictionary)###############
##Some example questions for testing at this stage
Questions = { 1: {
            "question_number": 1,
            "text": "Belebtes" #living beeing(s)
        },
        2: {
            "question_number": 2,
            "text": "Fabelwesen" #mythical/fabulous creature
        },
        3: {
            "question_number": 3,
            "text": "Vogel" #bird
        },
        4: {
            "question_number": 4,
            "text": "Gebäude" #building(s)
        },
        5: {
            "question_number": 5,
            "text": "Treppe" #stairways
        },
        6: {
            "question_number": 6,
            "text": "Laterne" #lantern/lamp
        },
        7: {
            "question_number": 7,
            "text": "Wasser" #water
        },
        8: {
            "question_number": 8,
            "text": "Pflanze" #plant
        },
        9: {
            "question_number": 9,
            "text": "Maschine" #machine
        },
        10: {
            "question_number": 10,
            "text": "Hut" #hat
        },
        11: {
            "question_number": 11,
            "text": "Obst" #fruit
        },
        #The questions up to here should be enough to identify any card.
        #The following questions are not strictly necessary to identify a card, if all of the questions above have been answered.
        12: {
            "question_number": 12,
            "text": "Rauch" #smoke
        },
        13: {
            "question_number": 13,
            "text": "Geld" #money
        },
        14: {
            "question_number": 14,
            "text": "Gelb" #yellow
        },
        15: {
            "question_number": 15,
            "text": "Grün" #green
        },
        16: {
            "question_number": 16,
            "text": "Blau" #blue
        },
        17: {
            "question_number": 17,
            "text": "Mensch" #human beeing
        },
        18: {
            "question_number": 18,
            "text": "Metall" #metal
        },
        19: {
            "question_number": 19,
            "text": "Himmel" #sky
        },
        20: {
            "question_number": 20,
            "text": "Gefrorenes" #something frozen
           },
        21: {
            "question_number": 21,
            "text": "Schal"  # scarf
        },
        22: {
            "question_number": 22,
            "text": "Bart"  # beard
        },
        23: {
            "question_number": 23,
            "text": "Papier"  # paper
        },
        24: {
            "question_number": 24,
            "text": "Auge"  # eye
        },
        25: {
            "question_number": 25,
            "text": "Stoff"  # cloth/fabric/textile
        },
        26: {
            "question_number": 26,
            "text": "Holz"  # wood
        },
        27: {
            "question_number": 27,
            "text": "Schrift"  # scripture/writing(s)
        },
        28: {
            "question_number": 28,
            "text": "Tür"  # door
        },
        29: {
            "question_number": 29,
            "text": "Fenster"  # window(s)
        },
        30: {
            "question_number": 30,
            "text": "Feuer"  # fire
        },
        31: {
            "question_number": 31,
            "text": "Schwert"  # sword
        },
        32: {
            "question_number": 32,
            "text": "Schlüssel"  # key
        },
        33: {
            "question_number": 33,
            "text": "Zinnen"  # merlons
        }

}
##############################################
