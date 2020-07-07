# Weather Project
## Overview
Steps to run weather system that will determine the weather of 
the current location as well as the booking location.

The system is built using a Django framework with the Django Rest 
Framework for the API aspect.

API endpoint looks like this: 
```bash
/weather?current_location=-33.927407,18.415747&booking_location=-32.927407,19.415747
```

JSON returned in a format such as this:
```bash
{
  "current_location": {
    "date": "2019-12-12",
    "type": "clear-day",
    "description": "Clear throughout the day",
    "temperature": 21.94,
    "wind": {
      "speed": 4.66,
      "bearing": 147,
      "gust": 11.25
    },
    "rain_prob": 0,
    "latitude": -33.927407,
    "longitude": 18.415747
  },
  "booking_location": {
    "date": "2019-12-12",
    "type": "cloudy",
    "description": "Overcast",
    "temperature": 19.67,
    "wind": {
      "speed": 4.66,
      "bearing": 147,
      "gust": 11.25
    },
    "rain_prob": 35,
    "latitude": -32.927407,
    "longitude": 19.415747
  }
}
```

## Installation
Install Python 3.7

```bash
pip install virtualenv
```

Create virtual enviroment using the following command:
```bash
virtualenv venv_weather
```

Activate the virtual enviroment.

On Windows use the following.
```bash
venv_weather\Scripts\activate.bat
```

Install the required packages, using pip and the requirements file.
```bash
pip install -r requirements.txt
```

## Setup
Run the django migrate
```bash
python manage.py migrate
```

Create a super user to access the admin interface, follow the promtes.
```bash
python manage.py createsuperuser
```

## Testing
Run the Django built in testing using the following command:
```bash
python manage.py test
```

## Activate Application without Docker
Run the server
```bash
python manage.py runserver
```

## Activate Application with Docker
Open Docker and navigate to the application via the Docker terminal.
Once at the application run the following commands:
```bash
docker-compose up -d --build
```

Once everything is done, run the next command:
```bash
docker-compose up
```

Once the web service is running you can use the system on the 
following URL:
[http://192.168.99.100:8000/](http://192.168.99.100:8000/)

To stop Docker once is running press CNTRL + C. Once the web service has stopped.
Run the following command:
```bash
docker-compose down
```