
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

#this is main function
def MC(CW_sub):
    while True:
        if CW_sub in check_yes:
            print(common_answers["full_mark"])
            break
        elif CW_sub in check_no:
            CW_24 = input("Was your submission next day, within 24 hours?\n").lower()

            if CW_24 in check_yes:
                print("Late Submission\n")
                validReason = input("Is there a valid reason?\n").lower()

                if validReason in check_yes:
                    print("Mitigating Circumstances")
                    waiting()
                    vlAccepted = input("Is your reason accepted?\n").lower()

                    if vlAccepted in check_yes:
                        print(common_answers["full_mark"])
                        break
                    elif vlAccepted in check_no:
                        print("10 marks will be subtracted from your overall mark.")
                    else:
                        print(common_answers["error"])
                        q = input("If you want to stop programm please enter 'q'\n")
                        ask(q)
                        if q == "q":
                            break
                elif validReason in check_no:
                    print("10 marks will be subtracted from your overall mark. But not in case you got below 40!")
                else:
                    print(common_answers["error"])
                    q = input("If you want to stop programm please enter 'q'\n")
                    ask(q)
                    if q == "q":
                        break
            elif CW_24 in check_no:
                CW_5d = input("Did you submit your CW within 5 days after the deadline?\n").lower()

                if CW_5d in check_yes:
                    validReason = input("Is there a valid reason?\n").lower()

                    if validReason in check_yes:
                        print("MC(Mitigating Circumstances) (late submission option)")
                        waiting()
                        vlAccepted = input("Is your MC accepted?\n").lower()

                        if vlAccepted in check_yes:
                            print(common_answers["full_mark"])
                            break
                        elif vlAccepted in check_no:
                            print(common_answers["zero_mark"])
                            break
                        else:
                            print(common_answers["error"])
                            q = input("If you want to stop programm please enter 'q'\n")
                            ask(q)
                            if q == "q":
                                break

                    elif validReason in check_no:
                        print(common_answers["zero_mark"])
                        break
                    else:
                        print(common_answers["error"])
                        q = input("If you want to stop programm please enter 'q'\n")
                        ask(q)
                        if q == "q":
                            break
                elif CW_5d in check_no:
                    validReason = input("Is there a valid reason?\n").lower()

                    if validReason in check_yes:
                        print("MC(Mitigating Circumstances) (non-submission/deferral) before specified deadline")
                        waiting()
                        print("Your MC is accepted.\n" + "Your case will be delayed to Deferral reassessment.")
                    elif validReason in check_no:
                        print(common_answers["zero_mark"])
                        break
                    else:
                        print(common_answers["error"])
                        q = input("If you want to stop programm please enter 'q'\n")
                        ask(q)
                        if q == "q":
                            break

                else:
                    print(common_answers["error"])
                    q = input("If you want to stop programm please enter 'q'\n")
                    ask(q)
                    if q == "q":
                        break

            else:
                print(common_answers["error"])
                q = input("If you want to stop programm please enter 'q'\n")
                ask(q)
                if q == "q":
                    break

