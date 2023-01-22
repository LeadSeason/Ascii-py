## Install dependencies
```
python -m venv venv
source venv/bin/activate 		# Bash/Zsh
source venv/bin/activate.fish 	# Fish
pip install -r requirements.txt
```

## Usage
```
$ python ascii.py --help
usage: ascii.py [-h] [-c CHARS] [-s SCALE] [-b BRIGHTNESS] convert_file

positional arguments:
  convert_file          image file to be converted

options:
  -h, --help            show this help message and exit
  -c CHARS, --chars CHARS
                        Characters to be used in ascii art
  -s SCALE, --scale SCALE
  -b BRIGHTNESS, --brightness BRIGHTNESS
```
