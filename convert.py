import os
from globals import audio_ext,video_ext


def convert(options):
  '''
  this function search for the matching files in the folders and convert them into the desired type according to the options recived
  :param options: options for the function from the optparse after formating
  '''
  input_files = []
  for (root, dirs, files) in os.walk(options.basedir, topdown=True):
    for file in files:
      if file.endswith(audio_ext+video_ext) and not file.endswith(options.target_ext):
        input_files.append(os.path.join(root,file))
  print(input_files)
  for file in input_files:
    print(f'ffmpeg -i "{file}" -af "{options.audio_filters}" {"-y" if options.overwrite else ""} -ar 44100 "{os.path.join(options.target_dir,os.path.splitext(os.path.basename(file))[0]+options.target_ext)}"')
    os.system(f'ffmpeg -i "{file}" -af "{options.audio_filters}" {"-y" if options.overwrite else ""} -ar 44100 "{os.path.join(options.target_dir,os.path.splitext(os.path.basename(file))[0]+options.target_ext)}"')



