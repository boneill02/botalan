import random
from subprocess import Popen, PIPE

from tweet import tweets

def cowsay(arg, msg):
    if arg == None:
        process = Popen(["cowsay", msg], stdout=PIPE)
    else:
        process = Popen(["cowsay", "-f", arg, msg], stdout=PIPE)

    (output, err) = process.communicate()
    exit_code = process.wait()
    return '```\n' + output.decode('utf-8') + '```\n'

def tweet():
    return random.choice(tweets)

def fortune(arg=None):
    if arg == None:
        process = Popen(["fortune"], stdout=PIPE)
    else:
        process = Popen(["fortune", arg], stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    return output.decode('utf-8')

def cowfortune(arg=None):
    if arg == None:
        p1 = Popen(["fortune"], stdout=PIPE)
    else:
        p1 = Popen(["fortune", arg], stdout=PIPE)

    p2 = Popen(["cowsay"], stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    (output, err) = p2.communicate()
    exit_code = p2.wait()
    return '```\n' + output.decode('utf-8') + '```\n'
