from setuptools import setup

with open("README.md", "r") as fh:
      long_description = fh.read()


print("                                                                                 ")
print("*********************************************************************************")
print("         Welcome to the PiWarsTurkeyRobotKit2019 library!")
print("         You can find the documentation at https://github.com/HisarCS/PiWarsTurkeyRobotLibrary")
print("         We recommend checking the documentation if faced with a problem. If the problem persists, don't be afraid to contact us.")
print("         Make sure that you use sudo while installing and using this library")
print("*********************************************************************************")
print("                                                                                 ")

setup(
    name = "PiWarsTurkeyRobotKit2019",
    version = "1.1.4",
    author = "Yasar İdikut, Sarp Yoel Kastro",
    author_email = "yasar.idikut@hisarschool.k12.tr, sarp.kastro@hisarschool.k12.tr",
    description = "Library that makes use of sensors, motors, and servos in the PiWars Turkey robot kit by HisarCS",
    packages = ["PiWarsTurkeyRobotKit2019"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Development Status :: 4 - Beta"],
    install_requires=[
#        'picamera',
#        'pygame',
#        'RPi.GPIO',
#        'wiringpi',
    ]

)
