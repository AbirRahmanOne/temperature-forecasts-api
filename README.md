# temperature-forecasts-api
This is temperature forecasts api


## Project Run Instructions:
### Create a virtual environment to isolate our package dependencies locally
* `python3 -m venv env`
* `source env/bin/activate`  # On Windows use `env\Scripts\activate`
### Install all dependencies 
* `pip install -r requirements.txt`
* `pip freeze > requirements.txt`
  
### Adding Countries Instructions:
* Open Terminal
* Go to project directory
* Type `python manage.py migrate`
* Type `python manage.py seed`

### Project Run Instructions:
* Open Terminal
* Go to project directory
* Create Super User 
   * Type  `python manage.py createsuperuser`
  
* Type `python manage.py runserver`


## API Overview (Example):

  
### Country CRUD Operation
* Get all countries list:
    * `http://localhost:8000/forecast/coolest-ten-districts`
    * Method: `GET`
* Get specific country details:
     * `http://localhost:8000/forecast/compare-temperature/`
     * Input Body: 
        {
            "src_lat":"22.7185",
            "src_long":"89.0705",
            "travel_date":"2023-10-14",
            "travel_lat":"23.7115253",
            "travel_long":"90.4111451"
      }
     * Method: `POST`


  




