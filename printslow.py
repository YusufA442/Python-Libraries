import sys,time

def printslow(string):
    for carrier in string:
        sys.stdout.write(carrier)
        time.sleep(0.01)
    sys.stdout.write("\n")