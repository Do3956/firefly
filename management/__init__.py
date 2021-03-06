#coding:utf8
'''
Created on 2013-8-8

@author: lan (www.9miao.com)
'''
from firefly.management import commands 
import sys

class CommandError(Exception): 
    """
    """
    def __str__(self):
        return "command error"

class Command:
    
    def __init__(self,subcommond,*args):
        '''工具类指令
        '''
        self.subcommond = subcommond
        self.args = args
        
    def execute(self):
        '''
        '''
        commmd = getattr(commands,self.subcommond )
        commmd.execute(*self.args)
        
        
def execute_commands(*args):
    '''
    '''
    if len(args)<2:
        raise CommandError()
    subcommand = args[1]
    comm = Command(subcommand,*tuple(args[2:]))
    comm.execute()
    
    
    