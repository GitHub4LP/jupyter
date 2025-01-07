import os
import subprocess

subprocess.run(r"jupyter lab --no-browser --ip=0.0.0.0 --port=7860 --ServerApp.allow_origin=* --notebook-dir=/ --ServerApp.disable_check_xsrf=True --allow-root --LabApp.token=", shell=True)
