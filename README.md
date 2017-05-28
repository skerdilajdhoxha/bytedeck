## Hackerspace test environment installation (instructions for students)
LMS for Timberline Secondary School's Digital Hackerspace

#### Preparation
1. Install Python 3: `sudo apt install python3`
1. Install Git: `sudo apt nstall git`.  If working in Windows, install [Git Bash](https://git-for-windows.github.io/)
1. Pick/create a location for the project, e.g: `~/Developer`

#### Clone the repository
1. Move to the parent directory of the project: `cd ~/Developer`
2. `git clone https://github.com/timberline-secondary/hackerspace.git`
3. This will download the project into ~/Developer/hackerspace/

#### Python Virtual Environment
1. If on Windows, open Git Bash as an administrator
2. On Linux, ensure you are using Python 3.x: `python -V` (Some distros might have Python 2.7 installed)
3. Install [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/): `pip3 install virtualenv`
2. Move to the parent directory of the project: `cd ~/Developer`
2. Create the virtual environment named hackerspace.  This will place the virtual environment into the same folder as the project (just for convenience): `virtualenv hackerspace`
3. Move into the hackerspace dir: `cd hackerspace` (if using git bash, you should now see "(master)" at the end of your prompt
3. Activate your virtual environment: Linux: `source bin/activate` Windows w/Git Bash: `source Scripts/activate`
4. You should now see "(hackerspace)" appear before your prompt.
5. Later, when you are finished you can leave the environment by typing: `deactivate`

#### Installing required python packages
1. `pip install -r requirments-basic.txt`
2. This does not include what is needed for a PostGres database or other production-specific stuff, only development requirements

#### Creating the SQLite database
1. A basic database to get started.  You can move to PostgreSQL later if you like:
`./src/manage.py migrate`  This will create your database and create tables for all the thrid-party apps/requirements
2. Now prepare tables for all of the hackerspace models: `./src/manage.py makemigrations badges announcements courses comments djcytoscape notifications portfolios profile_manager quest_manager prerequisites suggestions` (you might get an error later on if I forget to keep this list of apps updated =)
2. Create tables: `./src/manage.py migrate`
2. Populate the database with some default data: `./src/manage.py loaddata src/initial_data`
3. Create a superuser in the database (i.e.teacher/administrator account): `./src/manage.py createsuperuser`
4. Git Bash: if you get an error, try: `winpty python src/manage.py createsuperuser`

#### Runniing the server!
1. `./src/manage.py runserver`
2. Segmentation Fault?  try running it again...
3. In your browser go to [127.0.0.1:8000](http://127.0.0.1:8000) to see if it worked!
4. Log in as the superuser to see what a teacher/admin sees
5. Sign up to create a student account.
6. Stop running server (or any bash script in progress) with `Ctrl + C`

#### Setting up PyCharm IDE
1. Install some version of PyCharmIDE
1. File > Open, then choose the ~/Developer/hackerspace directory
1. Run > Edit Configurations
1. it "+" and choose Django Server
1. Defaults should be good, but "Run Browser" option is handy, tick it if you want to auto open a browser when you run the server.
1. Turn on Django support.  Click "Fix" button at bottom
1. Tick "Enable Django Support
1. Set Django project root to: ~/Developer/hackerspace/src
1. Set Settings to: `hackerspace_online/settings` (this is relative to the root above)
1. OK, OK.
1. Hit the green play button to test.




