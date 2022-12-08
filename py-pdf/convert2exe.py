from distutils.core import setup
import py2exe

setup(console=['wrapper.py'], packages=['merge', 'split'], package_dir={
    'merge':'merge',
    'split':'split'
})