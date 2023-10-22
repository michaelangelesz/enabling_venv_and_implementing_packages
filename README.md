# Enabling venv and implementing packages in Python
## Activity: Analyze the Best Golf Day
In today's activity, we take on the role of a passionate golfer: someone obsessed with the numbers and science of the game, always dedicated to swinging a club on the most ideal, most pleasant day of the week. We will be building a python application that allows us to determine, based on forecast windspeed, the finest day to play golf in the near future.

<hr />

## Establishing a Virtual Environment
To get started, open your terminal and navigate to where you have been storing your Python projects. Inside, generate a new directory called using_packages, or something of that nature. Then, navigate into that folder.

Once you're inside of your project folder, you are ready to instantiate a virtual environment. To do so, in your terminal, enter the following command:

On Mac:
```
python3 -m venv venv
```

On Windows:
```
py -m venv venv
```

Remember: The second "venv" is the name of your virtual environment! Typically, naming it "venv" is good practice, but you could name it anything you want to. Just know to change the second "venv" to whatever you named your environment!

Run the ls command now. If successful, you should have a file called venv in your directory. Don't worry about exploring that file for just now: this file will be storing all the necessary data that will be unique to your virtual environment.

Now that your virtual environment has been built, you'll need to activate it. Do so by entering into your terminal:

Mac:
```
source venv/bin/activate
```

Windows:
```
.\venv\Scripts\activate
```

Upon doing so, you should see a change in your terminal, it may indicate that you are now inside of a virtual environment! Now, any dependencies we install will install to our virtual environment instead of our computer's global python shell.

Before moving on, we should add a gitignore file and make sure to reference our venv file inside of it.

• Create a .gitignore file (The content inside should simply be venv)

<hr />

## Using PIP
Next up, we need to install the dependencies that will form the core functionality of our application:
• "requests" will allow us to make HTTP requests to our REST API
• "matplotlib" will build our extremely-important graph to visualize which day will be the best for golf. Quantifiably!
To install these dependencies, simply run the following code in your terminal:

```
pip3 install matplotlib requests
```

Once the packages have been installed, type ls into your terminal once again. What has changed? Nothing? That's right! When we work with external packages in Node.js, we automatically generate a package.json file that has a directory of all of our dependencies. At this stage, if we were to post our code on github, contributors would have no idea what dependencies they would need in order to get the code to work! That's a problem!

Luckily, Pip has a handy fix for that exact problem. Enter the following command in your terminal:

```
pip freeze > requirements.txt
```

The pip freeze command will post a directory of all of your external packages and the versions that they are on inside of a text file! Whenever you clone an external python project, you can easily install all of the dependencies from the included requirements.txt file by simply running:

```
pip install -r requirements.txt
```

Excellent work! With that all out of the way, we're ready to write some code.

<hr />

## Requesting API Data
Now that we have all of our external packages installed, create a file called script.py. We will be building all of our logic in this file.

Add the following code to script.py:

```
import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime
```

Hey, what gives! Why is the import syntax different for the bottom two? Great question! We are importing just specific modules from those packages. From matplotlib we are just importing the module that supports drawing a graph, and from datetime we are importing the module that allows us to access the current time! The other two, however, we are importing the entire package.

Next up, we need to make a request to our API using the requests package. Similarly to the axios package for Node.js, requests is fairly simple to implement and can handle RESTful request patterns handily. Just like when we fetch API data with JavaScript, we will need to convert our response object to json.

Add the following code to your script:

```
import pprint
import requests
from matplotlib import pyplot as plt
from datetime import datetime

API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/'
city = 'seattle' # feel free to enter your own city here!
r = requests.get(API_URL + city)
response = r.json()
print(response)
```

Now feel free to run your code! Let's see what this API is returning.

The API should have successfully returned weather data inside of an object, but it is not easily read.
Yuck! The data is there, but it's hard to read. But we've included a package that can help us with this!

Add the following code to your script to polish up that return and make it a touch easier to read:

undefinedClick here to copy
Expected return:

After implementing PrettyPrinter, our json response looks more readable with correct code-indenting.
Now that's what I call pretty printing.

