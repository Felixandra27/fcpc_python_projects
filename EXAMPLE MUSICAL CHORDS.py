#FELIXANDRA ANDAL
#BS-IT
#CREDITS TO https://jonthysell.com/2013/06/04/transposing-chord-progressions-with-python/
#MUSICAL TRANSPOSITION PROGRAM

import sys
import string
flats = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]
sharps = ["G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"]
preferFlats = True
input_chords = input('Input chords: ')
input_step = int(input('Input step: '))
user_chords = [word for word in input_chords.split()]
print(user_chords)
new = ''
for chord in user_chords:
    if chord in flats:
        index = flats.index(chord)
        if index + input_step >= len(flats):
            x = (index + input_step) - len(flats)
            new += flats[x]
        else:
            new += flats[index+input_step]
def transposeChords(chords, index):
    global _flats, _sharps, _preferFlats
    newChords = []
    notes = _flats if _preferFlats else _sharps
    for chord in chords:
        noteParts = (chord[:1], chord[1:])
        if (chord.find("b") == 1 or chord.find("#") == 1):
            noteParts = (chord[:2], chord[2:])
        oldNoteIndex = -1
        if (noteParts[0] in _flats):
            oldNoteIndex = _flats.index(noteParts[0])
        elif (noteParts[0] in _sharps):
            oldNoteIndex = _sharps.index(noteParts[0])
        if (oldNoteIndex == -1):  # Not a note
            newChords.append("".join(noteParts))
        else:
            newNote = notes[(oldNoteIndex + index) % len(notes)]
            newChords.append("".join([newNote, noteParts[1]]))
    return newChords
def main(args):
    """Take a progression of chords and print them out transposed."""
    if (len(args) == 0):
        print
        "tChords.py [list of chords seperated by spaces]"
        print
        "ex:"
        print
        "tChords.py C C7 F Fm C G7 C"
    else:
        for i in range(0, len(_flats)):
            newChords = transposeChords(args, i)
            print
            " ".join(newChords)
if __name__ == "__main__":
    main(sys.argv[1:])
print(new)