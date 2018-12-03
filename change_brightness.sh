#!/bin/bash

USAGE="usage: change_brightness [inc | dec | get] VALUE"

MAXBRIGHT=$(cat "/sys/class/backlight/intel_backlight/max_brightness")
BRIGHTFILE="/sys/class/backlight/intel_backlight/brightness"
READBRIGHT=$(cat $BRIGHTFILE)

if [ "$#" -eq 0 ]; then
  echo $USAGE
  exit 0
fi

if [ $1 = "inc" ]; then
  let "BRIGHT=$READBRIGHT + $2"
  echo $(($BRIGHT>$MAXBRIGHT?$MAXBRIGHT:$BRIGHT)) > $BRIGHTFILE
elif [ $1 = "dec" ]; then
  let "BRIGHT=$READBRIGHT - $2"
  echo $(($BRIGHT<0?0:$BRIGHT)) > $BRIGHTFILE
elif [ $1 = "get" ]; then
  echo $READBRIGHT
else
  echo $USAGE
fi
