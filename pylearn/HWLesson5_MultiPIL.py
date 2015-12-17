# coding=utf-8

from os import walk
import argparse
import Image
import re

parser = argparse.ArgumentParser()
'''
--path '/home/padznich/projects/pict/'
--ext gif jpg png
'''
parser.add_argument("--path", type=str, required=True, help="Enter folder path for pictures resizing.")
parser.add_argument("--ext", default='*', nargs='*',
                    help="Enter pictures extensions. As default value all pictures will be resized.")
args = parser.parse_args()

picts_folder = r'{}'.format(args.path)

pattern = (''.join('|(.*.{})'.format(e) for e in args.ext))[1:]


dir_content = []
for df in walk(picts_folder):
    dir_content.append(df)

path_to_picts = dir_content[0][0]
dir_root_files = dir_content[0][2]

for files in dir_root_files:
     if re.match(r'{}'.format(pattern), files, re.IGNORECASE):
         try:
             img = Image.open(path_to_picts + files)
             img_size = img.size
             img2x = img.resize((int(img_size[0] / 2.0), int(img_size[1] / 2.0)))
             img2x.save(r'{}resized_{}'.format(path_to_picts, files))
         except Exception as  e:
             with open('{}NotPict.log'.format(path_to_picts), 'a+') as file:
                 file.write('{}\n'.format(e))