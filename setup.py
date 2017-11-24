import setuptools

setuptools.setup(
    name="kinto_mpd",
    version="0.1.0",
    url="https://github.com/MusicBoxProject/raspberry-service",

    author="Mathieu Agopian",
    author_email="mathieu@agopian.info",

    description="A kinto plugin to start/stop playing a playlist in MPD",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=["python-mpd2"],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
