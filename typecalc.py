from time import time
import random as r

def mistake(paratest, user):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != user[i]:
                error += 1
        except IndexError:
            error += 1
    return error 

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed, 2)

test = [
    "Ratan Tata was born in Bombay, now Mumbai, during the British Raj, into a Parsi Zoroastrian family, on 28 December 1937.",
    "[8] He is the son of Naval Tata, who was born in Surat and later adopted into the Tata family, and Sooni Tata, the niece of Tata group founder Jamsetji Tata.",
    "Tata's biological grandfather, Hormusji Tata, was a member of the Tata family by blood.",
    "In 1948, when Tata was 10, his parents separated, and he was subsequently raised and adopted by Navajbai Tata, his grandmother and widow of Ratanji Tata.",
    "[9] He has a younger brother Jimmy Tata[10] and a half-brother, Noel Tata, from Naval Tata's second marriage with Simone Tata, with whom he was raised."
]

test1 = r.choice(test)

print("******Typing Speed*****")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter :")
time_2 = time()

print("Speed:", speed_time(time_1, time_2, testinput), "characters/sec")
print("Errors:", mistake(test1, testinput))
