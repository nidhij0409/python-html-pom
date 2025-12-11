Python Selenium Automation Framework – Demoblaze (POM + PyTest + HTML Reports)

This project is a complete end-to-end automation framework built using Python, Selenium WebDriver, PyTest, and Page Object Model (POM).
It automates an e-commerce purchase flow on https://www.demoblaze.com/
 including:
✔ Navigating product categories
✔ Selecting a product
✔ Adding to cart
✔ Handling modals/alerts
✔ Cart validation
✔ Placing order
✔ Generating HTML reports

🚀 Tech Stack
Languages: Python
Automation: Selenium WebDriver
Test Runner: PyTest
Design Pattern: Page Object Model (POM)
Reports: PyTest-HTML (self-contained HTML)
Utilities: WebDriverWait, Expected Conditions

project/
├── pages/                 # Page Object Model classes
│   └── demoblaze_page.py
├── tests/                 # Test cases
│   └── test_demoblaze_flow.py
├── reports/               # Auto-generated HTML reports
├── lib.py                 # WebDriver setup + common utilities
├── conftest.py            # PyTest fixtures (driver setup, reports config)
├── pytest.ini             # PyTest configuration
└── README.md              # Project documentation

🧪 Test Scenario Automated
The framework automates the following end-to-end scenario:
1️⃣ Open Demoblaze homepage
2️⃣ Navigate to Monitors category
3️⃣ Click Asus Full HD
4️⃣ Add to cart
5️⃣ Validate "Product added" modal + click OK
6️⃣ Navigate to cart
7️⃣ Validate product name

▶️ How to Run the Tests
1. Install required dependencies
pip install -r requirements.txt
2. Run with HTML report
pytest -v --html=reports/demoblaze_report.html --self-contained-html
After run, open the report:
reports/demoblaze_report.html
8️⃣ Click Place Order
9️⃣ Fill user details in the order form
🔟 Click Purchase
