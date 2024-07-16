emoticon="(v.v)"


def main():
    #it is accesiable to us but it was not modifiable now it is
    global emoticon
    say("Is anyone there")
    emoticon=":D"
    say("Ohhh Hi!")


def say(phrase):

    print(phrase+" "+ emoticon)
    #emoticon is accesiable by all the functions






main()
