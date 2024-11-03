def evaluatePostfix(givenExp):
    givenstack = []
    for charact in givenExp:
        if charact.isdigit():
            givenstack.append(int(charact))
        else:
            topfirst = givenstack.pop()
            topsecond = givenstack.pop()
            if charact == '+':
                givenstack.append(topsecond + topfirst)
            elif charact == '-':
                givenstack.append(topsecond - topfirst)
            elif charact == '*':  # Changed '×' to '*'
                givenstack.append(topsecond * topfirst)
            elif charact == '/':
                givenstack.append(topsecond // topfirst)  # Integer division
    return givenstack.pop()

# Main program
givenExp = input('Enter a postfix expression: ')
print('The value of the given postfix expression:', evaluatePostfix(givenExp))
