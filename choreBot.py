# Import libraries



# Dictionary initialization
chores = {0:"weekly", 1:"dishler", 2:"warden", 3:"counter", 4:"livingRoom", 5:"trash", 6:"unload"}

isaac = 0
adam = 1
benji = 2
arya = 3
troy = 4
steve = 5
cameron = 6


# FIFO Queue for weekly
weekly = ['isaac', 'steve', 'troy', 'adam', 'arya', 'benji', 'cameron']

def weekly_roto():
    popped = weekly.pop(0)
    weekly.append(popped)

print(f'before roto: {weekly}')

weekly_roto()

print(f'after roto: {weekly}')

# Chore algo




