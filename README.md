# Karnaugh mapper

This program simplifies boolean expressions using the k-map method.

* The result will be in sop (sum of products) form

* Simplifies Boolean expressions for up to four variables

* Assume the variables on the map are in alphabetical order starting with the rows first, and then the columns

  * A four variable map would use AB for the rows and CD for the columns

# Command line arguments

Two arguments are required:

  1. **--variable_count** (use -n to be followed by the amount of variables)

  2. **--minterms** (use -m to be followed by minterm values)

_**Example**_

For a 3 variable map with minterm values of 0, 1, and 2:

```
$ python3 kmapper.py -n 3 -m 0 1 2
```
