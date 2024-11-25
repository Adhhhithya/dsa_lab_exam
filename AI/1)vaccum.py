def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter location of vacuum (A or B): ")
    status_input = input(f"Enter state of {location_input} (1 for Dirty, 0 for Clean): ")
    status_input_complement = input("Enter state of the other room (1 for Dirty, 0 for Clean): ")

    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty")
            goal_state['A'] = '0'
            cost += 1
            print("COST for CLEANING A: " + str(cost))
            print("Location A has been cleaned")

            if status_input_complement == '1':
                print("Location B is Dirty")
                print("Moving right to Location B")
                cost += 1
                print("COST for moving RIGHT: " + str(cost))
                goal_state['B'] = '0'
                cost += 1
                print("COST for SUCK: " + str(cost))
                print("Location B has been cleaned")
            else:
                print("No action: " + str(cost))
                print("Location B is already clean")

        if status_input == '0':
            print("Location A is already clean")
            if status_input_complement == '1':
                print("Location B is Dirty")
                print("Moving right to Location B")
                cost += 1
                print("COST for moving RIGHT: " + str(cost))
                goal_state['B'] = '0'
                cost += 1
                print("COST for SUCK: " + str(cost))
                print("Location B has been cleaned")
            else:
                print("No action: " + str(cost))
                print("Location B is already clean")

    elif location_input == 'B':
        print("Vacuum is placed in Location B")
        if status_input == '1':
            print("Location B is Dirty")
            goal_state['B'] = '0'
            cost += 1
            print("COST for CLEANING B: " + str(cost))
            print("Location B has been cleaned")

            if status_input_complement == '1':
                print("Location A is Dirty")
                print("Moving LEFT to Location A")
                cost += 1
                print("COST for moving LEFT: " + str(cost))
                goal_state['A'] = '0'
                cost += 1
                print("COST for SUCK: " + str(cost))
                print("Location A has been cleaned")
            else:
                print("No action: " + str(cost))
                print("Location A is already clean")

        if status_input == '0':
            print("Location B is already clean")
            if status_input_complement == '1':
                print("Location A is Dirty")
                print("Moving LEFT to Location A")
                cost += 1
                print("COST for moving LEFT: " + str(cost))
                goal_state['A'] = '0'
                cost += 1
                print("COST for SUCK: " + str(cost))
                print("Location A has been cleaned")
            else:
                print("No action: " + str(cost))
                print("Location A is already clean")

    print("GOAL STATE: ", goal_state)
    print("Performance measurement: " + str(cost))

vacuum_world()
