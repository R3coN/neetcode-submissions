class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            match i:
                case '(':
                    stack.append(i)
                case '{':
                    stack.append(i)
                case '[':
                    stack.append(i)
                case ')':
                    if len(stack) > 0:
                        top = stack.pop()
                        if top != '(':
                            return False
                    else:
                        return False
                case '}':
                    if len(stack) > 0:
                        top = stack.pop()
                        if top != '{':
                            return False
                    else:
                        return False
                case ']':
                    if len(stack) > 0:
                        top = stack.pop()
                        if top != '[':
                            return False
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False