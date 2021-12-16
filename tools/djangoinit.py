# always import this to setup django in your standalone scripts. Ensures the path regardless of your script location.

import os, django, sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.as_posix())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
