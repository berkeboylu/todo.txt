exec(open('lib/commands.py').read())

# if file's doesn't exists
if (os.path.exists(PATH) == False):
    with open(PATH, 'a'):
        os.utime(PATH, None)

while True:
    input_ = input().split(" ")
    if input_[0] == "t":
        if input_[1] == "and" or input_[1] == "a": todo.add(input_[2::]) 
        elif input_[1] == "append" or input_[1] == "app": todo.append(input_[2::])
        elif input_[1] == "list" or input_[1] == "ls": todo.list(input_[2::])
        elif input_[1] == "listpri" or input_[1] == "lsp": todo.listpri(input_[2::])