import os
import sys
import gitlab
import subprocess

gl = gitlab.Gitlab(os.getenv('GL_URL'), os.getenv('GL_TOKEN'))

owned_projects = gl.projects.list(owned=True, all=True)

print ('i own {} projects'.format(len(owned_projects)))

for project in owned_projects:
#    print(project.ssh_url_to_repo)
    command = 'git clone {}'.format(project.ssh_url_to_repo)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    process.wait()

