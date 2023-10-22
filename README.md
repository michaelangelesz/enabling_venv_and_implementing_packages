# enabling_venv_and_implementing_packages
## Activity: Analyze the Best Golf Day
In today's activity, we take on the role of a passionate golfer: someone obsessed with the numbers and science of the game, always dedicated to swinging a club on the most ideal, most pleasant day of the week. We will be building a python application that allows us to determine, based on forecast windspeed, the finest day to play golf in the near future.

## Establishing a Virtual Environment
To get started, open your terminal and navigate to where you have been storing your Python projects. Inside, generate a new directory called using_packages, or something of that nature. Then, navigate into that folder.

Once you're inside of your project folder, you are ready to instantiate a virtual environment. To do so, in your terminal, enter the following command:

`python3 -m venv venv`

Remember: The second "venv" is the name of your virtual environment! Typically, naming it "venv" is good practice, but you could name it anything you want to. Just know to change the second "venv" to whatever you named your environment!

Run the ls command now. If successful, you should have a file called venv in your directory. Don't worry about exploring that file for just now: this file will be storing all the necessary data that will be unique to your virtual environment.

Now that your virtual environment has been built, you'll need to activate it. Do so by entering into your terminal:

`source venv/bin/activate`

Upon doing so, you should see a change in your terminal, it may indicate that you are now inside of a virtual environment! Now, any dependencies we install will install to our virtual environment instead of our computer's global python shell.

Before moving on, we should add a gitignore file and make sure to reference our venv file inside of it.

• Create a .gitignore file (The content inside should simply be venv)

## Using PIP
Next up, we need to install the dependencies that will form the core functionality of our application:
• "requests" will allow us to make HTTP requests to our REST API
• "matplotlib" will build our extremely-important graph to visualize which day will be the best for golf. Quantifiably!
To install these dependencies, simply run the following code in your terminal:

`pip3 install matplotlib requests`

Once the packages have been installed, type ls into your terminal once again. What has changed? Nothing? That's right! When we work with external packages in Node.js, we automatically generate a package.json file that has a directory of all of our dependencies. At this stage, if we were to post our code on github, contributors would have no idea what dependencies they would need in order to get the code to work! That's a problem!

Luckily, Pip has a handy fix for that exact problem. Enter the following command in your terminal:

`pip freeze > requirements.txt`

The pip freeze command will post a directory of all of your external packages and the versions that they are on inside of a text file! Whenever you clone an external python project, you can easily install all of the dependencies from the included requirements.txt file by simply running:

`pip install -r requirements.txt`

Excellent work! With that all out of the way, we're ready to write some code.
