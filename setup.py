import setuptools

setuptools.setup(
    name="fefradio",
    version="0.0.1",
    py_modules=["fefradio"],
    install_requires=[
        "click",
        "spotipy",
    ],
    entry_points={
        "console_scripts": [
            "fefradio=fefradio:cli",
        ],
    },
)
