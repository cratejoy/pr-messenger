from setuptools import setup, find_packages

setup(
    name='pr-messenger',
    description='Quick script for posting messages and statuses to Github PRs',
    url='https://github.com/cratejoy/pr-messenger',
    packages=find_packages(),
    install_requires=[
        'PyGithub==1.35'
    ],
    entry_points='''
        [console_scripts]
        pr-messenger=pr_messenger.pr_messenger:main
    ''',
)
