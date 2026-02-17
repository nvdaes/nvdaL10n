from setuptools import setup
import py2exe

setup(
	console=[{"script": "source/l10nUtil.py"}],
	options={
		"py2exe": {
			"includes": ["lxml._elementpath"],
			"excludes": [],
			"dll_excludes": [],
			"bundle_files": 3,
			"compressed": True,
			"optimize": 2,
		}
	},
	zipfile=None,
)
