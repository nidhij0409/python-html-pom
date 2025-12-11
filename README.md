# Python Selenium Automation Framework – Demoblaze  
### (POM + PyTest + HTML Reporting)

This project is an end-to-end automation framework built using **Python**, **Selenium WebDriver**, **PyTest**, and the **Page Object Model (POM)** design pattern.

It automates an e-commerce flow on **Demoblaze**:

✔ Navigate categories  
✔ Select a product  
✔ Add to cart  
✔ Handle alerts/modals  
✔ Validate cart  
✔ Place order  
✔ Generate HTML reports  

---

## 🚀 Tech Stack

**Languages:** Python  
**Automation:** Selenium WebDriver  
**Test Runner:** PyTest  
**Design Pattern:** Page Object Model (POM)  
**Reporting:** PyTest-HTML (self-contained HTML)  
**Utilities:** WebDriverWait, Expected Conditions  

---

## 📁 Project Structure
project/
│
├── pages/ # Page Object classes
│ └── demoblaze_page.py
│
├── tests/ # Test cases
│ └── test_demoblaze_flow.py
│
├── reports/ # Auto-generated HTML reports
│
├── lib.py # WebDriver setup + utilities
├── conftest.py # PyTest fixtures (driver setup, report config)
├── pytest.ini # PyTest configuration
└── README.md # Project documentation


---

## 🧪 Test Scenario Automated

This framework automates the following end-to-end scenario:

1️⃣ Open Demoblaze homepage  
2️⃣ Navigate to **Monitors** category  
3️⃣ Select **ASUS Full HD**  
4️⃣ Add product to cart  
5️⃣ Validate **"Product added"** alert and click OK  
6️⃣ Open cart  
7️⃣ Validate selected product  
8️⃣ Click **Place Order**  
9️⃣ Fill user details  
🔟 Complete the purchase  

---

## ▶️ How to Run the Tests
### **1. Install dependencies**
### **2. Run tests with HTML report**
After execution, open the generated report:

---

## 📸 Sample HTML Report (Screenshot Recommended)
<img width="1904" height="1073" alt="image" src="https://github.com/user-attachments/assets/f2f2e4ff-5296-4be8-b6b1-54f36dce70c5" />

---
## 💼 Author  
**Nidhi Shah**  
Automation QA Engineer | Python | Selenium | PyTest | POM  


