from distutils.core import setup
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='urlrecode',
    version='1.0.7',
    url='https://github.com/MKaterbarg/urlrecode',
    license='MIT',
    author='Martijn Katerbarg',
    packages=['urlrecode',],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email='martijnkaterbarg@gmail.com',
    description='Simple URLEncode and URLDecode which I needed for a couple of bash scripts.',
    entry_points={
        'console_scripts': [
            'urlrecode = urlrecode.main:main',
        ],
    },
)
