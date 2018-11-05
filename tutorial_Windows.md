#__Installation of the enviroment on Windows__
Instructions for MyHDL installation on Windows:

1. Download and install newest version of python for Windows (3.7.1 as of last tutorial update):
~~~
>> https://www.python.org/downloads/release/python-371/
~~~

2. Setup PATH variable to Python install directory (possibly done during Python installation):
~~~
>> System Properties >> Enviroment Variables >> Path >> Edit >> New
>> Type in %PYTHONPATH% from AppData
~~~

3. Download MyHDL package version 0.10:
~~~
>> https://github.com/myhdl/myhdl
>> Clone or download >> Download
~~~

4. Install MyHDL package: 
~~~
>> %MyHDL_PATH%/myhdl/test/core >> python setup.py install
~~~

5. Install a Python IDE, recommended one is PyCharm:
~~~
>> https://www.jetbrains.com/pycharm/download/#section=windows
~~~

6. Add MyHDL to Project Interpreter in IDE.