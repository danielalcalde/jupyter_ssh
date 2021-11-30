import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='jupyter_ssh',
     version='0.0.1',
     scripts=['jupyter_ssh"] ,
     author="Daniel Alcalde Puente",
     author_email="d.alcald.epuente@fz-juelich.de",
     description="A tool for easily opening jupyter notebook remotely through ssh.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/danielalcalde/jupyter_ssh",
     license="MIT",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
     ],
     install_requires=["fabric"],
 )
