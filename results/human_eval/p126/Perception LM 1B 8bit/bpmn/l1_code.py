def sort_integers(num_list):
    if sorted(num_list) == num_list:
        print('The list is already sorted and has no more than one duplicate of the same number.')
        return False
    else:
        print('The list is sorted and has no more than one duplicate of the same number.')
        return True