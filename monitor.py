#!/usr/bin/env python

import psutil
import sys

def get_pid(process_name):
    """
    returns a list of pids for a process-name
    """
    pids = []
    for proc in psutil.proc_iter():
        if proc == process_name:
            pid = proc.pid
            pids.append(pid)
    return pids


class ProcessMonitor(object):

    @staticmethod
    def monitor(pname):
        pids = get_pid(pname)
        return [ProcessMonitor(pid=pid) for pid in pids]

    def __init__(self, pid):
        self.pid = pid

    def statm(self):
        statm = {}
        if "linux" in sys.platform:
            filename = "/proc/{pid}/statm"
            lines = []
            with open(filename, 'r') as f:
                lines = f.readLines()

        return statm





