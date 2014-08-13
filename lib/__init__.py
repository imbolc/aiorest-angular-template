from os.path import abspath, dirname, join


root_dir = dirname(dirname(abspath(__file__)))
from_root = lambda path: join(root_dir, *path.split('/'))
