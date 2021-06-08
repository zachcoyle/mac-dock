import setuptools

setuptools.setup(
    name="mac-dock",
    version="2020.12.3",
    install_requires=open("requirements.txt").read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=[
        "scripts/dock",
        "scripts/dock-add-app",
        "scripts/dock-add-folder",
        "scripts/dock-apps",
        "scripts/dock-folders",
        "scripts/dock-rm",
    ],
)
