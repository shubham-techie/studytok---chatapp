## *#Studytok* - A discord-like chatapp to make communities for study discussion.
#### Deployed version - https://studytok-chatapp.herokuapp.com/

### Features -
1. Users can create rooms to discuss on some specific topics.
2. Host/Owner of the room can delete or update the room details as required.
3. User is also provided to delete their messages.
4. All rooms are grouped into topics. Users can also search a room using topic/ room_name/ room_description.


## Home Screen -
<img src="https://user-images.githubusercontent.com/85562020/174878381-43e1fb7d-08f3-4b1a-8bda-c871086396e7.png" width="800">

## Chat room -
<img src="https://user-images.githubusercontent.com/85562020/174878510-4d5b30df-c260-4e51-bfcf-74776625df77.png" width="800">

### Cloning the repository -
1. Clone the repository : ```git clone https://github.com/shubham-techie/studytok-chatapp.git```
2. Move into the directory : ```cd studytok-chatapp```
3. Creating a virtual environment : First install virtual environment ```pip install virtualenv``` and then create virtual environment ```virtualenv venv```
4. Activate the virtual environment : ```venv/Scripts/activate```  (Try this if the previous one isn't working : ```cd venv/Scripts``` --> ```activate``` --> ```cd../..```)
5. Install the required packages : ```pip install -r requirements.txt```                                                                                                

7. (Now, I have set the environment variables for SECRET_KEY and DATABASE CREDENTIALS. So, you need to generate SECRET_KEY and change the settings for Database file)
8.  Generate SECRET_KEY : First enable the python interpreter (using cmd```python```) and in interpreter run following two python lines ```from django.core.management.utils import get_random_secret_key``` and ```get_random_secret_key()```.  Copy the generated string SECRET_KEY in SECRET_KEY of setting.py file.
9.  Replace the DATABASES configuration with ```DATABASES = {                                                                                                                               'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
       }
    }```
8.  Set the ```DEBUG=True``` in settings.py file.
9.  Generate SQL executable commands using ```python manage.py makemigrations``` and create database using ```python manage.py migrate```.
10.  Now, the app is ready to go. Run the app : ```python manage.py runserver```
