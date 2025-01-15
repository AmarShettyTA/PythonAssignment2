import pytest

from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.read_properties import get_url, get_username, get_password

login_url = get_url()
username = get_username()
password = get_password()


@pytest.mark.parametrize("salutation, first_name, last_name, company", [("Mr.", "Levi", "Ackerman", "AOT")])
def test_user_creates_lead_and_validates(setup, salutation, first_name, last_name, company):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    login_page.open_login_page(login_url)
    login_page.enter_username(username=username)
    login_page.enter_password(password=password)
    login_page.click_login()

    home_page.is_on_homepage()
    home_page.clicks_sales_tab()
    home_page.clicks_leads_dropdown()
    home_page.creates_new_lead(salutation, first_name, last_name, company)
    home_page.validate_lead_created(salutation, first_name, last_name)
    home_page.convert_lead()
    home_page.clicks_go_to_leads()

    home_page.clicks_contacts_dropdown()
    name = first_name + " " + last_name
    home_page.validate_contact(name)
    home_page.clicks_accounts_dropdown()
    home_page.validate_account(company)


@pytest.mark.parametrize("account_name, salutation, first_name, last_name", [("Hogwarts", "Mr.", "Dumble", "Dore")])
def test_user_cretaes_account(setup, account_name, salutation, first_name, last_name):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)
    login_page.open_login_page(login_url)
    login_page.enter_username(username=username)
    login_page.enter_password(password=password)
    login_page.click_login()

    home_page.is_on_homepage()
    home_page.clicks_sales_tab()
    home_page.clicks_accounts_dropdown()

    home_page.create_account(account_name)
    home_page.validate_account_created(account_name)
    home_page.create_contact_from_account(account_name, salutation, first_name, last_name)
    home_page.validate_contact_created(account_name, first_name, last_name)
