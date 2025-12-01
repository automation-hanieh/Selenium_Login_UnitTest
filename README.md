# Selenium Login Automation (Python + Unittest)

This project is a simple automation framework built using **Python**, **Selenium WebDriver**, and **Unittest**. It contains:

* A valid login test
* An invalid login test
* Page Object Model (POM) structure
* Locators stored in a separate file
* HTML test report

##  Project Structure

```
├── Tests/
│   └── LoginTest.py
├── Pages/
│   ├── Login.py
│   └── MainPage.py
├── Locators/
│   └── locators.py
├── reports/
│   └── test_result.html 
└── README.md
```


##  Test Scenarios

###  Valid Login

* Opens the SauceDemo website
* Enters correct username and password
* Verifies that user lands on the main page

###  Invalid Login

* Opens the SauceDemo website
* Enters incorrect password
* Verifies login error (to be implemented)

##  Technologies Used

* Python 3
* Selenium WebDriver
* Unittest framework
* WebDriver Manager
