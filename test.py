
import os

from datetime import datetime, timedelta



tar_command_formatter = '''tar -cf {output_file} {input_file}'''
untar = ''' tar -xf {input_file} -C {output_location}'''

def zip_files():
    cmd = tar_command_formatter.format(input_file='source_dir/AB_NYC_2019.csv', output_file='source_dir/AB_NYC_2019.tar')
    os.system(cmd)


def move_files():
    os.system('mv source_dir/AB_NYC_2019.tar target_dir/AB_NYC_2019.tar')


def unzip_files():
    cmd = untar.format(input_file='target_dir/AB_NYC_2019.tar', output_location='target_dir/')
    os.system(cmd)


zip_files()
move_files()
unzip_files()

