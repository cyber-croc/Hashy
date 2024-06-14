# Hashy

![Hashy Logo](path_to_logo_image)

![Python Version](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Issues](https://img.shields.io/github/issues/zanesense/hashy)
![Stars](https://img.shields.io/github/stars/zanesense/hashy)
![Forks](https://img.shields.io/github/forks/zanesense/hashy)

Hashy is a powerful and user-friendly hash decryption tool available in both console and GUI interfaces. It supports decrypting various hash types, including MD5, SHA-1, SHA-256, SHA-384, and SHA-512. Hashy aims to simplify the process of retrieving the original string corresponding to a given hash.

## Features

✨ **Versatile Hash Decryption**: Supports MD5, SHA-1, SHA-256, SHA-384, and SHA-512.

✨ **Auto-Detection**: Automatically detects the hash type based on its length.

✨ **Console Interface**: For quick and efficient usage directly from the terminal.

✨ **Graphical User Interface (GUI)**: Built with PyQt5 for a more intuitive and user-friendly experience.

## Installation

Ensure you have Python 3.x installed. Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Usage

### Console Version

Decrypt a hash directly from the console:

```bash
python hashy.py -p <hash_value> [--md5|--sha1|--sha256|--sha384|--sha512]
```

**Example:**
```bash
python hashy.py -p d41d8cd98f00b204e9800998ecf8427e --md5
```

If no hash type is specified, Hashy will attempt to auto-detect it based on the hash length.

### GUI Version

Launch the GUI version for a more interactive experience:

```bash
python hashy-gui.py
```

**Steps:**

1. Enter the hash value.
2. Select the hash type or enable auto-detection.
3. Click the "Decrypt" button to retrieve the original string.

## Screenshots

### Console Version
![Console Screenshot](path_to_console_screenshot)

### GUI Version
![GUI Screenshot](path_to_gui_screenshot)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For issues, contributions, or feedback, please reach out via [GitHub](https://github.com/zanesense/hashy).

---

### Acknowledgements

Special thanks to the developers and contributors who have made this project possible. Your support and contributions are greatly appreciated.

---

### Support

If you find Hashy useful, consider giving it a ⭐ on [GitHub](https://github.com/zanesense/hashy). Your support helps us to keep improving and maintaining the project.

---

![Footer Logo](path_to_footer_logo)
