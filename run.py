from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()
try:

    with Booking() as bot:
        bot.land_first_page()
        bot.remove_popup()
        bot.change_currency()
        bot.select_place_to_go("New York")
        bot.select_dates(check_in_date='3 March 2024',
                        check_out_date='13 March 2024')
        bot.select_adults_childrens_rooms(adult_count=10)
        bot.click_search()
        # bot.apply_star_rating(star_value=4)
        # bot.apply_star_rating(3, 4, 5)
        # bot.sort_price_lowest_first()
        bot.refresh() #A workaround to let our bot to gab the data
        bot.report_results()
        # while True:
        #     pass
except Exception as e:
    if 'in PATH' in str(e): #error line compare in error
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise


