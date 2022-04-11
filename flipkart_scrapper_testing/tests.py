import requests


class tests:
    def __init__(self):
        self.test_url = "http://127.0.0.1:8080"
        self.test_data = {"content": "iphone"}
        self.work_test = {"search_string": "iphone", "product": "APPLE iPhone 12 (Black, 128 GB) "}

    def check_url(self):
        """
        This test is written to check connectivity to the url
        :return: State of the url (accessible or Not)
        """
        response = requests.get(self.test_url)
        if response.status_code == 200:
            print("Headers ",response.headers)
            print("Url:",response.url)
        else:
            print("Website not accessible")

    def check_search(self):
        response = requests.post(self.test_url+str("/results"), data=self.test_data)
        if response.status_code == 200:
            print("Search is working !!",response.status_code)
        else:
            print("Not able to post search request")

    def check_wordcloud(self):
        response = requests.post(self.test_url+str("/post_wordcloud"), data=self.work_test)
        if response.status_code == 200:
            print("Wordcloud is working !!",response.status_code)
        else:
            print("Not able to post search request")

    def check_download(self):
        response = requests.post(self.test_url+str("/post_download_csv"), data=self.work_test)
        if response.status_code == 200:
            print("Download is working !!",response.status_code)
        else:
            print("Not able to post search request")


if __name__ == "__main__":
    # Initialization of the test class
    test = tests()
    # Check url
    test.check_url()
    # check search bar
    test.check_search()
    # check wordcloud
    test.check_wordcloud()
    # check download option
    test.check_download()
