# The pass statement is a null statement.
# But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored. 

def sample_function():
    pass

class sampleClass:
    pass

n = 10
for i in range(n):
    # pass can be used as placeholder
    # when code is to added later
    pass

print("All the other statements will be executed normally!")