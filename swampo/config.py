import click as cli

def config_swampo(name, mail, license, spass):
    global username 
    global usermail
    global usrlicense
    global usrspass

    username= name
    usermail=mail
    usrlicense=license
    usrspass=spass

def verify_config():
    entspass = input('Enter your S Password: ')
    if entspass==usrspass:
        cli.echo('Login Successful')
    else:
        cli.echo('Login Unsuccessful! Try again')

