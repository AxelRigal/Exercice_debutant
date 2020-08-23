code = "print(any(('py' or 'txt') in ext for ext in ['.py', '.obj', '.json']))"

print(code.count('(') == code.count(')'))
