import psutil
import os, signal
import re

def killp_by_name(name):
  # this process pid
  own_pid = os.getpid()
  # Store related pids here
  pids = []

  for proc in psutil.process_iter(['pid','name']):
    # Check for firefox in the process name
    if(re.search(rf'{name}', proc.info['name']) and int(proc.info['pid']) != own_pid):
      pids.append(proc.info['pid'])

  # Kill all processes matching name
  for pid in pids:
    os.kill(pid, signal.SIGKILL)
