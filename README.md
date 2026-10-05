# 🔐 punyCod3

**Unicode & Punycode Analysis Tool**

A lightweight security tool for encoding, decoding, and analyzing Unicode/Punycode domain names.

The project was created to explore how Unicode characters can be used in domain names and how visually similar characters may be abused in **homograph attacks, phishing, and social engineering**.

---

## ✨ Features

- 🔄 Unicode ↔ Punycode encoding and decoding
- 🔍 Analyze potentially deceptive domain names
- 🌐 Web-based interface
- 🐍 Python-based tooling
- 🛡️ Security awareness for Unicode homograph attacks

---

## 🌐 Live Demo

Try the web version:

https://ryygans.github.io/punyCod3/website/

---

## 📸 How It Works

A domain containing Unicode characters can sometimes look almost identical to a legitimate domain while internally representing different characters.

`punyCod3` helps inspect the underlying representation of these domains by converting between Unicode and Punycode.

### Example

    Unicode
    раураl.com

    ↓ Punycode

    xn--80aa0cbo.com

> The visual appearance of a domain should not always be trusted. Inspecting its underlying representation can help identify potentially deceptive domains.

---

## 📂 Project Structure

    punyCod3/
    ├── python/
    │   └── Encoding & decoding tools
    ├── website/
    │   └── Web interface
    └── README.md

---

## 🧠 Security Concepts

This project helped me explore:

- Unicode & Punycode
- Internationalized Domain Names (IDN)
- Unicode homograph attacks
- Phishing techniques
- Social engineering
- Domain analysis
- Security-focused tooling

---

## 🛠️ Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-222222?style=for-the-badge&logo=github&logoColor=white)

---

## 🎯 Project Goals

The main goals of this project are to:

- Understand how Unicode domains are represented
- Learn how Punycode encoding works
- Recognize potential homograph-based phishing domains
- Build a practical security-oriented tool
- Improve Python and web development skills

---

## ⚠️ Disclaimer

This project is intended for **educational and defensive security purposes**.

Use this tool only for domains and systems you are authorized to analyze.

Always verify the authenticity of websites before interacting with suspicious domains.

The author is not responsible for misuse of this project.

---

## 👤 Author

**GitHub:** `Ryygans`  
**Security Handle:** `zoxxtzy`

> **Build. Analyze. Learn. Secure.**
