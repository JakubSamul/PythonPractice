# class StorageLocker():
#     def authenticate(self, client):
#         if client == 'aws':
#             #some code to authenticate against aws
#         elif client == 'azure':
#             #some code to authenticate against azure

#         return client
    
#     def upload(self, filename):
#         if client == 'aws':
#             #some code to upload a file to aws
#         elif client == 'azure':
#             #some code to upload a file to azure

from abc import ABC, abstractmethod


class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class Uploader(ABC):
    @abstractmethod
    def upload_file(self):
        pass


class Aws(Auth, Uploader):

    def authenticate(self):
        #some logic to authenticate against aws
        return 'auth_client'
    
    def upload_file(self):
        #some logic to upload file to aws 
        return 'status_client'
    

class Azure(Auth, Uploader):

    def authenticate(self):
        #some logic to authenticate against azure
        return 'auth_client'
    
    def upload_file(self):
        #some logic to upload file to azure
        return 'status_client'
    

class Gcp(Auth, Uploader):

    def authenticate(self):
        #some logic to authenticate against gcp
        return 'auth_client'
    
    def upload_file(self):
        #some logic to upload file to gcp
        return 'status_client'
    