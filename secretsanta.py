import random
import itertools
import datas

class Participant():
    newID = itertools.count().__next__

    def __init__(self, name):
        self.name = name
        self.id = Participant.newID()
        self.email = ''
        self.giftee = ''
        self.gifter = ''
        self.blacklist = []

    def __repr__(self):
        return self.name

    def getName(self):
        return self.name

    def getGiftee(self):
        return self.giftee

    def getGifter(self):
        return self.gifter

    def getBlacklist(self):
        return self.blacklist

def valid_pick(pick, constraints):
    '''
    Arguments :
        - pick, a list of Participant objects
        - constraints, a dictionary with participants' names (str) as indexes and tuples of participants (str) as values
    Returns :
        - True if the pick is abiding to the constraints, False otherwise
    '''
    for idx, participant in enumerate(pick[:-1]):
        if pick[idx+1].getName() in constraints[participant.getName()]:
            return False
    return pick[-1].getName() not in constraints[pick[0].getName()] and pick[0].getName() not in constraints[pick[-1].getName()]

def matching_participants(participants, constraints):
    '''
    Arguments :
        - participants (list) of Participant objects
        - constraints, a dictionary with participants' names (str) as indexes and tuples of participants (str) as values
    Returns :
        - pick, same format as participants but shuffled and abiding to the constaints
    '''
    while True:
        pick = list(participants)
        random.shuffle(pick)
        if valid_pick(pick, constraints):
            return pick

def create_pairs(valid_pick):
    '''
    Arguments :
        - valid_pick, list of Participant objects forming a correct hamiltonian path
    Returns :
        - couples : list of tuples each containing the pair (gifter (Participant obj), giftee (Participant obj))
    '''
    gifters = list(valid_pick)
    giftees = list(valid_pick[1:] + valid_pick[:1])
    couples = list(zip(gifters, giftees))
    return couples

if __name__ == '__main__':
    participants = [Participant(name) for name in datas.participants]
    pick = matching_participants(participants, datas.constraints)
    couples = create_pairs(pick)
    print(couples)
