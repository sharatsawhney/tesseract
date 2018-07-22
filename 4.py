import difflib

a = 'How are you, buddy? Hope you are great and enjoying.'
b = 'How r u, buddy? Hop u are grate & enjying!'

file1 = "out14.txt"
file2 = "out15.txt"
d = difflib.Differ()
diff = list(d.compare(open(file1).readlines(),open(file2).readlines()))
print(diff)
