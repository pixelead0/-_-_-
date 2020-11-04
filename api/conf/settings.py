import os.path
import glob

from dotenv import load_dotenv
load_dotenv(verbose=True)

conffiles = glob.glob(os.path.join(
    os.path.dirname(__file__), 'settings.d', '*.py'))
conffiles.sort()

for f in conffiles:
    exec(open(os.path.abspath(f)).read())
