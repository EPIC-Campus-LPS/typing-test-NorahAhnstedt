import time

start = time.time()

time_trial = input("Type the following sentence \n The quick brown fox jumps over the lazy dog, its sleek fur shimmering under the golden rays of the setting\nsun. The dog, roused from its nap, lifted one sleepy eye to observe the playful intruder. Can't you let a\nfellow rest in peace? the dog grumbled, though his voice held more amusement than annoyance. The fox, agile\nand unbothered, landed gracefully on the soft grass, tail flicking with mischief. Rest is for those who miss\nthe beauty of the chase, it replied with a sly grin. : \n")

sentence = ("The quick brown fox jumps over the lazy dog, its sleek fur shimmering under the golden rays of the setting sun. The dog, roused from its nap, lifted one sleepy eye to observe the playful intruder. Can't you let a fellow rest in peace? the dog grumbled, though his voice held more amusement than annoyance. The fox, agileand unbothered, landed gracefully on the soft grass, tail flicking with mischief. Rest is for those who miss the beauty of the chase, it replied with a sly grin.")

end = time.time()

seconds_to_minuetes = (end - start)/60
wpm = 94 // seconds_to_minuetes


for ch in time_trial:
    missed = 0
    if ch in time_trial == ch in sentence:
        pass
    else:
        missed += 1

print(f"{wpm}wpm and {missed} letters missed")
