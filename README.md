# write_to_file_daily_Github_Actions

## Initial purpose 
This repo is made as an test-environment for github actions. The goal is to create a github action that writes to a file name "dates.txt" and daily appends the current date on the next line.

The programming language that is being used is Python. 

The repo is inspired by this post: https://www.python-engineer.com/posts/run-python-github-actions/

## Phase 1: Remodeling the repo
I want to create an bot that gets certain currency in the "USD" base and puts them into a txt file. I will be using the following API:  https://api.metalpriceapi.com/v1/latest?api_key=[]
with the API call I filter out the specific data that I want and write it to a file using the github actions to run the python script.


