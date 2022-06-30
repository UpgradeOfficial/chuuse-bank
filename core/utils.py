from django.conf import settings

import random
from random import randint
from datetime import datetime, timedelta
from rest_framework.exceptions import  ValidationError



# from azure.storage.blob import generate_blob_sas, AccountSasPermissions, BlobServiceClient, BlobClient, ContainerClient, __version__
from datetime import datetime, timedelta
   
random_string = random.randint(1000, 9999)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


