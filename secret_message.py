"""
Task 1.  Display the input message at positions that are present in the Fibonacci 
sequence (a sequence formed by the the
Fibonacci number sorted in ascending order). Please ignore whitespace 
characters and use the extended Fibonacci.
Return the obtained characters capitalized and connected by the '*-*' character.
"""

def main():
    
    # fetching input from users
    message, message_length = get_formatted_input_message()
    
    # getting postions of characters in string which is to be displayed
    positions = list(fibonacci(message_length))
    
    # processing string 
    secret_message = process_string(message, positions)
    
    #displaying processed output string
    print "Secret Message is: {}".format(secret_message)

def process_string(message, pos):
    """
    :param message:Input message
    :param pos: Positions of character to be taken
    :return: Processed string
    """
    return '*-*'.join([message[index] for index in pos]).upper()
    

def get_formatted_input_message():
    """
    :return: Input string from user
    """
    message_length = 0
    message = ''
    while(True):
        message = raw_input("Enter message(len: 1 - 255): ").replace(" ", "")
        message_length = len(message)
        if message_length >= 1 and message_length <= 255:
            break
    return message, message_length


def fibonacci(max_num):
    """
    :param max_num: Max num to which fibonacci series to be displayed
    :return: Fibonacci series up to max_num
    """
    a, b = 0, 1
    while(True):
        yield a
        a, b = b, a + b
        if a >= max_num:
            break

if __name__ == '__main__':
    main()
