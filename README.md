# jsignal

A Pythonic implementation of the observer pattern.

# Installation

Installing this package is very simple. It can be installed with `pip` in two different ways. One is to install via the directory or url.

```shell
# Download from a directory
git clone https://github.com/JohnDevlopment/jsignal.git
cd jsignal
pip install .
```

```shell
# Download directly from a url
pip install https://github.com/JohnDevlopment/jsignal.git
```

The other is to install one of the wheels, which can be downloaded from the [releases](/releases). Let's say you downloaded `jsignal-1.0.0-py3-none-any.whl`. Well, the commandline looks like this:

```shell
pip install jsignal-1.0.0-py3-none-any.whl
```

## Requirements

`jsignal` currently requires Python version 3.9 or above. Its main dependencies are:
* `typing-extensions`
* `icecream` (optional, for debugging)
* `pytest` (optional, for testing)
* `pytest-cov` (optional, for testing)
* `poetry` (to build from source)
