# bitcoin_value

[![npm](https://img.shields.io/pypi/v/bitcoin-value.svg)](https://pypi.org/project/bitcoin-value/)

A tracker that gets the latest value of Bitcoin in any currency.

## Installation

Run the following to install:

```console
pip install bitcoin-value
```

## Usage

### Currency

```python
currency()
```

Params:

```
Currency: String ? The currency of the Bitcoin.
```

Demo:

```python
from bitcoin_value import currency

cur = currency("USD")
```

### Fetch

```python
currency.fetch()
```

Result:

```
Currency: str()
```

Demo:

```python
result = currency("USD").fetch()
print(result)
```

# License
[MIT](https://github.com/dewittethomas/nationality-predictor/blob/master/LICENSE)