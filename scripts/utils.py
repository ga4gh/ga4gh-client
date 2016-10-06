"""
Utilities for scripts
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import functools
import os
import shlex
import sys
import time
import subprocess

import humanize
import yaml


def getPathOfExecutable(executable):
    """
    Returns the full path of the executable, or None if the executable
    can not be found.
    """
    exe_paths = os.environ['PATH'].split(':')
    for exe_path in exe_paths:
        exe_file = os.path.join(exe_path, executable)
        if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
            return exe_file
    return None


def requireExecutables(executables):
    """
    Check that all of the given executables are on the path.
    If at least one of them is not, exit the script and inform
    the user of the missing requirement(s).
    """
    missingExecutables = []
    for executable in executables:
        if getPathOfExecutable(executable) is None:
            missingExecutables.append(executable)
    if len(missingExecutables) > 0:
        log("In order to run this script, the following "
            "executables need to be on the path:")
        for missingExecutable in missingExecutables:
            print(missingExecutable)
        exit(1)


def ga4ghImportGlue():
    """
    Call this method before importing a ga4gh module in the scripts dir.
    Otherwise, you will be using the installed package instead of
    the development package.
    Assumes a certain directory structure.
    """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(path)


def log(message):
    print(message)


class Timed(object):
    """
    Decorator that times a method, reporting runtime at finish
    """
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self.start = time.time()
            result = func(*args, **kwargs)
            self.end = time.time()
            self._report()
            return result
        return wrapper

    def _report(self):
        delta = self.end - self.start
        timeString = humanize.time.naturaldelta(delta)
        log("Finished in {} ({:.2f} seconds)".format(timeString, delta))


def runCommand(command, silent=False):
    """
    Run a shell command
    """
    splits = shlex.split(command)
    runCommandSplits(splits, silent=silent)


def runCommandSplits(splits, silent=False):
    """
    Run a shell command given the command's parsed command line
    """
    try:
        if silent:
            with open(os.devnull, 'w') as devnull:
                subprocess.check_call(splits, stdout=devnull, stderr=devnull)
        else:
            subprocess.check_call(splits)
    except OSError, e:
        if e.errno == 2:  # cmd not found
            raise Exception(
                "Can't find command while trying to run {}".format(splits))
        else:
            raise


def getAuthValues(filePath='scripts/auth.yml'):
    """
    Return the script authentication file as a dictionary
    """
    return getYamlDocument(filePath)


def getYamlDocument(filePath):
    """
    Return a yaml file's contents as a dictionary
    """
    with open(filePath) as stream:
        doc = yaml.load(stream)
        return doc
