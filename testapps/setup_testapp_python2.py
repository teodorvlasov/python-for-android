
from distutils.core import setup
from setuptools import find_packages

options = {'apk': {'debug': None,
                   'requirements': 'sdl2,pyjnius,kivy,python2',
                   'android-api': 19,
                   'ndk-dir': '/home/asandy/android/crystax-ndk-10.3.2',
                   'dist-name': 'bdisttest',
                   'ndk-version': '10.3.2',
                   'permission': 'VIBRATE',
                   }}

package_data = {'': ['*.py',
                     '*.png']
                }

packages = find_packages()
print('packages are', packages)

setup(
    name='testapp_python2',
    version='1.1',
    description='p4a setup.py test',
    author='Alexander Taylor',
    author_email='alexanderjohntaylor@gmail.com',
    packages=find_packages(),
    options=options,
    package_data={'testapp': ['*.py', '*.png']}
)
