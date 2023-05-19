# ENC Tool
A Python command-line too encrypt and decrypt your data securely.
<br><br>

# Installation
## Easy way
```shell
pip install enc-tool
```

## Hard way
- Clone the project
``` shell
git clone https://github.com/errornight/enc-tool.git
```
``` shell
cd enc-tool
```

- Install 
``` shell
python setup.py install
```
or
``` shell
pip install .
```

<br>

# Usage
- To encrypt a short message
``` shell
enc "THE-MESSAGE" -p PASSWORD
```
- To save the encrypted data **in a file**
``` shell
enc "THE-MESSAGE" -p PASSWORD -s WHERE-TO-SAVE
```
- To encrypt data **from a file**
``` shell
enc -p PASSWORD -f FILE-TO-ENCRYPT -s WHERE-TO-SAVE
```
- For decryption add **-d** to your command
```shell
enc -d -f FILE-TO-DECRYPT -p PASSWORD -S WHERE-TO-SAVE
```


<br>

# Where is **ENC-Tool** Useful?
- **Secure Communication:** Use ENC-Tool to encrypt sensitive messages or data before sending them through insecure channels.
- **Data Protection:** Safeguard confidential data such as passwords, credit card numbers, or personal information by encrypting it using ENC-Tool.
- **File Encryption:** Encrypt files containing important documents, private records, or sensitive information to prevent unauthorized access.<br>

*Remember that in this version you can not encrypt files like images, But you can encrypt the text data in text files.*
<br><br>

# Contributing
Open a pull request and let me know what you think :)