test = ['one', 'two', 'three']

# print(" ".join(test))

user_in = input("Enter a list of words:\n")

user_input = user_in.split(', ')
out = " ".join(user_input)

print(user_input)

print(out)