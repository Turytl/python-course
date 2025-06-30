# Output = ["1-cock.txt", "1-balls.txt", "1-cum.txt"]
filenames = ["1.cock", "1.balls", "1.cum"]

new_filename = [filename.replace(".", "-") + ".txt" for filename in filenames]

print(new_filename)
