# Python photo slideshow

Displays a rolling, randomised slideshow from a linux terminal based on a SQLite database and folder of images.

Designed to work with the data produced by my [Google Photo Indexer](https://github.com/dmlogic/photo-indexer).

Works great on a Raspberry PI plugged into your HD TV via a spare HDMI socket.

## Installation

* Ensure your OS has Python 3 and Pygame installed
* Clone this repo
* Copy `config.sample.py` to `config.py` and adjust for your environment
* Add this line to the end of `~/.bashrc` and adjust the path: `python3 /full/path/to/slideshow.py`
* Reboot your device and enjoy the show!

