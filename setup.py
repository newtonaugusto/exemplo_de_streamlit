# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by `pymedphys dev propagate`

from setuptools import setup

package_dir = {"": "lib"}

packages = [
    "pymedphys",
    "pymedphys._base",
    "pymedphys._data",
    "pymedphys._dev",
    "pymedphys._dicom",
    "pymedphys._dicom.anonymise",
    "pymedphys._dicom.constants",
    "pymedphys._dicom.ct",
    "pymedphys._dicom.delivery",
    "pymedphys._dicom.rtplan",
    "pymedphys._dicom.structure",
    "pymedphys._dicom.utilities",
    "pymedphys._electronfactors",
    "pymedphys._experimental",
    "pymedphys._experimental.autosegmentation",
    "pymedphys._experimental.fileformats",
    "pymedphys._experimental.fileformats.mapcheck",
    "pymedphys._experimental.fileformats.mephysto",
    "pymedphys._experimental.fileformats.profiler",
    "pymedphys._experimental.film",
    "pymedphys._experimental.paulking",
    "pymedphys._experimental.pedromartinez",
    "pymedphys._experimental.pedromartinez.oncentra",
    "pymedphys._experimental.pedromartinez.utils",
    "pymedphys._experimental.pinnacle",
    "pymedphys._experimental.plancomplexity",
    "pymedphys._experimental.pseudonymisation",
    "pymedphys._experimental.quickcheck",
    "pymedphys._experimental.serviceplans",
    "pymedphys._gamma",
    "pymedphys._gamma.api",
    "pymedphys._gamma.implementation",
    "pymedphys._gamma.utilities",
    "pymedphys._icom",
    "pymedphys._imports",
    "pymedphys._losslessjpeg",
    "pymedphys._mocks",
    "pymedphys._monaco",
    "pymedphys._mosaiq",
    "pymedphys._mudensity",
    "pymedphys._mudensity.delivery",
    "pymedphys._mudensity.plt",
    "pymedphys._streamlit",
    "pymedphys._streamlit.apps",
    "pymedphys._streamlit.apps.mudensity",
    "pymedphys._streamlit.utilities",
    "pymedphys._trf",
    "pymedphys._trf.decode",
    "pymedphys._trf.manage",
    "pymedphys._utilities",
    "pymedphys._utilities.algorithms",
    "pymedphys._utilities.constants",
    "pymedphys._utilities.filehash",
    "pymedphys._utilities.transforms",
    "pymedphys._vendor",
    "pymedphys._vendor.apipkg",
    "pymedphys._vendor.pylinac",
    "pymedphys._vendor.pylinac.core",
    "pymedphys._wlutz",
    "pymedphys.beta",
    "pymedphys.cli",
    "pymedphys.cli.experimental",
    "pymedphys.experimental",
    "pymedphys.tests",
    "pymedphys.tests.coordinates",
    "pymedphys.tests.delivery",
    "pymedphys.tests.dicom",
    "pymedphys.tests.dicom.rtplan",
    "pymedphys.tests.e2e",
    "pymedphys.tests.experimental",
    "pymedphys.tests.experimental.film",
    "pymedphys.tests.experimental.mapcheck",
    "pymedphys.tests.experimental.mephysto",
    "pymedphys.tests.experimental.paulking",
    "pymedphys.tests.experimental.paulking.film",
    "pymedphys.tests.experimental.paulking.test_coll",
    "pymedphys.tests.experimental.pinnacle",
    "pymedphys.tests.experimental.profiler",
    "pymedphys.tests.experimental.pseudonymisation",
    "pymedphys.tests.gamma",
    "pymedphys.tests.logfiles",
    "pymedphys.tests.logging",
    "pymedphys.tests.losslessjpeg",
    "pymedphys.tests.mocks",
    "pymedphys.tests.monaco",
    "pymedphys.tests.mudensity",
    "pymedphys.tests.trf",
    "pymedphys.tests.utilities",
    "pymedphys.tests.winstonlutz",
]

package_data = {
    "": ["*"],
    "pymedphys._experimental.serviceplans": ["templates/*"],
    "pymedphys._streamlit.apps": ["data/*"],
    "pymedphys.tests.dicom": ["data/rtplan/*", "scratch/*"],
    "pymedphys.tests.e2e": [
        "cypress/*",
        "cypress/fixtures/.gitignore",
        "cypress/integration/streamlit/*",
        "cypress/plugins/*",
        "cypress/support/*",
    ],
    "pymedphys.tests.experimental.mephysto": [
        "data/baselines/*",
        "data/measurements/*",
    ],
    "pymedphys.tests.experimental.paulking.film": ["data/*"],
}

extras_require = {
    ':python_version >= "3.6.0" and python_version < "3.7.0"': ["dataclasses"],
    "dev": [
        "tqdm",
        "attrs",
        "watchdog",
        "keyring",
        "packaging",
        "PyYAML",
        "requests",
        "numpy>=1.12",
        "matplotlib",
        "scipy",
        "pandas",
        "Pillow",
        "imageio",
        "shapely>=1.7.0",
        "dbfread",
        "pydicom>=2.0.0",
        "pynetdicom",
        "pylibjpeg-libjpeg",
        "immutables",
        "cython",
        "pymssql",
        "kiwisolver!=1.3.0",
        "python_dateutil",
        "scikit-image",
        "streamlit==0.70.0",
        "timeago",
        "sphinx>=1.4,<1.8",
        "sphinx-rtd-theme>=0.4.3,<0.5.0",
        "sphinxcontrib-napoleon",
        "sphinx-argparse",
        "sphinx-autobuild",
        "nbsphinx",
        "jupyter_client",
        "ipython",
        "ipykernel",
        "nbconvert==6.0.6",
        "pytest",
        "pytest-sugar",
        "hypothesis",
        "psutil",
        "pylint",
        "pytest-pylint",
        "pre-commit",
        "black>=19.3b0,<20.0",
        "mypy",
        "rope",
        "doc8",
        "tomlkit",
    ],
    "dicom": ["pydicom>=2.0.0", "pynetdicom", "pylibjpeg-libjpeg", "immutables"],
    "docs": [
        "sphinx>=1.4,<1.8",
        "sphinx-rtd-theme>=0.4.3,<0.5.0",
        "sphinxcontrib-napoleon",
        "sphinx-argparse",
        "sphinx-autobuild",
        "nbsphinx",
        "jupyter_client",
        "ipython",
        "ipykernel",
        "nbconvert==6.0.6",
    ],
    "doctests": ["tensorflow>=2.2.0", "black>=19.3b0,<20.0", "tomlkit"],
    "experimental": ["python_dateutil", "scikit-image"],
    "gui": ["streamlit==0.70.0", "timeago"],
    "ml": ["tensorflow>=2.2.0"],
    "tests": [
        "pytest",
        "pytest-sugar",
        "hypothesis",
        "psutil",
        "pylint",
        "pytest-pylint",
    ],
    "user": [
        "tqdm",
        "attrs",
        "watchdog",
        "keyring",
        "packaging",
        "PyYAML",
        "requests",
        "numpy>=1.12",
        "matplotlib",
        "scipy",
        "pandas",
        "Pillow",
        "imageio",
        "shapely>=1.7.0",
        "dbfread",
        "pydicom>=2.0.0",
        "pynetdicom",
        "pylibjpeg-libjpeg",
        "immutables",
        "cython",
        "pymssql",
        "kiwisolver!=1.3.0",
        "python_dateutil",
        "scikit-image",
        "streamlit==0.70.0",
        "timeago",
    ],
}

entry_points = {"console_scripts": ["pymedphys = pymedphys.cli:pymedphys_cli"]}

setup_kwargs = {
    "name": "pymedphys",
    "version": "0.34.0.dev10",
    "description": "Medical Physics library",
    "long_description": "|logo|\n\n.. |logo| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/pymedphys_title.png\n    :target: https://docs.pymedphys.com/\n\n.. START_OF_DOCS_IMPORT\n\n**A community effort to develop an open standard library for Medical Physics\nin Python. Building quality transparent software together via peer review\nand open source distribution. Open code is better science.**\n\n|build| |pypi| |python| |license|\n\n.. |build| image:: https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fpymedphys%2Fpymedphys%2Fbadge&label=build&logo=none\n    :target: https://actions-badge.atrox.dev/pymedphys/pymedphys/goto\n\n.. |pypi| image:: https://img.shields.io/pypi/v/pymedphys\n    :target: https://pypi.org/project/pymedphys/\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/pymedphys\n    :target: https://pypi.org/project/pymedphys/\n\n.. |license| image:: https://img.shields.io/pypi/l/pymedphys\n    :target: https://choosealicense.com/licenses/apache-2.0/\n\n\nWhat is PyMedPhys?\n------------------\n\nAn open-source Medical Physics python library with a focus on being\na place to share, review, improve, and transparently learn off of each\nother's code. It is inspired by the collaborative work of our physics peers\nin astronomy and their `Astropy Project`_. PyMedPhys is available on `PyPI`_\nand `GitHub`_.\n\n.. _`Astropy Project`: http://www.astropy.org/\n.. _`PyPI`: https://pypi.org/project/pymedphys/\n.. _`GitHub`: https://github.com/pymedphys/pymedphys\n\n\nMailing list\n------------\n\nIf you would like to dive into the community a great place to get started is\nto sign up to `the mailing list`_ and say hi by introducing yourself with\nwhere you're from, and what you hope to achieve with PyMedPhys.\n\n.. _`the mailing list`: https://groups.google.com/g/pymedphys\n\n\nTable of contents\n-----------------\n\n`Tutorials`_\n........................\n\nGet started with a hands-on introduction to PyMedPhys for beginners\n\n`How-To guides`_\n........................\n\nGuides and recipes for common problems and tasks\n\n`Reference`_\n............................\n\nTechnical reference for the `library`_ (modules, functions and classes),\nas well as the available `command line tools`_.\n\n`Background`_\n..............................\n\nExplanation and discussion of key topics and concepts\n\n\nBeta level of development\n-------------------------\n\nPyMedPhys is currently within the ``beta`` stage of its life-cycle. It will\nstay in this stage until the version number leaves ``0.x.x`` and enters\n``1.x.x``. While PyMedPhys is in ``beta`` stage, **no API is guaranteed to be\nstable from one release to the next.** In fact, it is very likely that the\nentire API will change multiple times before a ``1.0.0`` release. In practice,\nthis means that upgrading ``pymedphys`` to a new version will possibly break\nany code that was using the old version of pymedphys. We try to be abreast of\nthis by providing details of any breaking changes from one release to the next\nwithin the `Release Notes`_.\n\nOur Team\n--------\n\nPyMedPhys is what it is today due to its maintainers and contributors both past\nand present. Here is our team.\n\nMaintainers\n...........\n\n* `Simon Biggs`_\n    * `Riverina Cancer Care Centre`_, Australia\n\n.. _`Simon Biggs`: https://github.com/SimonBiggs\n\n* `Stuart Swerdloff`_\n    * `ELEKTA Pty Ltd`_: New Zealand\n\n.. _`Stuart Swerdloff`: https://github.com/sjswerdloff\n\n\nActive contributors\n...................\n\n* `Phillip Chlap`_\n    * `University of New South Wales`_, Australia\n    * `South Western Sydney Local Health District`_, Australia\n\n.. _`Phillip Chlap`: https://github.com/pchlap\n\n* `Matthew Cooper`_\n\n.. _`Matthew Cooper`: https://github.com/matthewdeancooper\n\n* `Jake Rembish`_\n    * `UT Health San Antonio`_, USA\n\n.. _`Jake Rembish`: https://github.com/rembishj\n\n* `Pedro Martinez`_\n    * `University of Calgary`_, Canada\n    * `Tom Baker Cancer Centre`_, Canada\n\n.. _`Pedro Martinez`: https://github.com/peterg1t\n\n* `Rafael Ayala`_\n    * `Hospital General Universitario Gregorio Marañón`_, Spain\n\n.. _`Rafael Ayala`: https://github.com/ayalalazaro\n\n\n|rccc| |uth| |uoc| |hgugm|\n\n\nMaintainer emeritus\n...................\n\n* `Matthew Jennings`_\n    * `Royal Adelaide Hospital`_, Australia\n\n.. _`Matthew Jennings`: https://github.com/Matthew-Jennings\n\n|rah|\n\nPast contributors\n.................\n\n* `Matthew Sobolewski <https://github.com/msobolewski>`_\n* `Paul King <https://github.com/kingrpaul>`_\n* `Jacob McAloney <https://github.com/JacobMcAloney>`_\n\n\n.. |rccc| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/rccc_200x200.png\n    :target: `Riverina Cancer Care Centre`_\n\n.. |rah| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/gosa_200x200.png\n    :target: `Royal Adelaide Hospital`_\n\n.. |jarmc| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/jarmc_200x200.png\n    :target: `Anderson Regional Cancer Center`_\n\n.. |nbcc| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/nbcc_200x200.png\n    :target: `Northern Beaches Cancer Care`_\n\n.. |uoc| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/uoc_200x200.png\n    :target: `University of Calgary`_\n\n.. |uth| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/UTHSA_logo.png\n    :target: `UT Health San Antonio`_\n\n.. |hgugm| image:: https://github.com/pymedphys/pymedphys/raw/master/docs/logos/HGUGM_200x200.png\n    :target: `Hospital General Universitario Gregorio Marañón`_\n\n.. _`Riverina Cancer Care Centre`: https://www.riverinacancercare.com.au/\n\n.. _`ELEKTA Pty Ltd`: https://www.elekta.com/\n\n.. _`Royal Adelaide Hospital`: https://www.rah.sa.gov.au/\n\n.. _`University of New South Wales`: https://www.unsw.edu.au/\n\n.. _`South Western Sydney Local Health District`: https://www.swslhd.health.nsw.gov.au/\n\n.. _`Anderson Regional Cancer Center`: https://www.andersonregional.org/services/cancer-care/\n\n.. _`Northern Beaches Cancer Care`: https://www.northernbeachescancercare.com.au/\n\n.. _`University of Calgary`: https://www.ucalgary.ca/\n\n.. _`Tom Baker Cancer Centre`: https://www.ahs.ca/tbcc\n\n.. _`UT Health San Antonio`: https://www.uthscsa.edu/academics/biomedical-sciences/programs/radiological-sciences-phd\n\n.. _`Hospital General Universitario Gregorio Marañón`: https://www.comunidad.madrid/hospital/gregoriomaranon/\n\n.. END_OF_DOCS_IMPORT\n\n.. _`Tutorials`: https://docs.pymedphys.com/tutes\n.. _`How-To guides`: https://docs.pymedphys.com/howto\n.. _`Reference`: https://docs.pymedphys.com/ref\n.. _`Background`: https://docs.pymedphys.com/background\n\n.. _`library`: https://docs.pymedphys.com/ref/lib\n.. _`command line tools`: https://docs.pymedphys.com/ref/cli\n\n.. _`Release Notes`: http://docs.pymedphys.com/release-notes.html\n",
    "author": "PyMedPhys Contributors",
    "author_email": "developers@pymedphys.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://pymedphys.com",
    "package_dir": package_dir,
    "packages": packages,
    "package_data": package_data,
    "extras_require": extras_require,
    "entry_points": entry_points,
    "python_requires": ">=3.6,<4.0",
}


setup(**setup_kwargs)
