'''
you are given an array of desired filenames in the order of their creation. since two 
files cannot have equal names, the one which comes later will have an addition to its name in a form of (k),
where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files
'''
def get_names_freq(names):
    names_freq = {}
    
    for name in names:
        if name not in names_freq:
            names_freq[name] = 1
        else:
            names_freq[name] += 1
            name_count = str(names_freq[name] - 1)
            new_filename = name + "(" + name_count + ")"
    
    return names_freq


# edit: just do dictionary stuff separately
def fileNaming(names):
    print "start: ", names
    names_freq = {}
    new_names = []
    file_system = {}
    
    names_freq = get_names_freq(names)
    print names_freq
    
    # just think about the file system
    for name in names:
        if name not in file_system:
            file_system[name] = 1
            new_names.append(name)
        else:
            name_count = str(names_freq[name] - 1)
            new_filename = name + "(" + name_count + ")"
            file_system[new_filename] = 1
            
            
    
    return new_names

test1 = ["doc", "doc", "image", "doc(1)", "doc"]
# ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]

test2 = ["a(1)", "a(6)", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
# ["a(1)", "a(6)", "a", "a(2)", "a(3)", "a(4)", "a(5)", "a(7)", "a(8)", "a(9)", "a(10)", "a(11)"]

test3 = ["dd", "dd(1)", "dd(2)", "dd", "dd(1)", "dd(1)(2)", "dd(1)(1)", "dd", "dd(1)"]

print fileNaming(test1)

    
    