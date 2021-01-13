txt1 = open("extext.txt", "r")
txt2 = open("extext2.txt", "r")

txt1 = str(txt1).split(" ")
txt2 = str(txt2).split(" ")

txt1 = set(txt1)
txt2 = set(txt2)

intersect = txt1.intersection(txt2)
num_shared = str(len(intersect))
print("The number of shared words is: " + num_shared)
