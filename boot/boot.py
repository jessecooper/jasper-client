#!/usr/bin/env python

import os
import json
import urllib2

import vocabcompiler

def say(phrase, OPTIONS = " -vdefault+m3 -p 40 -s 160 --stdout > ../static/audio/say.wav"):
    os.system("espeak " + json.dumps(phrase) + OPTIONS)
    os.system("aplay ../static/audio/say.wav")

def configure():
    try:
        urllib2.urlopen("http://www.google.com").getcode()

        print "CONNECTED TO INTERNET"
        print "COMPILING DICTIONARY"
        vocabcompiler.compile("../client/sentences.txt", "../client/dictionary.dic", "../client/languagemodel.lm")

        print "STARTING CLIENT PROGRAM"
        os.system("../client/start.sh &")

    except:

        print "COULD NOT CONNECT TO NETWORK"
        say("Hello, I could not connect to a network. Please read the documentation to configure your Raspberry Pi.")

if __name__ == "__main__":
    print "==========STARTING JASPER CLIENT=========="
    print "=========================================="
    print "COPYRIGHT 2013 SHUBHRO SAHA, CHARLIE MARSH"
    print "=========================================="
    say("Hello.... I am Jasper... Please wait one moment.")
    configure()
