from setuptools import setup

setup(
    name='yubi-lock',
    version='1.0',
    install_requires=[
        'click',
        'python-yubico'
    ],
    entry_points='''
        [console_scripts]
        yubi-lock=yubi_lock.cli:cli
    ''',
)
