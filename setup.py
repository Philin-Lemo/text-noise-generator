from setuptools import setup, find_packages

setup(
    name="Text noise generator",
    version="0.0.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "tng = text_noise_generator.text_noise_generator:main",
        ],
    },
    install_requires=[
        'windows-curses; sys_platform == "win32"',
    ],
)
