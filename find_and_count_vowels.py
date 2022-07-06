# finds and counts vowels

vowels = ["a","e","I","o","u","y"]
test = "racecar"
vowel_count = 0
for x in vowels:
    if test.find(x) >= 0:
        print("Found ", x, " in " + test + " at ", test.find(x))
        if test.find(x) >= 0:
            print("Found ", x, " in " + test + " at ", test.find(x))
