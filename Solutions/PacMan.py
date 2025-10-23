def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active == True and touching_ghost == True: 
        return True
    else: 
        return False
def score(touching_power_pellet, touching_dot):
    if touching_power_pellet != True and touching_dot != True:
        return False
    elif touching_dot == False and touching_power_pellet == True:
        return True
    else:
        return True
def lose(power_pellet_active, touching_ghost):
    if touching_ghost == True and not power_pellet_active:
        return True
    else:
        return False
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots == True and touching_ghost == False and not power_pellet_active:
        return True
    elif has_eaten_all_dots == True and touching_ghost == True and power_pellet_active == True:
        return True
    else:
        return False