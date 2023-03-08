from setuptools import setup

setup(
    name='3d-IFu-letters',
    version='0.1',
    description='3D modeling of letters of Imaginarium Festival',
    author='Pierre Gibertini',
    packages=['3dletters'],
    install_requires=[
        'dessia_common>=0.13.2',
        'volmdlr>=0.9.0'
    ],
)