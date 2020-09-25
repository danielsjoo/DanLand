#!/bin/bash
#this simple script copies the last file from windows downloads to the 
#current directory in wsl2

windowsDownloadsLocation="/mnt/c/Users/danie/Downloads"
fileNameRecentDownload=$(ls -Art $windowsDownloadsLocation | tail -1)
mv "$windowsDownloadsLocation/$fileNameRecentDownload" .
