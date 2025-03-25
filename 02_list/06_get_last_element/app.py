def get_lst():
    """ Prompts the user to enter one element of the list at a time and returns the resulting list. """
    lst = [] 
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem) 
        elem = input("Please enter an element of the list or press enter to stop. ") 
        return lst

def get_last_elem(lst):
    return lst[-1]
def main():
     
    lst = get_lst()
    get_last_elem(lst)
    
  

if __name__ == 'main': 
    main()