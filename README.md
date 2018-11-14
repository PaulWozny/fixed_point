### Fixed Point group
---
Main object of this group is to upgrade existing MyHDL module version 0.9 to a new version 0.10 in order to test properties of fixed point matrix multiplication.
Addidionaly, we would like to extend existing tutorial base  to quickstart beginners.

#### QuickStart guide
Go to *tutorial_[yourOS].md* and follow the instruction to install MyHDL on your computer.
In order to install fixed_point module you have to navigate to its direcory and run following command:
> sudo python3 setup.py install
---
Current state of work:
Eggs are compiled, woring on ToDo's left by previous contributor.
---

### Problems, Progress & Notes
- Problem with WFormat (incompatibile syntax of py2.7)
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
- Wformat previously handled __mul__ while keep 2 sign bits, and one was then counted as a iwl due to bad arithmetic. Main problem of 12.11.18
  previous handling left/commented out just in case/as an artifact  
      - Test bench for wformat modified to reflect this change
      - !@!Comments in code seem to hint that negative numbers are not handled for multiplication!@!  
              - This is further proven by sign bit handling (keeping 2 sign bits seems lazy and likely means original creator ignored them in wformat __mul__).
- Other fixes to obvious syntax errors (due to 3.6 port or previous user error)  
      - New build of fixed_point (new egg) included in current package (12.11.18)
  




---
#### Fixed point arithmetic
- quick description of what fixed point actually is
- ----||--- marix multiplication
- methods of implementing

#### ToDo (12.11.2018)
- write instruction for instalation of MyHDL in ubuntu 18.04
- get acquinted with fixed point documentation
- force upgrade fixed_point module to 0.10 and create set of benches to benchmark performance

#### ToDo (19.11.2018)
- Implement hardcoded multiplication of 4x4 matrices using fixed_point
- Scale multiplication functionality to varied input parameters
- Add screenshots to tutorials for more professional experience [Windows +]

