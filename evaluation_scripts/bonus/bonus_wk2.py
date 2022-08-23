# %% 
import sys
sys.path.insert(1, '../')
import eval_functions as ef
# %%
# Name: Laura Condon 
# Description: Assigning bonus points to the first 3 people alphabetically 
# who are not otherwise getting points
weeknum = 2

all_names = ef.getFirstNames()
print('Everyone:', all_names)
print()

#make a list of all the people who got points this week
points_list = ['Josh', 'Xingyu', 'Sierra', 'Xueyan', 'Andrew', 'Gigi', 'Jason', 'Monique']
print('People getting points already:', points_list)
print()

# Make a list of the names of people not getting points
# Example with a list comprehension
nopoints_list = [name for name in all_names if name not in points_list]

#Example doing the same thign with a loop
#nopoints_list = []
#for name in all_names:
#    if name not in points_list:
#        nopoints_list.append(name)

#Choose the first 3 people not getting points
bonus_names = nopoints_list[0:3]

print("People Getting bonus points:", bonus_names)
print()

#Write out the bonus points
ef.write_bonus(bonus_names, all_names, weeknum)

# %%
