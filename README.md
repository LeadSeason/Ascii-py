<h1 align="center">Ascii.py</h1>
<p align="center">Ascii converter made in python</p>

## about
Converts Image to ascii and prints to stdout. converts colors to closest xterm256 color.
Simple project made in a day. 

## example output

Original             |  Ascii
:-------------------------:|:-------------------------:
![](./example.png)  |  ![](./example-output.png)

## Install dependencies
```
python -m venv venv
source venv/bin/activate        # Bash/Zsh
source venv/bin/activate.fish   # Fish
pip install -r requirements.txt
```

## Usage
Use a terminal with xterm256 color support for best results.
```
$ python ascii.py --help
usage: ascii.py [-h] [-c CHARS] [-s SCALE] [-b BRIGHTNESS] convert_file

positional arguments:
  convert_file          image file to be converted

options:
  -h, --help            show this help message and exit
  -c CHARS, --chars CHARS                       Characters to be used in ascii art
  -s SCALE, --scale SCALE                       Size Multiplyer. Default 0.08
  -b BRIGHTNESS, --brightness BRIGHTNESS        Britness multipyer. Default 1.5
```

## faq
#### sauce for example?
https://www.reddit.com/r/Saber/comments/3nzufs/saber_render/

