## Vessel stay behavior detection

Detect ship stay behavior from [open-source](https://web.ais.dk/aisdata/) ship trajectory data. 

## Table of Contents

- [Research Information](#-Reseach-Information)
- [Folder Structure](#-Folder-Structure)
- [How to Reproduce](#-How-to-Reproduce)
- [Contacts](#%EF%B8%8F-contacts)

## 📌 Research Information  

- **📖 Research Project**  
  - **Title**: *A Research of detecting ship stay behavior from trajectory data*
  - **👨‍🔬 Authors**: Shunqiang Xu (ORCID: [0009-0000-0351-4312](https://orcid.org/0009-0000-0351-4312))  
  - **🏛️ Affiliation**: University of Twente, Faculty of Behavioural, Management and Social Sciences, Department of Learning, Data analytics and Technology
  - **📄 Article DOI**: [https://doi.org/10.1016/j.oceaneng.2025.121023](https://doi.org/10.1016/j.oceaneng.2025.121023)

## 📂 Folder Structure

| 📁 Folder    | 📄 File            | 📝 Description                                       |
| ----------- | ----------------- | --------------------------------------------------- |
| **data/**   | `cleaned_ais.pkl` | Input data                                          |
| **src/**    | `main.py`         | Python script  to generate output                   |
| **output/** | `output.png`      | Research output of the ship stay behavior detection |



## 📝 How to Reproduce

To reproduce the results, follow these steps:

```
# Ensure python intepretor is installed
The version Python 3.10 is used in this algorithm. Beyond versions are also compatible.

# Ensure Git is installed
# Visit https://git-scm.com to download and install console Git if not already installed.

# Clone the repository
git clone https://github.com/UT-shunqiang/Detect_Ship_Stay.git

# Navigate to the project directory
cd Detect_Ship_Stay

# Create vitual environment. "-3.10" can be replaced by the version of installed Python intepretor
python -3.10 -m venv myenv # myenv is env name

# Activate the environment
myenv/Scripts/activate

# install dependecies
pip install -r requirements.txt

# Navigate to the source code directory
cd src

# run the main.py
python main.py
```



## 🗨️ Contacts

For more details about the project, feel free to reach out to me. I am here to provide support and answer any questions you may have. Below are the best ways to contact:

- **Email**: Send your inquiries or support requests at [s.xu-1@utwente.nl](mailto:s.xu-1@utwente.nl).

Connect to my LinkedIn:

[![LinkedIn](https://img.shields.io/badge/subscribe-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTIwLjQ0NyAyMC40NTJoLTMuNTU0di01LjU2OWMwLTEuMzI4LS4wMjctMy4wMzctMS44NTItMy4wMzctMS44NTMgMC0yLjEzNiAxLjQ0NS0yLjEzNiAyLjkzOXY1LjY2N0g5LjM1MVY5aDMuNDE0djEuNTYxaC4wNDZjLjQ3Ny0uOSAxLjYzNy0xLjg1IDMuMzctMS44NSAzLjYwMSAwIDQuMjY3IDIuMzcgNC4yNjcgNS40NTV2Ni4yODZ6TTUuMzM3IDcuNDMzYTIuMDYyIDIuMDYyIDAgMCAxLTIuMDYzLTIuMDY1IDIuMDY0IDIuMDY0IDAgMSAxIDIuMDYzIDIuMDY1em0xLjc4MiAxMy4wMTlIMy41NTVWOWgzLjU2NHYxMS40NTJ6TTIyLjIyNSAwSDEuNzcxQy43OTIgMCAwIC43NzQgMCAxLjcyOXYyMC41NDJDMCAyMy4yMjcuNzkyIDI0IDEuNzcxIDI0aDIwLjQ1MUMyMy4yIDI0IDI0IDIzLjIyNyAyNCAyMi4yNzFWMS43MjlDMjQgLjc3NCAyMy4yIDAgMjIuMjIyIDBoLjAwM3oiIGZpbGw9IiMwQTY2QzIiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO3N0cm9rZS13aWR0aDouMDIwOTI0MSIgZD0iTTQuOTE3IDcuMzc3YTIuMDUyIDIuMDUyIDAgMCAxLS4yNC0zLjk0OWMxLjEyNS0uMzg0IDIuMzM5LjI3NCAyLjY1IDEuNDM3LjA2OC4yNS4wNjguNzY3LjAwMSAxLjAxYTIuMDg5IDIuMDg5IDAgMCAxLTEuNjIgMS41MSAyLjMzNCAyLjMzNCAwIDAgMS0uNzktLjAwOHoiLz48cGF0aCBzdHlsZT0iZmlsbDojZmZmO3N0cm9rZS13aWR0aDouMDIwOTI0MSIgZD0iTTQuOTE3IDcuMzc3YTIuMDU2IDIuMDU2IDAgMCAxLTEuNTItMi42NyAyLjA0NyAyLjA0NyAwIDAgMSAzLjQxOS0uNzU2Yy4yNC4yNTQuNDIuNTczLjUxMi45MDguMDY1LjI0LjA2NS43OCAwIDEuMDItLjA1MS4xODYtLjE5Ny41MDQtLjMuNjUyLS4wOS4xMzItLjMxLjM2Mi0uNDQzLjQ2NC0uNDYzLjM1Ny0xLjEuNTAzLTEuNjY4LjM4MlpNMy41NTcgMTQuNzJWOS4wMDhoMy41NTd2MTEuNDI0SDMuNTU3Wk05LjM1MyAxNC43MlY5LjAwOGgzLjQxMXYuNzg1YzAgLjYxNC4wMDUuNzg0LjAyNi43ODMuMDE0IDAgLjA3LS4wNzMuMTI0LS4xNjIuNTI0LS44NjUgMS41MDgtMS40NzggMi42NS0xLjY1LjI3NS0uMDQyIDEtLjA0NyAxLjMzMi0uMDA5Ljc5LjA5IDEuNDUxLjMxNiAxLjk0LjY2NC4yMi4xNTcuNTU3LjQ5My43MTQuNzEzLjQyLjU5Mi42OSAxLjQxMi44MDggMi40NjQuMDc0LjY2My4wODQgMS4yMTUuMDg1IDQuNTc4djMuMjU4aC0zLjUzNnYtMi45ODZjMC0yLjk3LS4wMS0zLjQ3NC0uMDc0LTMuOTA4LS4wOS0uNjA2LS4zMTQtMS4wODItLjYzNC0xLjM0Mi0uMzk1LS4zMjItMS4wMjktLjQzNy0xLjcwMy0uMzA5LS44NTguMTYzLTEuMzU1Ljc1LTEuNTIzIDEuNzk3LS4wNzYuNDcxLS4wODQuODQ1LS4wODQgMy44MzR2Mi45MTRIOS4zNTN6Ii8+PC9zdmc+)](https://www.linkedin.com/in/shunqiang-xu-87787a331/)

### :star: Give a Star! 

Support this research by **giving it a star** — It motivates me a lot! Thanks!
