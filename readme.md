# Support for translations in NVDA and the add-on template

This repository is intended to be used as a submodule for [NVDA](https://github.com/nvaccess/nvda) and the [add-on template](https://github.com/nvaccess/addonTemplate).

## Installation and Building an Executable

To install all dependencies (including PyInstaller) and build a standalone executable using [uv](https://github.com/astral-sh/uv):

1. Install all dependencies:

	```sh
	uv pip install .
	```

2. Build the executable:

	```sh
	uv run pyinstaller --onefile source/l10nUtil.py
	```

The resulting executable will be located in the `dist` directory.
