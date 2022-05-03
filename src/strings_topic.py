def vertical_print(a_string: str):
    """
    Print out a string vertically. In other words, print out a single character on each line

    :param a_string: Some string to print out
    :type a_string String
    """
    character_index = 0
    while character_index < len(a_string):
        print(a_string[character_index])
        character_index += 1
