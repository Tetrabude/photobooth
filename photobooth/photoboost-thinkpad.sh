#!/bin/bash

while(true)
do
  gphoto2 --wait-event --capture-image-and-download --hook-script view-photo.sh
done


