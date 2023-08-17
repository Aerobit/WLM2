#!usr/bin/env python3

# Word List Manipulator 2.0 (WLM2)
# Version 2.0 last edit 17-08-2023 14:00
# Build: 0001
# Trying to bring this great tool back from the dead.
# Re-written from bash to python and added new features.
# Still afew bugs and the Miscellaneous Fun menu is not functional yet.
# Credits to ;
# Gitsnik, Pureh@te, Members at unix.com
# Original Google code source: http://code.google.com/p/wordlist-manipulator/source/browse/wlm 
###################################################
# Defining Colors #
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"

###################################################
# Inporting the system name for the "clear()" function #
# import sleep to show output for some time period
import os
from os import system, name
from time import sleep
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

###################################################
# Main Menu #
def menu():
    print(end='\r' * 30)
    print(bright_cyan +"""
__    __ _     __  __
\ \/\/ /| |__ |  \/  |
 \_/\_/ |____||_|\/|_|   """+ white)
    print(bright_green + '\033[4m' + ' Wordlist Manipulator 2.0' + '\033[0m' + white)
    print()
    print('1.  Case options')
    print('2.  Combinations')
    print('3.  Prepend / Prefix')
    print('4.  Append / Suffix')
    print('5.  Inclusion Options')
    print('6.  Substitution Options')
    print('7.  Clean / Optimize wordlist')
    print('8.  Split files')
    print('9.  Removal / Deletion options')
    print('10. Miscellaneous Fun')
    print('f.  File information')
    print('h.  Version and listing of all functions')
    print('u.  Update')
    print()
    print('"Q" to quit')
    print('\n' * 2)


###################################################
# Case Menu #
def case_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Case Options' + '\033[0m' + white)
    print()
    print('1. Change case of first letter')
    print('2. Change case of last letter')
    print('3. Change all lower case to upper case')
    print('4. Change all upper case to lower case')
    print('5. Invert case (lower to upper, upper to lower')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Combination Menu #
def combo_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Combination Options' + '\033[0m' + white)
    print()
    print('1. Combine words from 1 list to each word in another list')
    print('2. Combine all wordlists in a directory to 1 wordlist')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Prepend / Prefix Menu #
def prefix_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Prefix Options' + '\033[0m' + white)
    print()
    print('1. Prefix numeric values in sequence to a wordlist (ie. 0 - 99999)')
    print('2. Prefix fixed number of numeric values in sequence to a wordlist (ie. 00000 - 99999)')
    print('3. Prefix word / characters to a wordlist')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Append / Suffix Menu #
def suffix_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Suffix Options' + '\033[0m' + white)
    print()
    print('1. Suffix numeric values in sequence to a wordlist (ie. 0 - 99999)')
    print('2. Suffix fixed number of numeric values in sequence to a wordlist (ie. 00000 - 99999)')
    print('3. Suffix word / characters to a wordlist')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Inclusion Menu #
def incl_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Inclusion Options' + '\033[0m' + white)
    print()
    print('1. Include characters/word in a defined position from the START of a word.')
    print('2. Include characters/word in a defined position from the END of a word.')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Substitution Menu #
def subs_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Substitution options' + '\033[0m' + white)
    print()
    print('1. Substitute/Replace characters from START of word.')
    print('2. Substitute/Replace characters from END of word.')
    print('3. Substitute/Replace characters at a certain position.')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Clean Menu #
def clean_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Substitution options' + '\033[0m' + white)
    print()
    print('1. Full optimization of wordlist.')
    print('2. Optimize wordlist for WPA.')
    print('3. Sort wordlist on length of words.')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Split Menu #
def split_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'File splitting options' + '\033[0m' + white)
    print()
    print('1. Split wordlists files by size.')
    print('2. Split wordlists into defined number of files.')
    print('3. Split wordlists by maximum linecount per file.')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Info Menu #
def info_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'File information options' + '\033[0m' + white)
    print()
    print('1. Line count and most counted word.')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Removal Menu #
def removal_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
    print()
    print('1. Remove X number of characters from start of word.')
    print('2. Remove X number of characters from end of word.')
    print('3. Remove specific characters globally from words.')
    print('4. Remove words containing specific characters.')
    print('5. Remove lines with X number of identical adjacent characters.')
    print('6. Remove lines existing in 1 list from another list.\n   (dont use on large lists, work in progress)')
    print('7. Remove words which do NOT have X number of numeric values.')
    print('8. Removing words which have X number of repeated characters.')
    print('9. Remove words of a certain length.')
    print('10.Remove characters from and including specified character.')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


###################################################
# Update Menu #
def update_menu():
    clear()
    print(end='\r' * 30)
    print('Wordlist Manipulator')
    print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
    print()
    print('1. Check for updates.')
    print('2. Update Word List Manipulator from Github.')
    print()
    print('"Q" to go back to the main menu')
    print('\n' * 2)


while True:
    clear()
    menu()
    choice = input('Choose from the above menu: ')
    if choice == '1':
        case_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Case Options' + '\033[0m' + white)
            print()
            case = input('Change first letter to lower case or upper case.\nChoose "u" or "l": ')
            file = input('Enter /path/to/wordlist you want to edit: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            if case == 'u':
                with open(file, errors='ignore') as fhand:
                    nhand = open(newfile, 'w', errors='ignore')
                    for lines in fhand:
                        words_s = lines.rstrip()
                        try:
                            words_c = words_s[0].upper() + words_s[1:]
                        except:
                            continue
                        nhand.write(words_c)
                        nhand.write('\n')
                        #print('Working..',end='\r')
                nhand.close()
            elif case == 'l':
                with open(file, 'r', errors='ignore') as fhand:
                    nhand = open(newfile, 'w', errors='ignore')
                    for lines in fhand:
                        words_s = lines.rstrip()
                        try:
                            words_c = words_s[0].lower() + words_s[1:]
                        except:
                            continue
                        nhand.write(words_c)
                        nhand.write('\n')
                        #print('Working..',end='\r')
                nhand.close()
            else:
                menu()
        if choice == '2':
                clear()
                print('Wordlist Manipulator')
                print(bright_cyan + '\033[4m' + 'Case Options' + '\033[0m' + white)
                print()
                case = input('Change last letter to lower case or upper case.\nChoose "u" or "l": ')
                file = input('Enter /path/to/wordlist you want to edit: ')
                newfile = input('Enter /path/to/wordlist you want to create: ')
                if case == 'u':
                    with open(file, errors='ignore') as fhand:
                        nhand = open(newfile, 'w', errors='ignore')
                        for lines in fhand:
                            words_s = lines.rstrip()
                            try:
                                words_c = words_s[:-1] + words_s[-1].upper()
                            except:
                                continue
                            nhand.write(words_c)
                            nhand.write('\n')
                            #print('Working..',end='\r')
                    nhand.close()
                elif case == 'l':
                    with open(file, 'r', errors='ignore') as fhand:
                        nhand = open(newfile, 'w', errors='ignore')
                        for lines in fhand:
                            words_s = lines.rstrip()
                            try:
                                words_c = words_s[:-1] + words_s[-1:].lower()
                            except:
                                continue
                            nhand.write(words_c)
                            nhand.write('\n')
                            #print('Working..',end='\r')
                    nhand.close()
        if choice == '3':
                clear()
                print('Wordlist Manipulator')
                print(bright_cyan + '\033[4m' + 'Case Options' + '\033[0m' + white)
                print()
                print('Change all letters to uppercase')
                file = input('Enter /path/to/wordlist you want to edit: ')
                newfile = input('Enter /path/to/wordlist you want to create: ')
                with open(file, errors='ignore') as fhand:
                    nhand = open(newfile, 'w', errors='ignore')
                    for lines in fhand:
                        words_s = lines.rstrip()
                        try:
                            words_c = words_s.upper()
                        except:
                            continue
                        nhand.write(words_c)
                        nhand.write('\n')
                        #print('Working..',end='\r')
                nhand.close()
        if choice == '4':
                clear()
                print('Wordlist Manipulator')
                print(bright_cyan + '\033[4m' + 'Case Options' + '\033[0m' + white)
                print()
                print('Change all letters to lowercase')
                file = input('Enter /path/to/wordlist you want to edit: ')
                newfile = input('Enter /path/to/wordlist you want to create: ')
                with open(file, errors='ignore') as fhand:
                    nhand = open(newfile, 'w', errors='ignore')
                    for lines in fhand:
                        words_s = lines.rstrip()
                        try:
                            words_c = words_s.lower()
                        except:
                            continue
                        nhand.write(words_c)
                        nhand.write('\n')
                        #print('Working..',end='\r')
                nhand.close()
        if choice == '5':
                clear()
                print('Wordlist Manipulator')
                print(bright_cyan + '\033[4m' + 'Case Options' + '\033[0m' + white)
                print()
                print('Invert case (lower to upper, upper to lower')
                file = input('Enter /path/to/wordlist you want to edit: ')
                newfile = input('Enter /path/to/wordlist you want to create: ')
                with open(file, errors='ignore') as fhand:
                    nhand = open(newfile, 'w', errors='ignore')
                    for lines in fhand:
                        words_s = lines.rstrip()
                        try:
                            words_c = words_s.swapcase()
                        except:
                            continue
                        nhand.write(words_c)
                        nhand.write('\n')
                        #print('Working..',end='\r')
                nhand.close()
        if choice == "q":
            menu()
    elif choice == '2':
        combo_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Combination Options' + '\033[0m' + white)
            print()
            print('Combine each line from one list to each each line in another list')
            file = input('Enter /path/to/wordlist to the wordlist you want to append: ')
            file2 = input('Enter /path/to/wordlist to the second wordlist you want to combine: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            nhand = open(newfile, 'w', errors='ignore')
            count = 0
            with open(file, 'r', errors='ignore') as fhand:
                readfile = fhand.readlines()
            with open(file2, 'r', errors='ignore') as f1hand:
                readfile1 = f1hand.readlines()
            for lines in readfile:
                try:
                    combined = readfile[count].rstrip() + readfile1[count].lstrip()
                except:
                    continue
                count = count + 1
                nhand.write(combined)
            nhand.close()
        if choice == '2':
            clear()
            import glob
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Combination Options' + '\033[0m' + white)
            print()
            print('Combine all wordlists in a directory into one wordlist')
            path = input('Enter /path/to/directory where the wordlists are stored: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            clear()
            nhand = open(newfile, 'a', errors='ignore')
            for file in glob.glob(path + '\*.*'):
                print(file)
            print()
            print('! Note that ALL files in directory will be combined. Do you want to continue?')
            choice = input('"Y" to continue or "Q" to go back.')
            if choice == 'y':
                for file in glob.glob(path + '\*.*'):
                    with open(file, 'r', errors='ignore') as infile:
                        for lines in infile:
                            nhand.write(lines)
                nhand.close()
            else:
                continue
    elif choice == '3':
        prefix_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Prefix Options' + '\033[0m' + white)
            print()
            print('Prefix numeric values in sequence to a wordlist (ie. 0 - 99999)')
            file = input('Enter /path/to/wordlist to prefix numbers to: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            prefix = int(input('Enter how many numeric values you want to Prefix (max 5): '))
            if prefix in range(1,6):
                if prefix == 1:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10):
                                    combined = str(count) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 2:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100):
                                    combined = str(count) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 3:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,1000):
                                    combined = str(count) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 4:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10000):
                                    combined = str(count) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 5:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100000):
                                    combined = str(count) + lines
                                    nhand.write(combined)
                                    count = count + 1
        if choice == '2':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Prefix Options' + '\033[0m' + white)
            print()
            print('Prefix fixed number of numeric values in sequence to a wordlist (ie. 00000 - 99999)')
            file = input('Enter /path/to/wordlist to prefix numbers to: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            prefix = int(input('Enter how many numeric values you want to Prefix (max 5): '))
            if prefix in range(1,6):
                if prefix == 1:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10):
                                    combined = str(count) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 2:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100):
                                    combined = str(count).zfill(prefix) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 3:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,1000):
                                    combined = str(count).zfill(prefix) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 4:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10000):
                                    combined = str(count).zfill(prefix) + lines
                                    nhand.write(combined)
                                    count = count + 1
                elif prefix == 5:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100000):
                                    combined = str(count).zfill(prefix) + lines
                                    nhand.write(combined)
                                    count = count + 1
        if choice == '3':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Prefix Options' + '\033[0m' + white)
            print()
            print('Prefix word / characters to a wordlist')
            file = input('Enter /path/to/wordlist to prefix numbers to: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            prefix = str(input('Enter word/characters you want prefixed: '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    for lines in fhand:
                        combined = prefix + lines
                        nhand.write(combined)
    elif choice == '4':
        suffix_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Suffix Options' + '\033[0m' + white)
            print()
            print('Suffix numeric values in sequence to a wordlist (ie. 0 - 99999)')
            file = input('Enter /path/to/wordlist to suffix numbers to: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            suffix = int(input('Enter how many numeric values you want to Suffix (max 5): '))
            if suffix in range(1,6):
                if suffix == 1:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10):
                                    combined = (lines.rstrip() + str(count))
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 2:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100):
                                    combined = (lines.rstrip() + str(count))
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 3:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,1000):
                                    combined = (lines.rstrip() + str(count))
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 4:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10000):
                                    combined = (lines.rstrip() + str(count))
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 5:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100000):
                                    combined = (lines.rstrip() + str(count))
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
        if choice == '2':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Suffix Options' + '\033[0m' + white)
            print()
            print('Suffix fixed number of numeric values in sequence to a wordlist (ie. 00000 - 99999)')
            file = input('Enter /path/to/wordlist to suffix numbers to: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            suffix = int(input('Enter how many numeric values you want to Suffix (max 5): '))
            if suffix in range(1,6):
                if suffix == 1:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10):
                                    combined = lines.rstrip() + str(count)
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 2:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100):
                                    combined = lines.rstrip() + str(count).zfill(suffix)
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 3:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,1000):
                                    combined = lines.rstrip() + str(count).zfill(suffix)
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 4:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,10000):
                                    combined = lines.rstrip() + str(count).zfill(suffix)
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
                elif suffix == 5:
                    with open(file, 'r', errors='ignore') as fhand:
                        with open(newfile, 'w', errors='ignore') as nhand:
                            for lines in fhand:
                                count = 0
                                for digit in range(0,100000):
                                    combined = lines.rstrip() + str(count).zfill(suffix)
                                    nhand.write(combined)
                                    nhand.write('\n')
                                    count = count + 1
        if choice == '3':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Suffix Options' + '\033[0m' + white)
            print()
            print('Suffix word / characters to a wordlist')
            file = input('Enter /path/to/wordlist to suffix numbers to: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            prefix = str(input('Enter word/characters you want suffixed: '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    for lines in fhand:
                        combined = lines.rstrip() + prefix
                        nhand.write(combined)
                        nhand.write('\n')
    elif choice == '5':
        incl_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Inclusion Options' + '\033[0m' + white)
            print()
            print('Include characters/word in a defined position from the START of a word.')
            file = input('Enter /path/to/wordlist you want to edit: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            word = input('Enter the characters/word you want included in each word: ')
            pos = int(input('Enter at what position to start from (after how many characters): '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    for lines in fhand:
                        combined = lines[:pos] + word + lines[pos:]
                        nhand.write(combined)
        if choice == '2':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Inclusion Options' + '\033[0m' + white)
            print()
            print('Include characters/word in a defined position from the END of a word.')
            file = input('Enter /path/to/wordlist you want to edit: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            word = input('Enter the characters/word you want included in each word: ')
            pos = int(input('Enter at what position to start from the END of the word (after how many characters from the END): '))
            neg = -abs(pos) - 1
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    for lines in fhand:
                        combined = word + lines[neg:]
                        finished = lines[:neg] + combined
                        nhand.write(finished)
    elif choice == '6':
        subs_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Substitution options' + '\033[0m' + white)
            print()
            print('Substitute/Replace characters from the START of word.')
            file = input('Enter /path/to/wordlist you want to edit: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            word = input('Enter the characters/word you want to use as a substitution: ')
            pos = int(input('Enter at what position to start from (after how many characters): '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    for lines in fhand:
                        combined = word + lines[pos:]
                        nhand.write(combined)
        if choice == '2':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Substitution options' + '\033[0m' + white)
            print()
            print('Substitute/Replace characters from the END of a word.')
            file = input('Enter /path/to/wordlist you want to edit: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            word = input('Enter the characters/word you want to use as a substitution: ')
            pos = int(input('Enter at what position to start from (after how many characters): '))
            neg = -abs(pos) - 1
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    for lines in fhand:
                        combined = lines[:neg] + word
                        nhand.write(combined)
                        nhand.write('\n')
        if choice == '3':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Substitution options' + '\033[0m' + white)
            print()
            print('Substitute/Replace characters at a certain position.')
            file = input('Enter /path/to/wordlist you want to edit: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            word = input('Enter the characters/word you want to use as a substitution: ')
            pos1 = int(input('Enter the start position of characters you want to replace: '))
            pos1 = pos1 - 1
            pos2 = int(input('Enter the stop position of characters you want to replace: '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    for lines in fhand:
                        finished = lines[:pos1] + word + lines[pos2:]
                        nhand.write(finished)
    elif choice == '7':
        clean_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Optimization options' + '\033[0m' + white)
            print()
            print('Full optimization of wordlist.')
            file = input('Enter /path/to/wordlist you want to optimize: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            min_length = int(input('Enter the minimum amount of characters per line: ')) + 1
            max_length = int(input('Enter the maximum amount of characters per line: ')) + 1
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    lines_seen = set()
                    count = 0
                    count2 = 0
                    most_counts = dict()
                    for line in fhand:
                        count += 1
                        if line not in lines_seen:
                            if line.startswith('#'):
                                continue
                            line = line.encode('ascii', 'ignore').decode().lstrip()
                            if min_length <= len(line) <= max_length:
                                nhand.write(line)
                                lines_seen.add(line)
                                count2 += 1
                                most_counts[line] = most_counts.get(line, 0) + 1
                    bigcount = None
                    bigword = None
                    if most_counts:
                        bigword, bigcount = max(most_counts.items(), key=lambda x: x[1])
                        bigword = bigword.rstrip()
            with open(newfile, 'r') as nhand:
                infile = nhand.readlines()
            sorted_file = sorted(infile, key=len)
            with open(newfile, 'w') as nhand:
                nhand.writelines(sorted_file)
            total = count - count2
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Results' + '\033[0m' + white)
            print()
            print('Removed all duplicate lines from the file..')
            print('Deleted words which did not meet length requirement..')
            print('Removed all non-ascii characters..')
            print('Removed all comments..')
            print('Removed any leading white spaces, tabs, and CRLF from the file..')
            print('Sorted file according to length')
            print('\n' * 2)
            print('First file total lines :', '{:,}'.format(count))
            print('New file total lines   :', '{:,}'.format(count2))
            print('Total lines removed    :', '{:,}'.format(total))
            print()
            if bigword and bigcount:
                print('Word counted the most  :', bigword)
                print('Total times counted    :', '{:,}'.format(bigcount))
            else:
                print('No words found in the file.')
            print('\n' * 2)
            input('Press Enter to Continue: ')
        if choice == '2':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Optimization options' + '\033[0m' + white)
            print()
            print('Optimization of wordlist for WPA/WPA2')
            file = input('Enter /path/to/wordlist you want to optimize: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    lines_seen = set()
                    count = 0
                    count2 = 0
                    most_counts = dict()
                    for line in fhand:
                        count += 1
                        if line not in lines_seen:
                            if line.startswith('#'):
                                continue
                            line = line.encode('ascii', 'ignore').decode().lstrip()
                            if len(line) >= 9 and len(line) <= 64:
                                nhand.write(line)
                                lines_seen.add(line)
                                count2 += 1
                                most_counts[line] = most_counts.get(line, 0) + 1
                    bigcount = None
                    bigword = None
                    if most_counts:
                        bigword, bigcount = max(most_counts.items(), key=lambda x: x[1])
                        bigword = bigword.rstrip()
            with open(newfile, 'r') as nhand:
                infile = nhand.readlines()
            sorted_file = sorted(infile, key=len)
            with open(newfile, 'w') as nhand:
                nhand.writelines(sorted_file)
            total = count - count2
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Results' + '\033[0m' + white)
            print()
            print('Removed all lines less than 8 or greater than 63 characters')
            print('Removed all duplicate lines from the file..')
            print('Removed all non-ascii characters..')
            print('Removed all comments..')
            print('Removed any leading white spaces, tabs, and CRLF from the file..')
            print('Sorted file according to length')
            print('\n' * 2)
            print('First file total lines :', '{:,}'.format(count))
            print('New file total lines   :', '{:,}'.format(count2))
            print('Total lines removed    :', '{:,}'.format(total))
            print()
            if bigword and bigcount:
                print('Word counted the most  :', bigword)
                print('Total times counted    :', '{:,}'.format(bigcount))
            else:
                print('No words found in the file.')
            print('\n' * 2)
            input('Press Enter to Continue: ')
        if choice == '3':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Optimization options' + '\033[0m' + white)
            print()
            print('Sort wordlist based on word size/length')
            file = input('Enter /path/to/wordlist you want to sort: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w', errors='ignore') as nhand:
                    infile = fhand.readlines()
                    sorted_file = sorted(infile, key=len)
                    nhand.writelines(sorted_file)
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Results' + '\033[0m' + white)
            print()
            print('Sorted file according to length')
            print('\n' * 2)
            input('Press Enter to Continue: ')
    elif choice == '8':
        split_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'File splitting options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist you want to split: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            size = int(input('Enter the size of the files to create in MB: '))
            chunk_size = (size * 950000)
            file_number = 1
            with open('rockyou.txt' ,'r' ,errors='ignore') as fhand:
                chunk = fhand.read(chunk_size)
                while chunk:
                    small_filename = newfile + '_{}.txt'.format(str(file_number).zfill(2))
                    with open(small_filename, 'w') as chunk_file:
                        chunk_file.write(chunk)
                    file_number += 1
                    chunk = fhand.read(chunk_size)
        if choice == '2':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'File splitting options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist you want to split: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            total_files = int(input('Enter number files to create: '))
            emptyfile = None
            file_number = 1
            with open(file, 'r', errors='ignore') as fhand:
                lines_per_file = round(len(fhand.readlines()) + total_files - 1) // total_files
            with open(file, 'r', errors='ignore') as fhand:
                for linenum, line in enumerate(fhand):
                    if linenum % lines_per_file == 0:
                        if emptyfile:
                            emptyfile.close()
                        small_filename = newfile + '_{}.txt'.format(str(file_number).zfill(2))
                        emptyfile = open(small_filename, "w")
                        file_number += 1
                    emptyfile.write(line)
                if emptyfile:
                    emptyfile.close()
        if choice == '3':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'File splitting options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist you want to split: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            lines_per_file = int(input('Enter number of lines per file: '))
            emptyfile = None
            file_number = 1
            with open(file, 'r', errors='ignore') as fhand:
                for linenum, line in enumerate(fhand):
                    if linenum % lines_per_file == 0:
                        if emptyfile:
                            emptyfile.close()
                        small_filename = newfile + '_{}.txt'.format(str(file_number).zfill(2))
                        emptyfile = open(small_filename, "w")
                        file_number += 1
                    emptyfile.write(line)
                if emptyfile:
                    emptyfile.close()
    elif choice == '9':
        removal_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist to remove characters from: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            pos = int(input('Enter how many characters to remove from start of word:'))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w') as nhand:
                    for lines in fhand:
                        lines = lines[pos:]
                        nhand.write(lines)
        if choice == '2':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist to remove characters from: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            pos = int(input('Enter how many characters to remove from end of word:'))
            neg = -abs(pos) - 1
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w',) as nhand:
                    for lines in fhand:
                        lines = lines[:neg]
                        nhand.write(lines)
                        nhand.write('\n')
        if choice == '3':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist to remove characters from: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            char = str(input('Enter the characters to remove from the file: '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w',) as nhand:
                    for lines in fhand:
                        lines = lines.rstrip().replace(char,'')
                        nhand.write(lines)
                        nhand.write('\n')
        if choice == '4':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist to remove words containing specific characters: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            char = str(input('Enter the character to check for: '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w',) as nhand:
                    for lines in fhand:
                        if char in lines:
                            continue
                        nhand.writelines(lines)
        if choice == '5':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist to remove lines with X number of identical adjacent characters: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            char_to_check = str(input('Enter the character to check for: '))
            X = int(input('Enter the number of identical adjacent characters to check for: '))
            with open(file, 'r', errors='ignore') as fhand:
                with open(newfile, 'w') as nhand:
                    lines = fhand.readlines()
                    for line in lines:
                        adjacent_chars = 0
                        for i in range(1, len(line)):
                            if line[i] == line[i-1] == char_to_check:
                                adjacent_chars += 1
                            else:
                                adjacent_chars = 0
                            if adjacent_chars == X - 1:
                                break
                        if adjacent_chars < X - 1:
                            nhand.write(line)
        if choice == '6':
            clear()
            print(end='\r' * 30)
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Removal options' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist to remove lines from: ')
            file2 = input('Enter /path/to/wordlist with the lines to remove: ')
            newfile = input('Enter /path/to/wordlist you want to create: ')
            with open(file, 'r', errors='ignore') as fhand:
                with open(file2, 'r', errors='ignore') as f2hand:
                    with open(newfile, 'w') as nhand:
                        original_lines = set(fhand.readlines())
                        lines_to_remove = set(f2hand.readlines())
                        remaining_lines = original_lines - lines_to_remove
                        nhand.writelines(remaining_lines)
    elif choice == 'f':
        info_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'File information options.' + '\033[0m' + white)
            print()
            file = input('Enter /path/to/wordlist you want to inspect: ')
            counts = dict()
            line_count = 0
            shortest_line = None
            longest_line = None
            shortest_word = None
            longest_word = None
            first_line = None
            last_line = None
            with open(file, 'r', errors='ignore') as fhand:
                for line in fhand:
                    if first_line is None:
                        first_line = line
                    last_line = line
                    words = line.split()
                    line_count += 1
                    for word in words:
                        counts[word] = counts.get(word, 0) + 1
                        if shortest_word is None or len(word) < len(shortest_word):
                            shortest_word = word
                        if longest_word is None or len(word) > len(longest_word):
                            longest_word = word
                    if shortest_line is None or len(line) < len(shortest_line):
                        shortest_line = line
                    if longest_line is None or len(line) > len(longest_line):
                        longest_line = line
            bigword, bigcount = max(counts.items(), key=lambda x: x[1])
            print('\n' * 2)
            print('Total lines          :', '{:,}'.format(line_count))
            print('Word counted most    :', bigword)
            print('Word was counted     :', '{:,}'.format(bigcount), 'times')
            print('File size (bytes)    :', '{:,}'.format(os.path.getsize(file)))
            print('File size (KB)       :', '{:,.2f}'.format(os.path.getsize(file) / 1024))
            print('File size (MB)       :', '{:,.2f}'.format(os.path.getsize(file) / (1024 ** 2)))
            print('Unique words         :', '{:,}'.format(len(counts)))
            print('Shortest line        :', shortest_line.strip())
            print('Longest line         :', longest_line.strip())
            print('Shortest word        :', shortest_word)
            print('Longest word         :', longest_word)
            print('First line           :', first_line.strip())
            print('Last line            :', last_line.strip())
            print()
            input('Press enter to continue.')
    elif choice == 'u':
        update_menu()
        choice = input('Choose from the above menu: ')
        if choice == '1':
            clear()
            print('Wordlist Manipulator')
            print(bright_cyan + '\033[4m' + 'Update options' + '\033[0m' + white)
            print()
            github_url = "https://raw.githubusercontent.com/Aerobit/WLM2/main/WLM2.py"
            os.system(f"curl -o WLM2.py {github_url}")
            print("Script updated successfully.")
            input('Press enter to continue.')
    elif choice == 'q':
        clear()
        quit('Thank you for using WLM 2.0\nGood Bye')
################################################################################
