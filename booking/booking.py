import os
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_report import BookingReport
from prettytable import PrettyTable #libraris install
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.common.exceptions import TimeoutException



class Booking(webdriver.Chrome):
    def __int__(self, driver_path=r"C:\SeleniumDriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(30)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(20)

    def remove_popup(self):
        try:
            close_popup_element = self.find_element(
                By.XPATH, "//button[@aria-label='Dismiss sign-in info.']"
            )
            close_popup_element.click()
        except:
            print("Skipping popup")

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.XPATH, "//button[@data-testid='header-currency-picker-trigger']"
        )
        currency_element.click()
        # usd_button = self.find_element(
        #     By.XPATH, "//div[@class='aca0ade214 aaf30230d9 cd2e7d62b0']/ul[1]/li[1]/button[1]"
        # )
        usd_button_text = self.find_element(
            By.XPATH, "//div[@class='aca0ade214 aaf30230d9 cd2e7d62b0']/ul[1]/li[1]/button[1]/div[1]/div[1]/span[1]"
        )
        usd_button_text.click()
        self.implicitly_wait(20)

    def select_place_to_go(self, place_to_go):
        place_field_element = self.find_element(
            By.XPATH, "//input[@id=':re:']"
        )
        place_field_element.send_keys(place_to_go)

        first_result_element = self.find_element(
            By.XPATH, "//li[@id='autocomplete-result-0']"
        )
        first_result_element.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.XPATH, f"//span[@aria-label='{check_in_date}']"
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.XPATH, f"//span[@aria-label='{check_out_date}']"
        )
        check_out_element.click()


    def select_adults_childrens_rooms(self, adult_count=1):
        # Search Box Click
        selection_box_element = self.find_element(
            By.XPATH, "//button[@class='a83ed08757 ebbedaf8ac ada2387af8']"
        )
        selection_box_element.click()

        # loop to click the element till minimum value
        # then increase according to your number
        while True:
            # adults decreases till minmum
            decrease_adults_element = self.find_element(
                By.XPATH,
                "//button[@class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 e91c91fa93']"
            )
            decrease_adults_element.click()

            # adults minimum value
            adults_value_element = self.find_element(
                By.XPATH, "//div[@class='a7a72174b8'][1]//span[@class='d723d73d5f']"
            )

            adults_value = int(adults_value_element.text)

            if adults_value == 1:
                break

        # decrease till minimu atfirst then increase according to demand
        # adult increase
        increase_adult_button_element = self.find_element(
            By.XPATH, "(//button[@type='button'])[8]"
        )
        for _ in range(adult_count - 1):
            increase_adult_button_element.click()

    def click_search(self):
        search_button_element = self.find_element(
            By.XPATH, "//button[@type='submit']"
        )
        search_button_element.click()

    """
    ===========================================
    Filteration 
    ===========================================
    """
    # def apply_star_rating(self, *star_values):#multiple value recieved *
    #     self.implicitly_wait(100)
    #     self.execute_script("window.scrollBy(0, 1500);")#scroll
    #
    #     star_filteration_box = self.find_elements(
    #         By.XPATH, "//div[@id='filter_group_class_:r1m:']//div[@data-filters-item]"
    #     )
    #     for star_value in star_values:
    #         for star_innerdiv_element in star_filteration_box:  # innerdiv
    #             star_inner_text = star_innerdiv_element.text  # innerdiv text
    #             if f"{star_value} stars" in star_inner_text:  # compare
    #                 star_innerdiv_element.click()
    #                 break

    # def sort_price_lowest_first(self):
    #     sort_button_element = self.find_element(
    #         By.XPATH, "//button[@class='a83ed08757 faefc93c6f b94d37c0c4']"
    #     )
    #     sort_button_element.click()
    #
    #     price_lowest_button_element = self.find_element(
    #         By.XPATH, "//button[@data-id='price']"
    #     )
    #     price_lowest_button_element.click()

    """
        ===========================================
        Filteration 
        ===========================================
    """
    def report_results(self):
        self.implicitly_wait(100)
        #
        # hotel_boxes = self.find_element(
        #     By.XPATH, "//div[@class='d4924c9e74']"
        # ).find_elements(
        #     By.XPATH, "(//div[@aria-label='Property'])"
        # )
        #
        # print(len(hotel_boxes))

        hotel_boxes = self.find_element(
            By.XPATH, "//div[@class='d4924c9e74']"
        )

        report = BookingReport(hotel_boxes)
        # report.pull_deal_box_attributes()
        table = PrettyTable()
        table.field_names["Hotel Name", "Hotel Price", "Hotel Score"]
        table.add_rows(report.pull_deal_box_attributes())
        print(table)













