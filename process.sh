#!/bin/sh

#rename 's/ /_/g' $1/*.jpg

#for f in $1/*.jpg; do
  #convert "$f" -crop 720x720+280+0 $2/$(basename "$f")
#done

for f in *_01.jpg; do
  w=$(echo $f | sed 's/_01.jpg$//')
  montage -geometry +0+0 ${w}_0[1-9].jpg ${w}.jpg
  rm ${w}_0[1-9].jpg
done
