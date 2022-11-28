import sys
import configparser

from generator.llvm_generator import generate

if __name__ == '__main__':
    config_path = './config.ini'
    print('Load config file from config.ini')

    # Read config.ini
    conf = configparser.ConfigParser()
    conf.read(config_path, encoding='utf-8')

    sections = conf.sections()

    # LLVM Configuration
    triple = conf.get('llvm', 'triple')
    data_layout = conf.get('llvm', 'data_layout')

    if len(sys.argv) < 2:
        print('Hint: usage \'python main.py xxx.m\'')
        print('Please input maverick file path: ')
        input_filename = input()
    else:
        input_filename = sys.argv[1]
    if not input_filename.endswith('.m'):
        print('Maverick source file should end with .m\n')
        exit(-1)
    output_filename = input_filename[0:len(input_filename) - 2] + ".ll"
    print('Source Maverick code file: ' + input_filename)
    print('Compiled llvm file: ' + output_filename)
    generate(input_filename, output_filename, triple, data_layout)