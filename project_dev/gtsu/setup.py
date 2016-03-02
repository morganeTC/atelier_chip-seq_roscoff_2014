from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "gtsu",
    version = "0.0",
    author_email='puthier@gmail.com',
    author = "Denis Puthier",
    description = ("Genomic tool suite"),
    url = "",
    keywords = "genomics",
    packages=['gtsu'],
    scripts=['bin/gtsu'],
    install_requires = [""],
    license='LICENSE.txt',
    long_description=open('README.rst').read(),
    cmdclass={'install': install}
    classifiers=[
        ""
    ],

)
