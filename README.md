### Fixed Point group
---
Main object of this group is to upgrade existing MyHDL module version 0.9 to a new version 0.10 in order to test properties of fixed point matrix multiplication.
Addidionaly, we would like to extend existing tutorial base  to quickstart beginners.

#### QuickStart guide
Go to *tutorial_[yourOS].md* and follow the instruction to install MyHDL on your computer.


---
In order to install fixed_point module you have to navigate to its direcory and run following command:
> sudo python2.7 setup.py install

current state of work:
- fixed_numbers module is written for py2.7
- myhdl is written for py3.6
- 2to3 tool doesn't provide ready-to-use code
---

### Problems xd
- Problem with WFormat (incompatibile syntax of py2.7
quick workaroud:
    - change sys libraries -> recompile to egg or
    - import local module 
- Problem with async in new python (myhdl/test/core functions)
- Build from current files into new egg to fix old python version compatibility issues via:
    - Remove current build 
    `>> sudo python3.6 setup.py install`
    - Use in *fixed_point* library
    - Old build supplied in repository is outdated  
-  Workaround for building eggs after each debuf process:
    `>> python setup.py develop`





---
#### Fixed point arithmetic
- quick description of what fixed point actually is
- ----||--- marix multiplication
- methods of implementing


#### ToDo (12.11.2018)
- write instruction for instalation of MyHDL in ubuntu 18.04
- get acquinted with fixed point documentation
- force upgrade fixed_point module to 0.10 and create set of benches to benchmark performance
---
- write readme in concise manner
- lubie placki

#### ToDo (19.11.2018)
- Implement hardcoded multiplication of 4x4 matrices using fixed_point
- Scale multiplication functionality to varied input parameters
- Add screenshots to tutorials for more professional experience