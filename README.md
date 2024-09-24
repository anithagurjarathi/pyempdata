# Employee Management Chain Script

This project is a Python script that processes employee data from an input file (`ldap_output.txt`) and prints out the management chain for each active employee.

## Project Structure

- `parse_ldap.py`: The main Python script containing the logic to parse the employee data and output the management chains.
- `ldap_output.txt`: The input file containing employee data in a specific format.

## How It Works

The script performs the following steps:
1. Parses the employee data from `ldap_output.txt`.
2. Creates `Employee` objects for each entry in the file.
3. Assigns managers to each employee based on the data.
4. Prints out the management chain for each active employee.

## How to Run

To run the script, make sure you have Python3 installed, then execute the following command:

```bash
python3 parse_ldap.py ldap_output.txt
