To run, create a new python virtual environment using python3 -m venv <env_name> and then activate it and execute the following commands:
### python3 -m pip install flask
### python3 -m pip install requests
### python3 -m pip install bs4
### python3 scrape.py
### python3 -m flask run --host=0.0.0.0

To test, you can run the following command in a separate terminal:
### curl -i -H "Content-Type: application/json" -X POST -d '{"maturity_date":"2022-05-1", "reference_rate": "SOFR", "rate_floor": 0.02, "rate_ceiling": 0.10, "rate_spread": 0.02}' http://localhost:5000

This took about three and a half hours. If I had more time, I would do several improvements (it is extremely rudimentary). I would add tests, I would add a requirements.txt to install everything, I would remove the rates.db and add a gitignore to prevent it from coming back, I would Dockerize it, I would research whether sqlite can handle concurrent reads/writes and probably swap it out with postgres, I would figure out how to keep the server up while updating the database with new Pensford data, I would make a cron job to run the scraper at a regular interval, I would fix up this markdown file, I would add comments, I would add more input validation/error handling to the code since Pensford might change its data format and the current code is very brittle.

If it came time to actually productionize, I would think about how to scale up and down the number of servers in response to increases and decreases in request load, and probably add a load balancer in front of it, presuming I had already containerized it and deployed it to the cloud. Instead of running a scraper, I would find an actual API for the data and use that. 
