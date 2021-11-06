def decode_to_string(bytes):
    '''convert bytes into string'''
    return bytes.decode("utf-8")

def get_countries_from_string(string):
    '''extract the countries from the string'''
    arr_of_countries = []
    start = None
    # loop and slice countries from string
    for idx in range(len(string)):
        # " can be start or end of string
        if string[idx] == '"':
            # next char is a comma or closing bracket, indicates end of string
            if string[idx + 1] == ',' or string[idx + 1] == ']':
                arr_of_countries.append(string[start:idx])
            # else its the start of the string
            else:
                start = idx + 1

    return arr_of_countries
