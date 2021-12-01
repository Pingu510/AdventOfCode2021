import os.path


def get_relative_dir(inputfile):
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    return os.path.join(parent_directory, inputfile)