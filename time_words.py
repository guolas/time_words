"""
Map from number to text
"""
number_to_text = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    21: "twenty one",
    22: "twenty two",
    23: "twenty three",
    24: "twenty four",
    25: "twenty five",
    26: "twenty six",
    27: "twenty seven",
    28: "twenty eight",
    29: "twenty nine",

}

"""
Get the hours and the minutes
"""
H = int(input().strip())
M = int(input().strip())

if M == 0:
    time = number_to_text[H] + " o'clock"
elif M == 15:
    time = "quarter past " + number_to_text[H]
elif M == 30:
    time = "half past " + number_to_text[H]
elif M == 45:
    time = "quarter to " + number_to_text[H]
elif M == 1:
    time = number_to_text[M] + " minute past " + number_to_text[H]
elif M == 59:
    time = number_to_text[60 - M] + " minute to " + number_to_text[H]
elif M < 30:
    time = number_to_text[M] + " minutes past " + number_to_text[H]
else:
    time = number_to_text[60 - M] + " minutes to " + number_to_text[H]

print(time)
