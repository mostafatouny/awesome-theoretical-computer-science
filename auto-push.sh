#!/bin/sh

currentDate=`date`

git add .
git commit -m "$currentDate"
git push -u origin main
