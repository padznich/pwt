import argparse
import struct

parser = argparse.ArgumentParser()
parser.add_argument('--i', type=str,required=True)
parser.add_argument('--o', type=str,required=True)
args = parser.parse_args()

si = args.i
so = args.o
#si = C:\\home\\Lesson4\\pict.bmp
#so = C:\\home\\Lesson4\\pictCorrected.bmp

with open(si, 'rb+') as file:
    fr = file.read()
    header = struct.unpack("<ccihhi", fr[:14])
    info = struct.unpack("<iiihhiiiiii", fr[14:54])

    frmod = fr[:54] + (len(fr) - 54)*'\x00' # black
    #frmod = fr[:54] + (len(fr) - 54)*'\xff' # white

    with open(so, 'wb') as modfile:
        modfile.write(frmod)

    print(header)
    print(info)