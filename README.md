# MTLT - Make This Like That

_MTLT is a parser for firewall config files._

## Installation

```bash
> git clone git@github.corp.ebay.com:NetDev/MTLT.git
> virtualenv venv36 -p <path to python36>
> source venv36/bin/activate
> pip install -r requirements.txt
> python setup.py install
```

## Running Tests

```bash
> git clone git@github.corp.ebay.com:NetDev/MTLT.git
> virtualenv venv36 -p <path to python36>
> source venv36/bin/activate
> pip install -r requirements.txt
> tox
```

## Basic Usage

Most execution is done via the mtlt driver script.

```bash
> mtlt <this> <that> --ticket=<SECUR #>
```

## Other Usage

```bash
> python mtlt/parser.py --file=conf/ais-hd-02.lvs.netsec.ebay.com find-objects-w-child '' '10.29.66.0'
> python mtlt/parser.py --file=conf/ais-hd-02.lvs.netsec.ebay.com find-objects-w-child '' '10.29.*.0'
> python mtlt/parser.py --file=conf/ais-hd-02.lvs.netsec.ebay.com find-objects '10.241.15.22'
```
