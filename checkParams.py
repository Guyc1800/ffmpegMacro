import os
from globals import audio_ext


def check_parameters(options,args):
  '''
  takes options and args from main and format them to defaults values and exist if values are missing or invalid
  :param options: from main
  :param args: from main
  :return formated options and args
  '''
  if len(args) >= 1:
    options.basedir = args[0]
  if not options.target_dir:
    options.target_dir = options.basedir
  if not os.path.isdir(options.basedir):
    exit('basedir must be a directory')
  if options.target_ext not in audio_ext:
    exit(f'invalid extension, must be one of the supported types {audio_ext}')
  if not os.path.exists(options.target_dir):
    os.mkdir(options.target_dir)
  return options, args


