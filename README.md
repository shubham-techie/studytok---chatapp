## #Studytok- A discord-like chatapp to make communities for study discussion.
#### Deployed version - https://studytok-chatapp.herokuapp.com/
### Functionalites -
1. Users can create rooms to discuss on some specific topics.
2. Host/Owner of the room can delete or update the room details as required.
3. User is also provided to delete their messages.
4. All rooms are grouped into topics. Users can also search a room using topic/ room_name/ room_description.


### Cloning the repository -
1. Clone the repository : ```git clone https://github.com/shubham-techie/studytok-chatapp.git```
2. Move into the directory : ```cd studytok-chatapp```
3. Creating a virtual environment : First install virtual environment ```pip install virtualenv``` and then create virtual environment ```virtualenv venv```
4. Activate the virtual environment : ```venv/Scripts/activate```  (Try this if this isn't working : ```cd venv/Scripts``` --> ```activate``` --> ```cd../..```)
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


### Home Screen -
![image](https://user-images.githubusercontent.com/85562020/174847660-dfc892ec-f65c-4e65-8fff-e7ae947ddf51.png)

### Chat room -
![image](https://user-images.githubusercontent.com/85562020/174848880-43da82e7-f180-42d3-a395-521186698b7f.png)
