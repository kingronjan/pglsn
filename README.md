# pglsn
A PostgreSQL LSN converter, capable of transforming LSNs into numerical formats and converting numbers back into LSN strings.


# Usage

Usage: python pglsn.py [lsn] ...

Transfer string lsn to int, for example `5/559D8D30` will display `22911225136`,
otherwise if int value was gaven, a string will be displayed, for example `22911225136` will display `5/559D8D30`.

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
