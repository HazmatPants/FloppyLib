# note: some functions may require elevated permissions

import shutil
import win32api
import os
import time

def checkReady(letter: str = "A:\\") -> bool:
    """
    Returns True if there is a floppy disk inserted into the drive.

    Attempts to read the file size of the floppy, Windows returns error 21 if the device is not ready.
    
    Parameters:
    letter (str): the letter of the floppy drive (default A:\\)
    """
    try:
        total, used, free = shutil.disk_usage(letter) # try to check file size of floppy
        if total:
            return True
    except WindowsError as e: # returns error 21 if there is no floppy inserted
        if e.winerror == 21:
            return False

def checkWriteProtect(letter: str = "A:\\") -> bool:
    """
    Returns True if the floppy is presumed to be write-protected.

    Attempts to write a temporary file to the disk (file is deleted afterwards)

    Parameters:
    letter (str): the letter of the floppy drive (default A:\\)
    """
    try:
        with open(f"{letter}/tmp", "w") as f:
            f.write(" ")

        time.sleep(0.1) # delay to ensure the file is not in use
        os.remove(f"{letter}/tmp")
        return False # if file.write was successful, disk is not write protected
    except PermissionError:
        return True # if permission is denied, disk is most likely write-protected
    except OSError as e:
        print(f"Error accessing disk: {e}")
        return True
    except Exception as e:
        print(f"Unexpected error: {e}")
        return True

def getFormat(letter: str = "A:\\") -> str:
    """
    Returns file system format, e.g. FAT.

    Parameters:
    letter (str): the letter of the floppy drive (default A:\\)
    """
    drive_info = win32api.GetVolumeInformation(letter)
    return drive_info[4]  # The file system type is the 5th element in the tuple

def getUsage(letter: str = "A:\\") -> tuple:
    """
    Returns disk usage as a tuple.

    Parameters:
    letter (str): the letter of the floppy drive (default A:\\)
    """
    try:
        return shutil.disk_usage(letter)
    except Exception as e:
        print(f"Error: {e}")

def byteConv(bytes, unit) -> int:
    """
    Returns bytes in other units

    Parameters:
    bytes (int): number of bytes to convert
    unit (str): unit to convert to, e.g. kb, mb
    """
    if unit == "kb":
        return bytes / 1024
    elif unit == "mb":
        return bytes / (1024**2)