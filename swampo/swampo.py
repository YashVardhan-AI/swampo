import click
from re import split
import click as cli
import subprocess as sb
from runfile import rn as run, strun
from config import *
from git_tools import *

@click.group()
@click.version_option('0.1.4', prog_name='Swampo')
def main():
    '''I am Swampo! A CLI Friend to make your life easier. '''
    pass

@main.group()
def git():
    '''Use Git Through Swampo'''
    
@git.command('config', help='Configure your Git Account')
def git_config():
    gname = click.prompt('Enter your username for Git: ')
    gmail = click.prompt('Enter your email ID linked to Github: ')
    changeGitConfig(gname, gmail)

@git.command('add-all', help= 'Add all files to stage')
def git_add():
    gitadd()

@git.command('add-file', help= ('Add your preferred files'))
def git_add_file(*args):
    for arg in args:
        gitaddf(arg)
    
@git.command(help='See the status of your profile')
def profile():
    git_project_profile()

@main.command()
def config():
    '''Helps to configure your profile for Swampo'''


@main.command()
def build():
    '''Build your desired project structure'''

@main.command()
def info():
    '''Know about what I can do for you'''


if __name__=='__main__':
    main()