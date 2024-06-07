# Hashy -  Hash Decrypter

## Description
This Python script is designed to identify and decrypt various hash values, including MD5, SHA-1, SHA-256, SHA-384, and SHA-512.

## Requirements
- Python 3.x
- Required Python packages:
  - os
  - sys
  - requests
  - argparse
  - huepy

You can install the required packages using:
```sh
pip install -r requirements.txt
```

## Usage
To run the script, use the following command:

```sh
python Hashy.py -p <hash_value>
```

You can also specify the hash type directly using command-line arguments:
- For MD5:
  ```sh
  python Hashy.py -p <hash_value> --md5
  ```
- For SHA-1:
  ```sh
  python Hashy.py -p <hash_value> --sha1
  ```
- For SHA-256:
  ```sh
  python Hashy.py -p <hash_value> --sha256
  ```
- For SHA-384:
  ```sh
  python Hashy.py -p <hash_value> --sha384
  ```
- For SHA-512:
  ```sh
  python Hashy.py -p <hash_value> --sha512
  ```

If no hash type is provided, the script will try to determine the hash type based on the length of the hash.

## Example
```sh
python Hashy.py -p 5d41402abc4b2a76b9719d911017c592 --md5
```

## Features
- Automatically identifies the hash type based on the length of the hash if not specified.
- Supports MD5, SHA-1, SHA-256, SHA-384, and SHA-512.
- Uses online databases to decrypt the hash.

## Notes
- Ensure you have an active internet connection as the script relies on online services to decrypt hashes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
