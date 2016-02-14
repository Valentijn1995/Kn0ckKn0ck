# Kn0ckKn0ck - Stress testing tool
Kn0ckKn0ck is a stress testing tool which can launch different types of Denial of Service attacks against a given target (for ethical purposes of course). Kn0ckK0ck is a personal project. I started the project because I wanted to learn more about Python, the HTTP protocol, Proxies and the effectiveness of different types of Denial of Service attacks. I will try to implement new features and improve existing one's when I have some spare time on my hands.

## Features
* TCP and Http attacks
* Support for running attack through multiple http proxies
* Kn0ckKn0ck supports Basic authentication with proxies
* Runs on default python 2.7 installation

## Features to come
* SYN and half-http attacks
* Support for Socks proxies
* Amplification attacks (DNS and NTP)
* DDOS feature (launch a coordinated attack)
* IPv6 router advertisements DOS attack as explained by Sam Bowne on his Defcon 19 talk (https://www.youtube.com/watch?v=1EAnjZqXK9E).
* Graphical front-end
* Digest support for http proxy (only basic is supported now)

# Installation
* Download the latest release
* Run the following command to execute the unit tests:
```
python Kn0ckKn0ckTestSuite.py
```
* Run the following command to view the program help
```
python K0ckKn0ck.py -h
```
* Choose your options and use **Kn0ckKn0ck.py** to execute your attack. Example:
```
python Kn0ckKn0ck.py -a http -f Docs/Proxyfile_examples/example.csv 127.0.0.1 80
```
* Run ``` python setup.py install ``` if you want to install Kn0ckKn0ck permanently on your system and use the program in your own attack scripts. See the example scripts in de Docs folder for some examples.

# Documentation
The documentation for this project is located in the **Docs** folder. You will need to install Sphinx to build the class documentation. Run the following command to install Sphinx:
```
pip install Sphinx
```

Next, open a terminal and browse to the /Docs/Sphinx directory. From here run the following command if you have a GNU/Linux or Mac OS X system (any UNIX or UNIX-like system with Make will do):
```
make html
```
This command will build the documentation and place it in the build directory. Open the **index.html** file with your web-browser to browse the documentation.

Windows users will have to run the following command to build the documentation:
```
make.bat html
```

At the moment, only class documentation is included. I plan to add tutorials later.
# License
Kn0ckK0ck is licensed under the [MIT](LICENSE) license.
