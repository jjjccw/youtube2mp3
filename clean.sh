#!/usr/bin/bash
if [[ -d ~/Music/youtube2mp3 ]];then
    echo "output directory found, removing now"
    rm -fr ~/Music/youtube2mp3/
else
    echo "--skipping removal of ~/Music/youtube2mp3/"
fi

if [[ -d dist ]];then
    echo "dist directory found, removing now"
    rm -fr dist
else
    echo "--skipping removal of dist/"
fi
