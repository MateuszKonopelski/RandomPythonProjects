'''Function "intersect" takes multiple arguments
and find a common element in each of them'''

def intersect(*args):
    '''
    Method used: One by one element from each argument
    loop through all arguments and return it if
    it is find in each of the arguements.

    :param args: Strings or lists
    :return: List with common elements.
    '''
    common = []
    for element in args:                    # loop for each argument
        '''
        Method used: multiple
        '''
        for i in element:                   # loop for each element in argument
            count = 0
            for element in args:            # loop again for each argument
                if i in element:            # check if element is in this argument
                    count += 1              # if yes count it
                if count == len(args):      # if element is in all arguments count =
                    common.append(i)        # number of all arguments.
    print(list(set(common)))                # delete multiplicates and print as list
