
import time, sys

check_yes = ['yes', 'y']  
check_no = ['no', 'n'] #we need this arrays for if else statement

print("Welcome to Mitigating Circumstances! You will be required to answer to the questions Yes or No")
print("CW Submission:") #Introduction


# this function is nothing but makes load animation
def waiting():
    for i in range(9):
        sys.stdout.write("   ")
        x = i % 4
        sys.stdout.write('\r' + "." * x)
        time.sleep(0.5)
        sys.stdout.flush()

common_answers = {
    "full_mark": "You will get your full mark!",
    "zero_mark": "You will get 0 mark! Next time study hardly and get high marks!",
    "error": "Please make clear that your answer should be only YES or NO!!!" 
} # we need this dictionary to print the results, We made this dict because this three answers very common


