import time
import locators
from wrappers.wrappers import enter_using_xpath, click_using_xpath, is_element_displayed, click_using_actions_and_xpath


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def is_on_homepage(self):
        is_element_displayed(self.driver, locators.home_page_title)

    def clicks_sales_tab(self):
        click_using_xpath(self.driver, locators.nav_sales_button, "Clicked on Sales tab")

    def clicks_leads_dropdown(self):
        click_using_xpath(self.driver, locators.leads_dropdown, "Clicked on Leads dropdown")

    def creates_new_lead(self, salutation, first_name, last_name, company):
        click_using_actions_and_xpath(self.driver, locators.new_lead_button, "Clicked on new lead")
        click_using_xpath(self.driver, locators.salutations_dropdown, "Cliked on salutation dropdown")
        click_using_xpath(self.driver, locators.salutation_option.format(salutation), "Clicked on salutation from dropdown")
        enter_using_xpath(self.driver, locators.first_name_textbox, first_name, "Entered first name")
        enter_using_xpath(self.driver, locators.last_name_textbox, last_name, "Entered last name")
        enter_using_xpath(self.driver, locators.company_textbox, company, "Entered company")
        click_using_xpath(self.driver, locators.save_button, "Clicked on save")

    def validate_lead_created(self, salutation, first_name, last_name):
        name = salutation + " " + first_name + " " + last_name
        is_element_displayed(self.driver, locators.lead_name.format(name))

    def convert_lead(self):
        click_using_actions_and_xpath(self.driver, locators.convert_lead_button, "Clicked on convert")
        is_element_displayed(self.driver, locators.convert_lead_text)
        click_using_actions_and_xpath(self.driver, locators.convert_button,
                                      "Clicked on convert button in convert lead pop up")
        is_element_displayed(self.driver, locators.lead_converted_success_text)

    def clicks_go_to_leads(self):
        click_using_actions_and_xpath(self.driver, locators.go_to_leads_button, "Clicked on Go to Leads button")

    def clicks_contacts_dropdown(self):
        click_using_actions_and_xpath(self.driver, locators.contacts_dropdown, "Clicked on contacts dropdown")

    def validate_contact(self, name):
        is_element_displayed(self.driver, locators.name_in_account.format(name))

    def clicks_accounts_dropdown(self):
        click_using_actions_and_xpath(self.driver, locators.accounts_dropdown, "Clicked on accounts dropdown")

    def validate_account(self, company):
        is_element_displayed(self.driver, locators.company_name_in_account.format(company))

    def create_account(self, account_name):
        click_using_actions_and_xpath(self.driver, locators.new_account_button, "Clicked on new account button")
        enter_using_xpath(self.driver, locators.account_name_textbox, account_name, "Entered account name")
        click_using_actions_and_xpath(self.driver, locators.save_button, "Clicked on save")

    def validate_account_created(self, account_name):
        is_element_displayed(self.driver, locators.account_name_textbox.format(account_name))

    def create_contact_from_account(self, account_name, salutation, first_name, last_name):
        click_using_actions_and_xpath(self.driver, locators.contacts_in_account, "Clicked on contacts in account page")
        click_using_xpath(self.driver, locators.new_contact_button, "Clicked on new contact button")
        is_element_displayed(self.driver, locators.auto_account_name.format(account_name))
        click_using_xpath(self.driver, locators.salutations_dropdown, "Clicked on salutation dropdown")
        click_using_xpath(self.driver, locators.salutation_option.format(salutation),
                          "Clicked on salutation from dropdown")
        enter_using_xpath(self.driver, locators.first_name_textbox, first_name, "Entered first name")
        enter_using_xpath(self.driver, locators.last_name_textbox, last_name, "Entered last name")
        click_using_actions_and_xpath(self.driver, locators.save_button, "Clicked on save")

    def validate_contact_created(self, account_name, first_name, last_name):
        name = first_name + " " + last_name
        is_element_displayed(self.driver, locators.contact_name_in_contact_table.format(name))
        click_using_actions_and_xpath(self.driver, locators.accounts, "Clicked on account")
        click_using_actions_and_xpath(self.driver, locators.account_from_table.format(account_name), "Clicked on account from table")
        is_element_displayed(self.driver, locators.conatcts_linked_in_account_page.format(name))
