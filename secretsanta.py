import random
import datas

def valid_pick(pick, constraints):
    for idx, participant in enumerate(pick[:-1]):
        if pick[idx+1] in constraints[participant]:
            return False
    return pick[-1] not in constraints[pick[0]] and pick[0] not in constraints[pick[-1]]

def matching_participants(participants, constraints):
    while True:
        pick = list(participants)
        random.shuffle(pick)
        if valid_pick(pick, constraints):
            return pick

if __name__ == '__main__':
    print(matching_participants(datas.participants, datas.constraints))
