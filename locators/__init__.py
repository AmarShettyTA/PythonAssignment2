# Login page xpaths
username_textbox = '//input[@id="username"]'
password_textbox = '//input[@id="password"]'
login_button = '//input[@id="Login"]'

# Home page
home_page_title = '//span[@title="Home"]'
nav_sales_button = '(//span[text()="Sales"])[1]'

# Sales page
leads_dropdown = '//a[@title="Leads"]//following-sibling::*//div'
new_lead_button = '//span[text()="New Lead"]'
salutations_dropdown = '//button[@name="salutation"]'
salutation_option = '//span[@title="{}"]'
first_name_textbox = '//input[@name="firstName"]'
last_name_textbox = '//input[@name="lastName"]'
company_textbox = '//input[@name="Company"]'
save_button = '//button[@name="SaveEdit"]'
lead_name = '(//*[contains(text(), "{}")])[1]'
convert_lead_button = '//button[@name="Convert"]'
convert_lead_text = '//h1[text()="Convert Lead "]'
convert_button = '(//button[text()="Convert"])[2]'
lead_converted_success_text = '//h2[text()="Your lead has been converted"]'
go_to_leads_button = '//button[text()="Go to Leads"]'
contacts_dropdown = '//a[@title="Contacts"]//following-sibling::*//div'
name_in_account = '//span[text()="{}"]'
accounts_dropdown = '//a[@title="Accounts"]//following-sibling::*//div'
company_name_in_account = '//span[text()="{}"]'
new_account_button = '//span[text()="New Account"]'
account_name_textbox = '//input[@name="Name"]'
account_name = '(//*[contains(text(), "{}")])[2]'
contacts_in_account = '//span[@title="Contacts"]'
new_contact_button = '//button[@name="NewContact"]'
auto_account_name = '//input[@data-value="{}"]'
contact_name_in_contact_table = '(//span[contains(text(), "{}")])[2]'
accounts = '//a[@title="Accounts"]'
account_from_table = '(//a[text()="{}"])[1]'
conatcts_linked_in_account_page = '//article[@aria-label="{}"]'
