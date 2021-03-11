# bitcoin_value

[![npm](https://img.shields.io/pypi/v/bitcoin-value.svg)](https://pypi.org/project/bitcoin-value/)

A tracker that gets the latest value of Bitcoin in any of these currencies:

- AED
- AFN
- ALL
- AMD
- ANG
- AOA
- ARS
- AUD
- AWG
- AZN
- BAM
- BBD
- BDT
- BGN
- BHD
- BIF
- BMD
- BND
- BOB
- BRL
- BSD
- BTC
- BTN
- BWP
- BYR
- BZD
- CAD
- CDF
- CHF
- CLF
- CLP
- CNY
- COP
- CRC
- CUP
- CVE
- CZK
- DJF
- DKK
- DOP
- DZD
- EEK
- EGP
- ERN
- ETB
- EUR
- FJD
- FKP
- GBP
- GEL
- GHS
- GIP
- GMD
- GNF
- GTQ
- GYD
- HKD
- HNL
- HRK
- HTG
- HUF
- IDR
- ILS
- INR
- IQD
- IRR
- ISK
- JEP
- JMD
- JOD
- JPY
- KES
- KGS
- KHR
- KMF
- KPW
- KRW
- KWD
- KYD
- KZT
- LAK
- LBP
- LKR
- LRD
- LSL
- LTL
- LVL
- LYD
- MAD
- MDL
- MGA
- MKD
- MMK
- MNT
- MOP
- MRO
- MTL
- MUR
- MVR
- MWK
- MXN
- MYR
- MZN
- NAD
- NGN
- NIO
- NOK
- NPR
- NZD
- OMR
- PAB
- PEN
- PGK
- PHP
- PKR
- PLN
- PYG
- QAR
- RON
- RSD
- RUB
- RWF
- SAR
- SBD
- SCR
- SDG
- SEK
- SGD
- SHP
- SLL
- SOS
- SRD
- STD
- SVC
- SYP
- SZL
- THB
- TJS
- TMT
- TND
- TOP
- TRY
- TTD
- TWD
- TZS
- UAH
- UGX
- USD
- UYU
- UZS
- VEF
- VND
- VUV
- WST
- XAF
- XAG
- XAU
- XBT
- XCD
- XDR
- XOF
- XPF
- YER
- ZAR
- ZMK
- ZMW
- ZW

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