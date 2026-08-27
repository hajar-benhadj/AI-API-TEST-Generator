<div align="center">

# 🚀 AI API Test Generator

An automated Python-based tool that parses Swagger/OpenAPI documentation, extracts API endpoints, and automatically generates robust Pytest test cases to streamline backend testing.

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d88506d50ef.gif" width="100%"/>

<p>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pytest-0A7EDC?style=for-the-badge&logo=pytest&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black"/>
</p>

</div>

---

## ✨ Key Features

* **📊 Automated Parsing:** Seamlessly reads and parses Swagger/OpenAPI JSON files to extract all available backend API endpoints.
* **🤖 AI-Powered Scaffolding:** Utilizes AI models and structured templates to automatically generate comprehensive Pytest test cases.
* **⚡ Instant Execution:** Automatically runs the generated test suite using Pytest to validate backend functionality instantly.
* **📂 Structured Architecture:** Clean modular layout separating core logic, generated outputs, and sample configurations.

---

## 📂 Project Structure

AI-API-TEST-GENERATOR/
│
├── core/
│   ├── __init__.py          # Package initializer
│   ├── ai_generator.py      # Generates Pytest test cases using templates/AI
│   ├── executor.py          # Executes generated tests automatically via Pytest
│   └── parser.py            # Parses Swagger/OpenAPI JSON files
│
├── generated_tests/
│   └── test_generated_api.py  # Automatically generated test suite
│
├── samples/
│   └── sample_swagger.json    # Sample Swagger/OpenAPI documentation file
│
├── .gitignore                 # Specifies files and directories ignored by Git
├── requirements.txt           # Project dependencies
└── main.py                    # Main entry point of the application

---

## 🛠️ Technologies Used

* **Python 3.12** — Core programming language for logic and automation scripts.
* **Pytest** — Robust testing framework used to execute generated test suites.
* **Requests** — HTTP library for sending requests during API validation.
* **OpenAI API** — Intelligent code generation engine for automated scaffolding.

---

## 🚀 How to Run Locally

1. Clone this repository to your local machine:
   git clone https://github.com/hajar-benhadj/AI-API-TEST-GENERATOR.git
   cd AI-API-TEST-GENERATOR

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set up environment variables:
   Create a .env file in the root directory and add your OPENAI_API_KEY.

5. Run the main script to generate tests:
   python main.py

6. Execute the generated tests using Pytest:
   pytest generated_tests/test_generated_api.py -v

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⭐ Show Your Support

If this project saved you hours of writing API tests manually, please consider giving it a ⭐ — it helps other developers discover it!

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.
