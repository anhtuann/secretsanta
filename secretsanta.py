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

def valid_pick(pick):
    '''
    Arguments :
        - pick, a list of Participant objects
    Returns :
        - True if the pick is abiding to the constraints in each Participant's blacklist, False otherwise
    '''
    for idx, participant in enumerate(pick[:-1]):
        if pick[idx+1].getName() in participant.getBlacklist():
            return False
    return pick[-1].getName() not in pick[0].getBlacklist() and pick[0].getName() not in pick[-1].getBlacklist()

def matching_participants(participants):
    '''
    Arguments :
        - participants (list) of Participant objects
    Returns :
        - pick, same format as participants but shuffled and abiding to the constaints in each Participant's blacklist
    '''
    while True:
        pick = list(participants)
        random.shuffle(pick)
        if valid_pick(pick):
            return pick

def create_pairs(valid_pick):
    '''
    Arguments :
        - valid_pick, list of Participant objects forming a correct hamiltonian path
    Returns :
        - couples : list of tuples each containing the pair (gifter (Participant obj), giftee (Participant obj))
        - also update each Participant object's gifter and giftee values
    '''
    gifters = list(valid_pick)
    giftees = list(valid_pick[1:] + valid_pick[:1])
    couples = list(zip(gifters, giftees))
    for pair in couples:
        gifter, giftee = pair
        gifter.giftee = giftee
        giftee.gifter = gifter
    return couples

if __name__ == '__main__':
    participants = [Participant(name) for name in datas.participants]
    for participant in participants:
        participant.blacklist.extend(datas.constraints[participant.getName()])
    pick = matching_participants(participants)
    couples = create_pairs(pick)
    print(couples)
