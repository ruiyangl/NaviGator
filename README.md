# NaviGator
It's a trip destination recomandation web application where users can enter the location they are planning on visiting on the NaviGator website, and it would show the user a list of tourist or historical attractions within a radius of the location.

## Installation

### Backend
We used Python flask for the backend to interact with OpenTripMap API    
More information about OpenTripMap: https://opentripmap.io/product).   
To install Flask: https://flask.palletsprojects.com/en/2.2.x/installation/. 
  
    
    
After installation, navigate to: `/NaviGator/BackEnd`   
to start the RESTapi run: `flask --app handler run`  
     
     
If it's your first time using the OpenTripMap API,   
you would also need to sign in and obtain an API key on their website(https://opentripmap.io/login).    
After obtaining the API key, modify your own key in the `/NaviGator/BackEnd/handler.py` file


### Frontend
