# Environments, Conda & Pip
'''
It is good practice to have a unique environment for each project or task. This ensures that dependencies of 
one project will not create breaking changes for another.'''


# Creating Python environments for a project or task

'''
Do not install packages straight into your ‘base’ environment,
create an environment for each project or task, just to keep things separate. 

conda create --name my_first_env python=3.7
'''

# switch to the newly created environment.

'''
conda activate tutorial
'''

# check the available environments

'''
conda env list
'''