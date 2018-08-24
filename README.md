# AirBNB Price Prediction with CrimeIndex (Shelter Made Safer)


The emergence of sharing accommodation via online marketplaces have drastically changed the travel accommodation industry in the recent past. Airbnb,
a pioneer in travel accommodation industry has created a platform for the people to list, discover, and book unique accommodations around the world. 
The company does not own any lodging; it is merely a broker and receives percentage service fees (commissions) from both guests and hosts in
conjunction with every booking. It has over 3,000,000 lodging listings in 65,000 cities and 191 countries, and the cost of lodging is set by the host. This
project revolves around this concept of shared economy and helps the user in predicting optimal price for the listings and safety level of the neighborhood.

This project analyzes the Airbnb’s complete listings of New York city to predict whether the price set by the host is optimal. It considers various attributes like
number of rooms, availability, location, people allowed and many more to predict the price. Parallel to this, the crime data of the city is clustered based on the
neighborhood, location and crime-type. This acquired classifiers are then put together with the Airbnb listings to provide better results for the user in terms of
predicting accommodation with cheap pricing to safer neighborhood. In a nutshell, this project helps the guests to check how safe and cheap are the
listings posted onto the Airbnb website.

Prerequisites:
- Docker
- Python2.7
- Elastic Search and Kibana (updated to run in AWS ES)

A. Step to Run this application: 

1. Build Docker image [Run] ``` make build ```
2. Run the container.
	* Run the container in detached mode. [Run] ``` make run-detached ``` (Recommended mode)
	* Run the container in interactive mode. [Run] ``` make run-interactive ```

3. Open 127.0.0.1:5000 in your browser.
4. To remove the existing containers. [Run] ``` make clean ``` (Caution: Do this only if you have to delete your containers)


B. Misc: 
1. To check the running containers [Run] ``` docker ps  ```
    If you couldn't find sms_detached or sms_interactive containers then there should be some error and the contianer should be exited. To check exited container run ``` docker ps -a  ```
2. To debug the process run in interactive mode. (GOTO step A:2b)


Please star this project if you like it. 
If you still couldn't run in your system, raise an issue and I will try to reply ASAP.

