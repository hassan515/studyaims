import os
import sys
path = '/home/hassan515/EdForeign'
if path not is sys.path:
    sys.path.append(path)

os.environ['DJANG_SETTING_MODULE'] = "EdForeign.settings"
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())  
