#Installation of the environment on ubuntu
Make essential updates and upgrades beforehand:

~~~
>> sudo apt-get update

>> sudo apt-get upgrade
~~~
1.First install python using:
~~~ 
>> sudo apt-get install python3.6
~~~

2.You can install MyHDL using pip commmand:
~~~
>> pip install myhdl
~~~
or go to http://www.myhdl.org/start/installation.html for other options.

3.Installing The Python IDE, for example Pycharm: 
~~~
>> sudo snap install pycharm-community --classic
~~~
4.Essential is adding myhdl package to Project Interpreter in IDE:
 
 - Run Pycharm:
 
~~~
>>  sudo pycharm-community 
~~~

 - Create new project
 
 - Add myhdl to Project Interpreter in Pycharm:
 
~~~
File >> Settings >> Project: [name of project] >> Project Interpreter >> + Sign (Install) >> myhdl >> Install Package 
~~~
