# runs only when the terminal directory is set to big_list_builder

# clean README
printf "" > ../README.md

# Intro
printf "![banner](./TCS-banner.png)\n# Awesome Theoretical Computer Science [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)\nThe interdisciplinary of Mathematics and Computer Science; It is distinguished by its emphasis on mathemtical technique and rigour." >> ../README.md

# Table of Contents
printf "\n\n---\n\n## Contents\n" >> ../README.md
## input
  ## file name
  ## last level to generate (-1 disabled)
  ## whether last level is one line (1 true)
python3 genToC.py 'source.json' -1 1 >> ../README.md

# Content
printf "\n---\n\n" >> ../README.md
## input
  ## file name
python3 genCon.py 'source.json' >> ../README.md