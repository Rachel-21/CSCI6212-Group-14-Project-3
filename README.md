## CS6212 - Group 14 - Project 3 - Longest Common Subsequence 

- Rachel Gonzalez Rodriguez - G37147365
- Srinivas Ravindranath - G22058521
- Ozgun Ozkan - G39576650 
- Esma Kokten - G48837791

This repository houses the code for our CS6212 project.

### Requirements

The script is compatible to run with **python3**. 

**Matplotlib** library is necessary:

Install directly on system:

```
pip3 install matplotlib
```

Install using virtualenv (keeps it separate from system packages):
```
pip3 install virtualenv
python3 -m venv .venv
source .venv/bin/activate 
pip3 install matplotlib
```

In case of issue on WSL or linux systems:
```
pip3 install --upgrade pip
pip3 install sip
sudo apt-get install python3-pyqt5    # for linux systems only
```

### How to run the program

Run the script only, you can change the input lengths by manuplating the **test_values** array:

```
python3 ./longest_common_subsequence.py 
```

**NOTE**: Please note that running the above code takes some time as this code is memory intensive so if the code 
looks like it's stuck, it is not stuck.  **Please do not exit if it looks stuck**.

Plots the graph and creates the 'outputs.txt'. 

