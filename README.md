# pglsn
A PostgreSQL LSN converter, capable of transforming LSNs into numerical formats and converting numbers back into LSN strings.


# Usage

You can either download the `pglsn.py` file directly or copy its content and save it locally.

Usage: `python pglsn.py [lsn] ...`

This tool converts PostgreSQL LSNs (Log Sequence Numbers) to integers and vice-versa. 
For instance, the string `5/559D8D30` becomes `22911225136`, and `22911225136` converts back to `5/559D8D30`.

## example

```shell
$ python pglsn.py 5/559D8D30
5/559D8D30: 22911225136
```

And for multiple strings or numbers:

```shell
$ python pglsn.py 5/559D8D30 5/559D8D31 22911225136
5/559D8D30: 22911225136
5/559D8D31: 22911225137
22911225136: 5/559D8D30
```
