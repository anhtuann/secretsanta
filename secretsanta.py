import random
import datas

def valid_pick(pick, constraints):
    '''
    Arguments :
        - pick, a list of participants (str)
        - constraints, a dictionary with participants (str) as indexes and tuples of participants (str) as values
    Returns :
        - True if the pick is abiding to the constraints, False otherwise
    '''
    for idx, participant in enumerate(pick[:-1]):
        if pick[idx+1] in constraints[participant]:
            return False
    return pick[-1] not in constraints[pick[0]] and pick[0] not in constraints[pick[-1]]

def matching_participants(participants, constraints):
    '''
    Arguments :
        - participants (list) of names (str) forming an hamiltonian path
        - constraints, a dictionary with participants (str) as indexes and tuples of participants (str) as values
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
        - valid_pick, list of participants (str) forming a correct hamiltonian path
    Returns :
        - couples : list of tuples each containing the pair (gifter, giftee)
    '''
    gifters = list(valid_pick)
    giftees = list(valid_pick[1:] + valid_pick[:1])
    couples = list(zip(gifters, giftees))
    return couples

if __name__ == '__main__':
    pick = matching_participants(datas.participants, datas.constraints)
    couples = create_pairs(pick)
    print(couples)
