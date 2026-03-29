# XSS Payload Generator

## 👤 Student Details

* Name: Dharshana
* Roll Number: 727823TUCY009

---

## 📌 Project Title

XSS Payload Generator

---

## 🧠 Project Description

The XSS Payload Generator is a Python-based tool designed to generate multiple Cross-Site Scripting (XSS) payloads for testing web application vulnerabilities.

Cross-Site Scripting (XSS) is a common web security vulnerability that allows attackers to inject malicious scripts into web pages viewed by users. This tool helps in identifying such vulnerabilities by providing different types of payloads.

---

## ⚙️ Tools & Technologies Used

* Python 3
* Kali Linux
* Metasploitable2
* DVWA (Damn Vulnerable Web Application)

---

## 🧪 Features

* Generates multiple XSS payloads
* Covers different attack types (script, event-based, HTML injection)
* Displays timestamp and roll number
* Easy to use and execute

---

## 🛠️ Setup Instructions

1. Clone the repository:
   git clone https://github.com/your-username/hacker-skct-727823TUCY009

2. Navigate to project folder:
   cd SKCT_727823TUCY009_XSS_Payload_Generator/code

3. Run the tool:
   python3 tool_main.py

---

## ▶️ Usage

* Run the tool to generate payloads
* Copy payloads and test in DVWA (XSS module)
* Observe alert popups to confirm vulnerability

---

## 🧪 Test Cases

| Test Case | Payload                      | Result  |
| --------- | ---------------------------- | ------- |
| 1         | <script>alert(1)</script>    | Success |
| 2         | <img src=x onerror=alert(1)> | Success |
| 3         | '><script>alert(1)</script>  | Success |

---

## 🖼️ Screenshots

Screenshots are available in the `/screenshots` folder showing:

* Tool execution
* XSS attack results
* Different payload behaviors

---

## 🔄 Pipeline Description

The project includes a pipeline with three stages:

* setup_lab.py → Initializes the environment
* run_tool.py → Executes payload generation
* analyze_results.py → Analyzes the output

---

## ⚠️ Ethical Considerations

This project was developed and tested in a controlled lab environment using Kali Linux and Metasploitable2.

No real-world systems were targeted. The project is intended only for educational and ethical hacking purposes.

---

## 📦 Requirements

* Python 3.x

---

## 📌 Summary

This tool automates the generation of XSS payloads and helps in identifying vulnerabilities in web applications, making it useful for learning and security testing.
