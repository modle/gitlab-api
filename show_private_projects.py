import os
import sys
import gitlab
import subprocess

gl = gitlab.Gitlab(os.getenv('GL_URL'), os.getenv('GL_TOKEN'))

owned_projects = gl.projects.list(owned=True, all=True, visibility='private')

print ('i own {} projects'.format(len(owned_projects)))

projects_dir = '/home/matt/projects/all-projects'

for project in owned_projects:
    print(project.namespace['name'], project.name)

