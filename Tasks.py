tasks = input ("Enter your tasks for today separated by a comma: \n").split(', ') 
done_tasks = []
ongoing_tasks = []
for x in tasks :
    print()
    print(x)
    print()
    done = input(f"Did you finish {x} already ?\n").lower()
    if done == "yes" :
        done_tasks.append(x)
        print("Nice jop")
        print("----------\n")
    else:
        ongoing_tasks.append(x)
        print("----------\n")
        print("Try not to put it off")
user_choice = input ("Do you want to see your todays progress? (yes, no)\n").lower()
if user_choice == "yes" :
   print("                 *************Done Tasks*******************                 ") 
   print(f'\n{done_tasks}\n')          
   print("                 *************Ongoing Tasks****************                  ")
   print(f'\n{ongoing_tasks}\n')
else :   
    print("Please press enter to exite ")