# bCNC-launcher

bCNC launcher allows to manage different configurations of the bCNC software, this is really useful when you want to control more than one CNC machine with the bCNC software from the same computer.

## Install bCNC software

Install (or upgrade) bCNC along with all required packages.

    pip install --upgrade 
    
For more details about installation process, see the ![bCNC installation](https://github.com/vlachoudis/bCNC/wiki/Installation) wiki page.

## Use bCNC-launcher

Download repository and install required packages:

    git clone https://github.com/AngelJMC/bCNC-launcher
    cd bCNC-launcher
    pip install -r requirements.txt

Execute **bCNC-launcher**

    python main.py

![Application](/doc/app-main.png)



### How it works?

The bCNC configuration file is saved in your home directory **${HOME}/.bCNC**  or **~/.bCNC**. bCNC-launcher modifies this configuration file using the parameters specified in the profile configuration file before running the bCNC program. 

The configuration profiles must be located in the directory **./profiles** and have the extension **.ini**. You can create as many configuration profiles as you wish. It is important that the configuration profiles maintain the same layout in terms of section names and options as the default configuration file. 

For example, if you only want to modify the dimensions of the workspace, the configuration profile would be:

    [CNC]
    travel_x = 100.0
    travel_y = 100.0
    travel_z = 50.0




## Icons source
    
[CNC Machine](https://icons8.com/icon/1545/cnc-machine) and [Play](https://icons8.com/icon/GwYlS5m5Goz6/play) icons by [Icons8](https://icons8.com)



