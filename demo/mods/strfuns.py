print('Name : ', __name__)

NEWLINE = '\n'

def find_first_space_pos(st : str) -> bool:
    """
    Returns the position of first space
    :param st: Input string
    :return: Position of first space. -1 if no space is found
    """
    return  st.find(' ')

def count_spaces(st : str) -> int:
    """
    Returns number of spaces in the given string
    :param st: Input string
    :return: Number of space
    """
    return  st.count(' ')


