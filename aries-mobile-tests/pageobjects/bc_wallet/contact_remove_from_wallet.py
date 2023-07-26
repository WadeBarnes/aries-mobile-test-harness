import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageobjects.basepage import BasePage
from pageobjects.basepage import WaitCondition


class ContactRemoveFromWalletPage(BasePage):
    """Remove Contact from wallet page object"""

    # Locator
    on_this_page_text_locator = "Remove this Contact"
    remove_contact_locator = (AppiumBy.ID, "com.ariesbifold:id/ConfirmRemoveButton")

    def on_this_page(self):     
        return super().on_this_page(self.on_this_page_text_locator)

    def select_remove_from_wallet(self):
        if self.on_this_page():
            self.find_by(self.remove_contact_locator, wait_condition=WaitCondition.ELEMENT_TO_BE_CLICKABLE).click()

            # return a new page object for the Remove from wallet page
            from pageobjects.bc_wallet.contacts import ContactsPage
            return ContactsPage(self.driver)
        else:
            raise Exception(f"App not on the {type(self)}") 

    def get_details_text(self) -> str:
        if self.on_this_page():
            return self.driver.page_source
        else:
            raise Exception(f"App not on the {type(self)}")

