# Pyciphering

##### An awesome package to text ciphering

### Installation

You can install pyciphering with **pip** as follows:

```
pip install pyciphering
```

### Usage

```python
import pyciphering
```

Printing encoded and decoded text is incredibly easy:

```python
print(pyciphering.atbash.encode("Hello world!"))

print(pyciphering.atbash.decode("ZYX"))
```

### Ciphers

#### List of all ciphers

- atbash
- caesar
- viegenere
- bifid
- trifid
- polybius