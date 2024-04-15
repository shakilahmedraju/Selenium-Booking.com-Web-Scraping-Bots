# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element #whole div of list
        self.deal_boxes = self.pull_deal_boxes() #individual div of list

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(
            By.XPATH, "//div[@class='c82435a4b8 a178069f51 a6ae3c2b40 a18aeea94d d794b7a0f7 f53e278e95 c6710787a4']"
        )

    def pull_deal_box_attributes(self):

        for deal_box in self.deal_boxes:#collect info from each div
            collection = []
            hotel_name = deal_box.find_element(
                By.XPATH, "(//div[@data-testid='title'])"
            ).get_attribute('innerHTML').strip()

            hotel_price = deal_box.find_element(
                By.XPATH, "//span[@data-testid='price-and-discounted-price']"
            ).get_attribute('innerHTML').strip()

            hotel_star = deal_box.find_element(
                By.XPATH, "//div[@class='a3b8729ab1 d86cee9b25']"
            ).get_attribute('innerHTML').strip()

            collection.append(
                [hotel_name, hotel_price, hotel_star]
                #rows[[name, pric, star], [name, pric, star]]
            )
        return collection
