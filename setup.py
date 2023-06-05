import os
from setuptools import setup, find_packages

def src(pth):
    return os.path.join(os.path.dirname(__file__), pth)

# Project description
descr = 'EAGE Hackathon 2023 - NLP'

setup(
    name="geodude", # Choose your package name
    description=descr,
    long_description=open(src('README.md')).read(),
    keywords=['NLP',
              'LLM',
              'Hackathon'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    author='Miguel Corrales, Nick Luiken, Mustafa Alfarhan',
    author_email='miguel.corrales@kaust.edu.sa, nicolaas.luiken@kaust.edu.sa, mustafa.alfarhan@kaust.edu.sa',
    install_requires=['numpy >= 1.15.0',
                      'torch >= 1.2.0',
                      'pylops >= 1.17.0'],
    packages=find_packages(),
    use_scm_version=dict(root='.',
                         relative_to=__file__,
                         write_to=src('package/version.py')),
    setup_requires=['setuptools_scm'],

)
