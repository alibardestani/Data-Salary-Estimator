import imp
from unittest.mock import patch
import glassdoor_job_scraper as gs
import pandas as pd

path = r'C:\Users\My Computer\Desktop\ds_salary_proj\chromedriver'

df = gs.get_jobs('data scientist', 15, False, path, 15)