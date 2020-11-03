from setuptools import setup, find_packages

requirements = [
    'box2d-py~=2.3.5',
    'gym>=0.17.1',
    'numpy>=1.18',
]

setup(
    name='lunar_lander_custom',
    version='0.0.1',
    python_requires='>=3.5',
    description='LunarLander with Mixed Action Space',
    url='git@github.com:nimishsantosh107/LunarLander-Custom.git',
    author='Nimish Santosh',
    author_email='nimishsantosh107@gmail.com',
    install_requires=requirements,
    license='unlicense',
    packages=packages=find_packages(include=['lunar_lander_custom', 'lunar_lander_custom.*']),
    zip_safe=False
)