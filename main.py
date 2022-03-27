from optparse import OptionParser
from checkParams import check_parameters
from convert import convert


# this script enable to convert whole folder of audio/video files into another format from this list('.mp3','.aac','.dsf','.m4a','.flac','.wav','.wma')
# the program search in given folder for files that can be converted and convert them using ffmpeg tool,
# to use the program run the main.py in the cmd or other consoles and pass the parameters
# you can see explanation of the available parameters using command  "python.exe main.py -h".
# example of using the program :
# python.exe main.py --input="C:\\Users\\guyc1\\Desktop\\aaa" -extension=".aac" -t "C:\\Users\\guyc1\\Desktop\\bbb" -o -f "lowpass=24000, volume=8dB"


if __name__ == '__main__':
    parser = OptionParser(description='convert any audio/video file to audio file with desired extension.')
    parser.add_option('-i','--input',action='store',dest="basedir",help='path of the base directory to search and convert files from',metavar='DIR')
    parser.add_option('-e','--extension',action='store',dest="target_ext",help='desired file type to convert to',type='string',default='.mp3')
    parser.add_option('-t','--targetDir',action='store',dest="target_dir",metavar='DIR',help='optional, target directory to store the converted files')
    parser.add_option('-o','--overwrite',action='store_true',dest="overwrite",help='flag overwrite existing files',default=False)
    parser.add_option('-f','--filters',action='store',dest="audio_filters",help='set audio filters',default="lowpass=24000, volume=6dB")
    (options,args) = parser.parse_args()
    (options,args) = check_parameters(options=options, args=args)
    convert(options=options)




