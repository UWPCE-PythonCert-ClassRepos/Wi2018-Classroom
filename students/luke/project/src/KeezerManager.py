#!/usr/bin/env python3

"""
Keezer management project.  See README.md
"""

import os
import imp
import glob

import KeezerSensor
import KeezerDisplay

# Concrete sensor and display classes are loaded dynamically.  There are
# a few approaches to this.  In addition to the goergevreilly one copied
# below, there's another example at:
# https://www.blog.pythonlibrary.org/2012/07/31/advanced-python-how-to-dynamically-load-modules-or-classes/

# https://www.georgevreilly.com/blog/2016/03/02/PythonImportSubclassFromDynamicPath.html
def import_class(implementation_filename, base_class):


    impl_dir, impl_filename = os.path.split(implementation_filename)
    module_name, _ = os.path.splitext(impl_filename)

    try:
        sys.path.insert(0, impl_dir)
        fp, filename, description = imp.find_module(module_name)
        module = imp.load_module(module_name, fp, filename, description)
        for name in dir(module):
            obj = getattr(module, name)
            if (type(obj) == type(base_class)
                and issubclass(obj, base_class)
                and obj != base_class):
                    return obj
        raise ValueError("No subclass of {0} in {1}".format(
                base_class.__name__, implementation_filename))
    finally:
        sys.path.pop(0)


class KeezerManager:
    """
    Driver class for keezer manager.

    Loads sensor and display modules dynamically.
    Polls sensors.
    Passes sensor data to displays.
    """

    def __init__(self):
        self.sensors = []
        self.outputs = []

        """ Populate sensors from sensors/ directory"""
        for file in glob.glob("sensors/*.py"):
            self.sensors.append(import_class(file, KeezerSensor))

        """ Populate displays from displays/ directory"""
        for file in glob.glob("displays/*.py"):
            self.sensors.append(import_class(file, KeezerDisplay))


    def run(self):
        while True:
            # sample time
            # poll sensors
                # send sensor data to display

            # sleep for remainder of polling interval


if __name__ == "__main__":
    # List registered sensors and displays

