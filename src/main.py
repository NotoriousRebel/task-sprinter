import sys


options = {'1': 'START',
           '2': 'ADD',
           '3': 'REMOVE',
           '4': 'EDIT',
           '5': 'EXIT',}

def get_option():
    option = input()
    return option

def print_menu():
    print("""
        ================= TASK SPRINTER  =================
        1 - Start routine
        2 - Add routine
        3 - Remove routine
        4 - Edit routine
        5 - Exit
        ==================================================
    """)

if __name__ == "__main__":
    while True:
        print_menu()
        option = get_option() # lacks input validation
        if options[option] == 'START':
            print('Starting')
            routine = choose_routine()
            routine.start()

        elif options[option] == 'ADD':
            print('Adding')
            routine = choose_routine()
            routine.add()

        elif options[option] == 'REMOVE':
            print('Removing')
            routine = choose_routine()
            routine.remove()

        elif options[option] == 'EDIT':
            print('Editing')
            routine = choose_routine()
            routine.edit()

        else: # EXIT
            print('Exiting')
            sys.exit()



