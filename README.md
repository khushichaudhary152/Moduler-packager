# 📦 ✦ **MODULER-PACKAGER** ✦ ⚙️

### 🐍 `MODULES` • `PACKAGES` • `BUILT-IN LIBRARIES`

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Modules](https://img.shields.io/badge/Modules-Enabled-8A2BE2?style=for-the-badge&logo=python&logoColor=white)](#)
[![Packages](https://img.shields.io/badge/Packages-Custom-FF69B4?style=for-the-badge&logo=python&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Completed-00C853?style=for-the-badge&logo=checkmarx&logoColor=white)](#)

<br>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2500&pause=800&color=58A6FF&center=true&vCenter=true&width=650&lines=Welcome+to+Moduler-Packager+%F0%9F%93%A6;Python+Modules+%E2%9A%99%EF%B8%8F;Custom+Packages+%F0%9F%93%81;Multi-Utility+Toolkit+%F0%9F%90%8D" alt="Typing Animation">

<br>

`⚡ Python` • `🧩 Utilities` • `📁 File Handling` • `🆔 UUID` • `🎲 Random` • `🧮 Math`

</div>

---

## 🚀 About The Project

**Moduler-Packager** is a Python-based **Multi-Utility Toolkit** created to demonstrate the practical use of Python modules, packages, built-in libraries, custom modules, and file handling.

It provides an interactive **menu-driven interface** where different utilities can be accessed from a single program.

---

## ✨ Features

| 🔢 | Feature |
|:---:|---|
| 🕒 | Datetime & Time Operations |
| 🧮 | Mathematical Operations |
| 🎲 | Random Data Generation |
| 🆔 | UUID Generation |
| 📁 | File Operations using Custom Module |
| 🔍 | Module Attribute Exploration using `dir()` |
| 🚪 | Exit |

---

## 🛠️ Technologies & Concepts

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Datetime](https://img.shields.io/badge/Datetime-Module-4CAF50?style=flat-square)
![Math](https://img.shields.io/badge/Math-Module-FF9800?style=flat-square)
![Random](https://img.shields.io/badge/Random-Module-9C27B0?style=flat-square)
![UUID](https://img.shields.io/badge/UUID-Module-E91E63?style=flat-square)
![File Handling](https://img.shields.io/badge/File-Handling-795548?style=flat-square)
![Packages](https://img.shields.io/badge/Custom-Package-00BCD4?style=flat-square)

</p>

---

## 📂 Project Structure

```text
📦 Moduler-Packager
│
├── 🐍 main.py
├── 📅 datetime_utils.py
├── 🧮 math_utils.py
├── 🎲 random_utils.py
├── 🆔 uuid_utils.py
│
└── 📁 utilities
    ├── 📦 __init__.py
    ├── 📄 file_operations.py
    └── 🧮 math_operations.py
```

## 📊 PROGRAM FLOW

```mermaid
flowchart TD

    A([🚀 START]) --> B[📋 Display Main Menu]
    B --> C{🔍 Choose Option}

    C -->|1| D[🕒 Datetime & Time Operations]
    C -->|2| E[🧮 Mathematical Operations]
    C -->|3| F[🎲 Random Data Generation]
    C -->|4| G[🆔 Generate Unique Identifier UUID]
    C -->|5| H[📁 File Operations]
    C -->|6| I[🔎 Explore Module Attributes using dir]
    C -->|7| J([🚪 EXIT])

    D --> D1[📅 Current Date & Time]
    D1 --> B

    E --> E1[√ Square Root]
    E1 --> E2[⚡ Power]
    E2 --> E3[🔢 Factorial]
    E3 --> B

    F --> F1[🎯 Enter Start & End]
    F1 --> F2[🎲 Generate Random Number]
    F2 --> B

    G --> G1[🔐 Generate UUID4]
    G1 --> B

    H --> H1{📂 File Choice}
    H1 -->|1| H2[📝 Create File]
    H1 -->|2| H3[✍️ Write File]
    H1 -->|3| H4[📖 Read File]
    H1 -->|4| H5[➕ Append File]

    H2 --> B
    H3 --> B
    H4 --> B
    H5 --> B

    I --> I1[📦 Datetime Module]
    I1 --> I2[📦 Math Module]
    I2 --> I3[📦 Random Module]
    I3 --> I4[📦 UUID Module]
    I4 --> B

    J --> K([🎉 PROGRAM END])

    style A fill:#00C853,stroke:#006B2E,color:#fff,stroke-width:3px
    style B fill:#2196F3,stroke:#0D47A1,color:#fff,stroke-width:3px
    style C fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:3px
    style D fill:#7E57C2,stroke:#4527A0,color:#fff
    style E fill:#E91E63,stroke:#880E4F,color:#fff
    style F fill:#00ACC1,stroke:#006064,color:#fff
    style G fill:#5C6BC0,stroke:#283593,color:#fff
    style H fill:#8D6E63,stroke:#4E342E,color:#fff
    style I fill:#26A69A,stroke:#00695C,color:#fff
    style J fill:#F44336,stroke:#B71C1C,color:#fff,stroke-width:3px
    style K fill:#607D8B,stroke:#263238,color:#fff,stroke-width:3px
```


## 📤 SAMPLE OUTPUT

```mermaid
flowchart TD

    A([🚀 Run Program]) --> B[📋 Welcome to Multi-Utility Toolkit]
    B --> C[Display Main Menu]
    C --> D{Choose Option}

    D -->|Choice 1| E[🕒 Datetime Operations]
    E --> E1["Current Date and Time:<br>2026-10-16 14:15:30"]
    E1 --> C

    D -->|Choice 2| F[🧮 Mathematical Operations]
    F --> F1["Enter a number: 6"]
    F1 --> F2["Square Root: 2.449489742783178<br>Power: 36.0<br>Factorial: 720"]
    F2 --> C

    D -->|Choice 3| G[🎲 Random Data Generation]
    G --> G1["Enter starting number: 1<br>Enter ending number: 100"]
    G1 --> G2["Random Number: 68"]
    G2 --> C

    D -->|Choice 4| H[🆔 Generate Unique Identifier UUID]
    H --> H1["Generated UUID:<br>550e8400-e29b-41d4-a716-446655440000"]
    H1 --> C

    D -->|Choice 5| I[📁 File Operations]
    I --> I1{Choose File Operation}

    I1 -->|Create File| I2["Enter filename: test.txt<br>File created successfully."]
    I2 --> I3["Write File<br>Enter content: hello python<br>Data written successfully."]
    I3 --> I4["Read File<br>File Content:<br>hello python"]
    I4 --> I5["Append File<br>Enter content to append:<br>Welcome toolkit<br>Data appended successfully."]
    I5 --> C

    D -->|Choice 6| J[🔍 Explore Module Attributes]
    J --> J1["Datetime Module: dir(datetime)<br>Math Module: dir(math)<br>Random Module: dir(random)<br>UUID Module: dir(uuid)"]
    J1 --> C

    D -->|Choice 7| K([🚪 Exit])
    K --> L([🎉 Thank You for using Multi-Utility Toolkit])

    style A fill:#00C853,stroke:#006B2E,color:#fff,stroke-width:3px
    style B fill:#2196F3,stroke:#0D47A1,color:#fff,stroke-width:3px
    style C fill:#42A5F5,stroke:#1565C0,color:#fff,stroke-width:3px
    style D fill:#FF9800,stroke:#E65100,color:#fff,stroke-width:3px

    style E fill:#7E57C2,stroke:#4527A0,color:#fff
    style F fill:#E91E63,stroke:#880E4F,color:#fff
    style G fill:#00ACC1,stroke:#006064,color:#fff
    style H fill:#5C6BC0,stroke:#283593,color:#fff
    style I fill:#8D6E63,stroke:#4E342E,color:#fff
    style J fill:#26A69A,stroke:#00695C,color:#fff
    style K fill:#F44336,stroke:#B71C1C,color:#fff,stroke-width:3px
    style L fill:#607D8B,stroke:#263238,color:#fff,stroke-width:3px

    style E1 fill:#EDE7F6,stroke:#7E57C2
    style F1 fill:#FCE4EC,stroke:#E91E63
    style F2 fill:#FCE4EC,stroke:#E91E63
    style G1 fill:#E0F7FA,stroke:#00ACC1
    style G2 fill:#E0F7FA,stroke:#00ACC1
    style H1 fill:#E8EAF6,stroke:#5C6BC0
    style I1 fill:#EFEBE9,stroke:#8D6E63
    style I2 fill:#EFEBE9,stroke:#8D6E63
    style I3 fill:#EFEBE9,stroke:#8D6E63
    style I4 fill:#EFEBE9,stroke:#8D6E63
    style I5 fill:#EFEBE9,stroke:#8D6E63
    style J1 fill:#E0F2F1,stroke:#26A69A
```


## 🧠 CONCEPTS DEMONSTRATED

| Concept | Purpose |
|---|---|
| 📦 Modules | Use built-in and custom Python modules |
| 📁 Packages | Organize modules inside the `utilities` package |
| ⚙️ Functions | Create reusable program operations |
| 🔀 Conditional Statements | Handle different menu choices |
| 🔁 Loops | Keep the menu running until Exit |
| 📄 File Handling | Create, write, read and append files |
| 🎲 Random Module | Generate random numbers |
| 🆔 UUID Module | Generate unique identifiers |
| 🕒 Datetime Module | Work with date and time |
| 🧮 Math Module | Perform mathematical calculations |
| 🔍 `dir()` | Explore module attributes |
| 🖥️ Menu-Driven Program | Provide an interactive user interface |

    

    

    

## 📸 SCREENSHOTS & 🎥 DEMO VIDEO

### 📸 Project Screenshots
<img width="1920" height="4662" alt="op ss 7" src="https://github.com/user-attachments/assets/180f1481-7668-4808-a1fd-37e87b0c9d11" />


### 🎥 Demo Video





## 👩‍💻 AUTHOR

<div align="center">

### ✨ Khushi Chaudhary ✨

🐍 Python Developer | 📦 Module & Package Explorer

**Project:** `Moduler-Packager`

</div>

---

## 🌟 THANK YOU

<div align="center">

### 💙 Thank you for visiting my project!

⭐ If you found this project useful, consider giving it a **Star**!

🐍 **Built with Python**  
📦 **Modules • Packages • Functions • File Handling**

<br>



</div>



    
