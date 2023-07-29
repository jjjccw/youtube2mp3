#!/usr/bin/bash
if [[ -d ~/Downloads/youtube2mp3 ]];then
    echo "output directory found, removing now"
    rm -fr ~/Downloads/youtube2mp3/
else
    echo "--nothing to do for clean.sh"
fi
