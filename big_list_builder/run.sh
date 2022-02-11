# clean README
printf "" > ../README.md
# Intro
./appendIntro.sh
# Table of Contents
printf "\n\n---\n\n## Contents\n" >> ../README.md
./appendToC.sh
# Content
printf "\n---\n\n" >> ../README.md
./appendCon.sh
