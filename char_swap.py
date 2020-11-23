password = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
pass_list = list(password)


def TextFileEncyption(offset, txt):
    '''This will convert the text file that the user inputted earlier,
       using the offset factor to do so'''
    Message = ""
    print("The program is now going to encrypt your chosen text file...")
    # go through each character in the input text
    for char in txt:
        number = ord(char)
        # ...and only modify characters that are *not* a space character
        if number != 32:
            number = number + offset
            if number > 126:
                number -= 94
        # ...then convert the value back into a character
        ASCIIletter = chr(number)
        # and append it to the message variable for output.
        Message += ASCIIletter
    print(Message)



if __name__ == "__main__":
    import sys
    inText = "map"
    if len(sys.argv) > 1:
        inText = sys.argv[1]
    TextFileEncyption(2, inText)
