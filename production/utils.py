import os


project_root = os.path.normpath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def get_data_dir():
    return os.path.join(project_root, 'data')
