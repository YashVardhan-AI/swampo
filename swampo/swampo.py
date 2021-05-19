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
@click.argument('files', nargs=-1)
def git_add_file(files):
    for arg in files:
        gitaddf(arg)
    
@git.command(help='See the status of your profile')
def profile():
    git_project_profile()

@git.command(help='Commit the staged files')
def settle():
    msg = click.prompt('Enter your Commit Message: ')
    gitCommit(msg)

@git.command('set-repo', help='')
def set_repo():
    name= cli.prompt('Enter a variable for your repository link: ')
    link= cli.prompt('Enter the link of your repository: ')
    set_remote(name, link)


@git.command('publish', help='Publish your repository to Github')
def push_repo():
    inp = cli.prompt('''How to you want to publish?
1. Publish to a specific remote and branch
2. Publish directly to upstream repo''')
    git_push(int(inp))
    

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