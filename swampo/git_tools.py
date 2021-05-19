from re import split
import subprocess as sb
from runfile import rn as run, strun
import click as cli

def changeGitConfig(name, email):
    run(f'git config --global user.name {name}')
    run(f'git config --global user.email {email}')

def checkGitConfig(inputname): # After inputname you need to add a '\n' string
    name = sb.run('git config --global user.name', stdout=sb.PIPE, shell=True)
    if (name.stdout.decode())==inputname:
        pass
    else:
        key = input('Invalid Name. Did you enter the correct name? Enter D to retry, E to sign-up for Git, or A to skip')
        while True:
            # if key 'd' is pressed
            if key.lower().split()=='d':
                break
            # if key 'e' is pressed
            elif key.lower().split()=='d':
                break
            elif key.lower().split()=='a':
                break
            else:
                print('Invalid Input')

def git_init(directory, projectname):
    if 'current' in directory:
        run('git init')
        
    else:
        run(f'cd; cd {directory}; git init')

    cli.echo("Your project has been initialised! Check your Project Info by typing 'swampo -g project-info")

def git_clone(link, directory):
    if 'current' in directory:
        strun(f'git clone {link}')
    else:
        strun(f'cd; cd {directory}; git clone {link}')

def git_project_profile():
    try:
        run('git status')
        cli.echo("""'swampo git add-all' -- Stage all files
'swampo git add-file FILE        -- Stage particular files""")
    except CalledProcessError:
        cli.echo('OOPS! Something went wrong!')

def gitCommit(message):
    try:
        sb.run('git commit -m {message}', shell=True, check=True)
        print('Your files were commited successfully')
    except sb.CalledProcessError:
        print('Something went wrong...')
        
def create_ssh_key(email):
    try:
        run('ls -al ~/.ssh')
        print('You already have an SSH Key... ')
    except sb.CalledProcessError:
        cli.echo('''> Enter a file in which to save the key (/home/you/.ssh/id_ed25519): [Press enter]
> Enter passphrase (Press Enter for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]''')
        run(f'ssh-keygen -t ed25519 -C "{email}"')
        run(f'eval "$(ssh-agent -s)"; ssh-add ~/.ssh/id_ed25519')
        cli.echo("An SSH Key was generated in '~/.ssh/id_ed25519.pub'. Now you can add the key in Github")

    
def set_remote(name, branch, link):
    try:
        run('git remote add {name} {link}')
    except sb.CalledProcessError:
        cli.echo('Something went wrong. Did you type a valid link?')

def git_push(remote, branch):
    try:
        run(f'git push -u {remote} {branch}')
    except sb.CalledProcessError:
        cli.echo('Something went wrong... ')

def gitadd():
    try:
        run('git add .')
    except sb.CalledProcessError:
        cli.echo('Something went wrong!')

def gitaddf(arg):
    try:
        run(f'git add {arg}')
        cli.echo('Files were added successfully!')
    except sb.CalledProcessError:
        cli.echo('Something went wrong!')


    

