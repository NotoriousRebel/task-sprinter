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
    print_menu()
    option = get_option() # not implemented correctly, lacks input validation

    if options[option] == 'START':
        print('Starting')
        pass
    elif options[option] == 'ADD':
        print('Adding')
        pass
    elif options[option] == 'REMOVE':
        print('Removing')
        pass
    elif options[option] == 'EDIT':
        print('Editing')
        pass
    else: # EXIT
        print('Exiting')
        sys.exit()



