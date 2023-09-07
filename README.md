# Bitcoin Value

A Python module to fetch the latest value of Bitcoin in different currencies.

[![PyPi Version](https://img.shields.io/pypi/v/bitcoin-value.svg)](https://pypi.org/project/bitcoin-value/)
[![MIT License](https://img.shields.io/pypi/l/bitcoin-value.svg)](https://github.com/dewittethomas/bitcoin-value/blob/master/LICENSE)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Getting Bitcoin Value](#getting-bitcoin-value)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install the `bitcoin-value` module using pip:

```bash
pip install bitcoin-value
```

## Usage

### Getting Bitcoin Value

You can use this module to get the current value of Bitcoin in various currencies. Here's an example of how to use it:

```python
from bitcoin_value import currency

# Specify the currency code (e.g., "USD", "EUR")
bitcoin_value = currency("USD")

# Print the Bitcoin value in the specified currency
print(f"1 BTC is equivalent to {bitcoin_value} USD")
```

## Contributing

Contributions to this project are welcome. If you have any improvements or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License.