import scrapy
import configparser
import os
import scrapy
from scrapy.http import FormRequest

class GradespiderSpider(scrapy.Spider):
    name = "GradeSpider"
    allowed_domains = ["powerschool.aacps.org"]
    start_urls = ["https://powerschool.aacps.org"]

    script_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(script_directory, '..', '..', '..', 'config.ini')
    config = configparser.ConfigParser()
    config.read(config_file_path)
    Username = config.get('credentials2', 'username')
    Password = config.get('credentials2', 'password')
    grades = []

    def start_requests(self):
        login_url = 'https://powerschool.aacps.org/public'
        yield scrapy.Request(login_url, callback=self.login)

    def login(self, response):
        return FormRequest.from_response(response,
                                         formdata={'dbpw': self.Password,
                                                   'serviceName': 'PS Parent Portal',
                                                   'pcasServerUrl': '/',
                                                   'credentialType': 'User Id and Password Credential',
                                                   'ldappassword': self.Password,
                                                   'account': self.Username,
                                                   'pw': self.Password},
                                         callback=self.parse_home)
    
    def parse_home(self, response):
        pass
