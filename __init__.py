#!/usr/bin/env python3
#
#
#   Windlib (Useful Functions Library)
#
#
#   Oh, I wrote this library just to facilitate my writing of some private scripts.
#   Don't be angry because my "Chinglish" ...
#
#   Version 1.2.2 (2021/4/10)
#
#   Copyright (C) 2021 SNWCreations. All rights reserved.
#
#
#   Functions:
#       typeof (added in v1.1.0)
#       check_os
#       unzip
#       get_file
#       get_large_file
#       find_file_on_all_partitions
#       get_os_partition
#       file_exists (added in v1.1.0)
#       find_files_with_the_specified_extension (added in v1.1.0, changed in v1.2.1)
#       get_file_with_progress (added in v1.1.0)
#       find_str_in_file (added in v1.2.0)
#
#

name = 'windlib'

#The library description...

"""
Windlib by SNWCreations

If you will use this library, I suggest importing the functions in this library through the "from" statement.

A useful function library for me!

I'm so lazy...

(C) 2021 SNWCreations. All rights reserved.
"""


print('Windlib by SNWCreations')
print('(C) 2021 SNWCreations. All rights reserved.')


#import libraries for functions
import os
import sys
import zipfile
import platform
import urllib
import requests
from pathlib import Path
from clint.textui import progress

#some variables for functions.
disklst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
found_letters = []



def typeof(variate):
    """
    Detect the type of a variable.
    """
    var_type=None
    if isinstance(variate,int):
        var_type = 'int'
    elif isinstance(variate,str):
        var_type = 'str'
    elif isinstance(variate,float):
        var_type = 'float'
    elif isinstance(variate,list):
        var_type = 'list'
    elif isinstance(variate,tuple):
        var_type = 'tuple'
    elif isinstance(variate,dict):
        var_type = 'dict'
    elif isinstance(variate,set):
        var_type = 'set'
    return var_type



def check_os(wantedOSName, slient=True, auto_exit=False):
    """
    Through the "platform" module, the system label (the first parameter) provided in the call parameter is compared with the current system label.

    The function "platform.system()" may return a string, which is a system label that can be used for comparison.

    If your python works support multiple systems, then you can combine the supported system types into a list, and then call this function.

    For example, if a work supports Windows, Mac OS, Jython (Python in Java Virtual Machine) and Linux, then the labels of these three systems can be defined as support_list: ['win32','darwin','linux','Java']

    Then, call it through the following method:

    check_os(support_list)

    * Default parameters:

    * slient - executes without generating any information.

    The default value is True. The valid values are True or False.

    * auto_exit - If the obtained system type is not what you want, it will decide whether to terminate the process according to this variable.
    
    If the process is terminated, an error value of "1" will be returned.

    The default value is False. The valid values are True or False.
    """

    wantedOSNameType = typeof(wantedOSName)
    if wantedOSNameType == 'list':
        if 'Java' in wantedOSName:
            if not platform.system() == 'Java':
                if not slient == True:
                    print('Not the desired operating system.')
                if not auto_exit == False:
                    sys.exit(1)
            else:
                if not slient == True:
                    print('It\'s desired opearting system.')
        #Oh! The f**king pylint!!!!!
        if not sys.platform() in wantedOSName:
            if not slient == True:
                print('Not the desired operating system.')
            if not auto_exit == False:
                sys.exit(1)
        else:
            if not slient == True:
                print('It\'s desired opearting system.')
    elif wantedOSNameType == 'str':
        if wantedOSName == 'Java':
            if not platform.system() == wantedOSName:
                if not slient == True:
                    print('Not the desired operating system.')
                if not auto_exit == False:
                    sys.exit(1)
            else:
                if not slient == True:
                    print('It\'s desired opearting system.')
        elif not platform.system() == wantedOSName:
            if not slient == True:
                print('Not the desired operating system.')
            if not auto_exit == False:
                sys.exit(1)
        else:
            if not slient == True:
                print('It\'s desired opearting system.')
            



def os_info(slient=True):
    """
    Get detailed information about the system, excluding information about computer accessories.

    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """

    if not slient == True:
        print('Getting operating system version...')
    if sys.platform == 'win32':
        os_version_tmp = platform.platform()
        os_vers = os_version_tmp.split('-')
        os_edition = str(platform.win32_edition())
        os_arch = platform.architecture()
        os_version = 'Microsoft' + os_vers[0] + ' ' + os_vers[1] + ' ' + os_edition + ' ' + os_vers[2] + ' ' + os_arch[0]
    elif sys.platform == 'darwin':
        os_version_tmp = platform.platform()
        os_version = os_version_tmp.replace('-', ' ')
    elif sys.platform == 'linux':
        os_version_tmp = platform.platform()
        os_version = os_version_tmp.replace('-', ' ')
    elif platform.system() == 'Java':
        os_version = 'Java virtual machine (you may be using Jython to call this function)'
    else:
        if not slient == True:
            print('Encountered a return value that could not be processed.')
    if not slient == True:
        print(os_version)



def unzip(filename):
    """unzip zip file"""

    zip_file = zipfile.ZipFile(filename)
    if os.path.isdir(filename + "_files"):
        pass
    else:
        os.mkdir(filename + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,filename + "_files/")
    zip_file.close()



def get_file(url, save_path='.', slient=True):
    """
    Download a file from the Internet.

    But please note that the target file cannot be too large, otherwise there will be no response for a long time.

    If you want to download a large file, please use the "get_large_file" function.

    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """
    filename = os.path.basename(url)
    save_name = save_path + '/' + filename
    if not slient == True:
        print('Downloading', save_name)
    file = urllib.request.urlopen(url)
    data = file.read()
    with open(save_name, "wb") as f:
        f.write(data)



def get_file_with_progress(url):
    """
    Download a file from the Internet.

    You can display progress while downloading.
    """
    res = requests.get(url, stream=True)
    total_length = int(res.headers.get('content-length'))
    filename = os.path.basename(url)
    with open(filename, "wb") as pypkg:
        for chunk in progress.bar(res.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1, width=100):
            if chunk:
                pypkg.write(chunk)



def get_large_file(url, save_path='.', slient=True):
    """
    This function is specifically for downloading large files.

    Filename refers to the local name of the file you want to save.

    For example, If you want to download "www.example.net/example.zip", then the local name should be "example.zip".

    Of course, the filename may not be consistent with the filename provided by the url.

    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """

    filename = os.path.basename(url)
    save_name = save_path + '/' + filename
    if not slient == True:
        print('Downloading', save_name)
    r = requests.get(url, stream=True)
    f = open(save_name, "wb")
    # chunk是指定每次写入的大小，每次只写了1024byte
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
    if not slient == True:
        print('Completed.')



def find_file_on_all_partitions(filename, slient=True):
    """
    Find files on all hard disk partitions.

    For example, if you want to find a file called "example.txt" on all hard disk partitions, then you should call it like this:

    find_file_on_all_partitions('example.txt')

    This function will search for this file in the order of "A:\\example.txt", "B:\\example.txt", etc.

    For another example, if you want to find a file called "example.txt" in the "example" folder on all hard disk partitions, then you should call:

    find_file_on_all_partitions('example/example.txt')

    This function will find this file in the order of "A:\\example\\example.txt", "B:\\example\\example.txt", etc.

    If found, the drive letter of the partition where the target file can be found will be placed in the "found_letters" list.

    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """

    now = disklst[0]
    now_file = now + ':' + os.sep + filename
    os.path.isfile(now_file)
    if now_file.isfile():
        found_letters.insert(0, now)
    del disklst[0]
    if not disklst == []:
        if not slient == True:
            find_file_on_all_partitions(filename)
        else:
            find_file_on_all_partitions(filename, slient=False)
    else:
        if not found_letters == []:
            if not slient == True:
                print('Done!')
                print('The target file was found in the partition with these drive letters:', found_letters)
        else:
            if not slient == True:
                print('Done!')
                print('The target file was not found!')
    del now
    del now_file
    



def get_os_partition(slient=True):
    """
    Get the drive letter of the partition where the system is located.

    Will return a variable "os_partition"

    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """

    os_partition_tmp = os.getenv("SystemDrive")
    os_partition = os_partition_tmp.replace(':', '')
    if not slient == True:
        print('The SystemDrive is', os_partition)
    del os_partition_tmp



def file_exists(filename, auto_exit=False, slient=True):
    """
    Check if the file exists.

    If the "auto_exit" parameter is True, the program will exit when the target file cannot be found.

    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """
    file = Path(filename)
    os.path.isfile(file)
    if file.is_file():
        if not slient == True:
            print('The file exists.')
        return 0
    else:
        if not slient == True:
            print('The file not exists.')
        return 1
    if not auto_exit == False:
        sys.exit(1)



def find_files_with_the_specified_extension(file_type, folder, slient=True):
    """
    Find the file with the specified extension name in targeted folder, and add the file name to the "file_list" list.

    The "file_type" variable must be an extension, and does not need to carry ".".

    For example "txt" "jar" "md" "class"

    Cannot be ".txt" ".jar" ".md" ".class"
    
    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """
    f_type = '.' + file_type
    items = os.listdir(folder)
    file_list = []
    for names in items:
        if names.endswith(f_type):
            file_list.append(names)
    del items



def find_str_in_file(string, filename, slient=True):
    """
    Find target string in a file.
    
    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """
    with open(filename, 'r') as f:
        counts = 0
        for line in f.readlines():
            time = line.count(string)
            counts += time
        if not slient == False:
            print("%s出现的次数：%d"%(str,counts))



