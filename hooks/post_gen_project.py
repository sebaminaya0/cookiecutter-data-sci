import os
import subprocess

MESSAGE_COLOR = '\033[94m'
RESET_COLOR = '\033[0m'

print(f'{MESSAGE_COLOR}Installing dependencies...{RESET_COLOR}')
print(f'{MESSAGE_COLOR}Initializing git repo...{RESET_COLOR}')

username = '{{ cookiecutter.github_username }}'
email = '{{ cookiecutter.email }}'

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'congif', 'user.name', f'{username}'])
subprocess.call(['git', 'congif', 'email.name', f'{email}'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f'{MESSAGE_COLOR}Creating conda environment...{RESET_COLOR}')

subprocess.call(['conda', 'env', 'create', '-f', 'environment.yml'])
subprocess.call(['conda', 'activate', '{{ cookiecutter.project_slug }}'])

print(f'{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_COLOR}')