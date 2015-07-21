#!/bin/bash
#################################
# Speech Script by Dan Fountain #
#      TalkToDanF@gmail.com     #
#################################
#http://danfountain.com/2013/03/raspberry-pi-text-to-speech/

INPUT=$*
STRINGNUM=0

ary=($INPUT)
#echo "---------------------------"
#echo "Speech Script by Dan Fountain"
#echo "TalkToDanF@gmail.com"
#echo "---------------------------"
for key in "${!ary[@]}" 
  do
    SHORTTMP[$STRINGNUM]="${SHORTTMP[$STRINGNUM]} ${ary[$key]}"
    LENGTH=$(echo ${#SHORTTMP[$STRINGNUM]})
    #echo "word:$key, ${ary[$key]}"
    #echo "adding to: $STRINGNUM"
    if [[ "$LENGTH" -lt "100" ]]; then
      #echo starting new line
      SHORT[$STRINGNUM]=${SHORTTMP[$STRINGNUM]}
    else
      STRINGNUM=$(($STRINGNUM+1))
      SHORTTMP[$STRINGNUM]="${ary[$key]}"
      SHORT[$STRINGNUM]="${ary[$key]}"
    fi
done

for key in "${!SHORT[@]}"
  do
    #echo "line: $key is: ${SHORT[$key]}"

    #echo "Playing line: $(($key+1)) of $(($STRINGNUM+1))"
    NEXTURL=$(echo ${SHORT[$key]} | xxd -plain | tr -d '\n' | sed 's/\(..\)/%\1/g')
    mpg123 -q -h 10 -d 11 "http://translate.google.com/translate_tts?tl=en&ie=UTF-8&q=$NEXTURL"
	#-d is doubletime, -h is halftime for playback
	#adding &ie=utf-8 fixes issues with special chars
done
