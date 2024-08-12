# Simple Port Scanner

Simple Python script allows you to discover open, closed, or filtered ports on a target system.

## Prerequisites

No need for additional installations.

## Usage

1. Clone repo on your local machine and switch to script folder.

   ```bash
   git clone https://github.com/HASHKS1/PythonS.git
   cd port-scanner
   ```

2. Run the script

   ```bash
   python3 portScanner.py
   ```

3. You will be prompted to enter the host name of the target, and to specify the start and end port numbers.

    Exemple: 

   ```bash
    Enter the hostname to be scanned: wiki.com
    Enter the starting port: 10  
    Enter the ending port: 100
   ```

4. The script will scan the specified ports and display the results.

   ```bash
    Start Scanning ports on 66.96.149.1...
    Port 80 is open
    Time taken: 93.05869174003601
   ```