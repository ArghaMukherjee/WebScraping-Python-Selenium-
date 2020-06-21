from selenium import webdriver
import sys
import timeit
import string
import pickle

# import geckodriver_autoinstaller
# geckodriver_autoinstaller.install()

class scraping():
    driver = webdriver.Firefox()
    url = ''
    xpth = ''

    def __init__(self):
        pass

    #function to check the drivers are working properly or not
    def sel_gecko_check(self):
        try:
            self.driver = webdriver.Firefox()
            self.driver.get("http://www.python.org")
            assert "Python" in self.driver.title
            print('Selenium Drivers Verified functioning successfully !!!')
            return True
        except BaseException as err:
            # self.driver.close()
            print(str(err))
            return False,sys.exit()

        finally:
            self.driver.close()
            print('Terminating Gecko browser check !!!')

    #This function navigates to the URL mentioned and locates the xpath,fetched the value and writes it to result.txt file.
    def navigate_to_website(self,url,xpth):
        try:
            self.url=url
            self.xpth=xpth
            self.driver.get(self.url)
            data = self.driver.find_element_by_xpath(self.xpth).text
            print(data)

            with open('result.txt','wb') as fp:
                pickle.dump(data,fp)
                print('File created and data inserted in the file !!!!!')
        except BaseException as err:
            print(str(err))
            self.driver.close()
            sys.exit()
        finally:
            print('Closing automation instance')
            self.driver.close()


if __name__ == '__main__':
    obj = scraping()
    #temporarily commenting as tested with connection, for testing the connection, please uncomment line 59
    # obj.sel_gecko_check()
    xpth = '//*[@id="toc"]/ul'
    url = 'https://en.wikipedia.org/wiki/List_of_car_brands'
    obj.navigate_to_website(url,xpth)
    print("Time taken:",timeit.timeit())