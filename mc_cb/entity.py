import mc_cb.commands as commands
from .variable import execute_handle
from .tools import command_str,tmp_function

class execute(execute_handle):
    def __init__(self,run:commands,*args:str | execute_handle) -> None:
        self.command_str=command_str("execute",*args,"run",run.command_str)
        tmp_function.add(self.command_str)