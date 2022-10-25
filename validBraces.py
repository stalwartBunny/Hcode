def containsValidBraces():
    evalString = input("Input the evaluation string: ")
    validity = False
    stack = []

    for char in evalString:

        if len(stack) == 0:
            stack.append(char)

        else:
            if char == ')' and stack[-1] == '(':
                stack.pop()

            elif char == '}' and stack[-1] == '{':
                stack.pop()

            elif char == ']' and stack[-1] == '[':
                stack.pop()

            else:
                stack.append
    if stack:
        validity = False
    else:
        validity = True

    if validity == True:
        print("valid")
    else:
        print("invalid")


containsValidBraces()
