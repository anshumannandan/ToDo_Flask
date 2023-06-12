# <p align = "center"> ToDo Application </p>
## <p align = "center"> Features </p>

### <p align = "center">1. Get Paginated List of all Tasks </p>
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/ff32ab8d-8ff5-48fb-8c24-2a84f0fcefb3)
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/7cefdf8c-75cf-4758-9a45-bc7c8a4f3d4c)

### <p align = "center">2. Add a Task </p>
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/02a49d22-9539-4e0f-a0d9-3e8881262bbf)

### <p align = "center">3. Edit an existing Task </p>
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/b7b16ed6-dea2-44e9-86a2-2684a5abe176)

### <p align = "center">4. Get details of an existing Task </p>
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/0bc7a0c3-4077-4cfc-a111-4bc90c43aab9)

### <p align = "center">5. Delete an existing Task </p>
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/7297b544-80fe-4527-87b9-dd3c16058bc3)
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/276cefd4-32b3-4af0-9caf-f5587b2ab273)

### <p align = "center">6. Validations </p>
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/09e8667e-8222-4afc-8f18-052b0bc3ef29)
![image](https://github.com/anshumannandan/ToDo_Flask/assets/93365821/9185905a-e666-42fd-9c6d-7e8c57c623c4)


## How to setup the project on your local machine?

1. Clone the repository:

```CMD
git clone https://github.com/anshumannandan/ToDo_Flask
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Navigate to the project directory: 

```CMD
cd ToDo_Flask
```

3. Install & Create a virtual environment:

```CMD
pip install virtualenv
virtualenv venv
```

4. Activate the virtual environment:
```CMD
venv/scripts/activate
```

5. Install the dependencies: 

```CMD
pip install -r requirements.txt
```

6. Create a file named `.env` having following contents
```
DEBUG = # True or False
DATABASE = # DATABSE URL
```

7. Open Python terminal from command prompt

```CMD
python
```

8. In the python terminal execute the following commands

```py
from app import app, db
app.app_context().push()
db.create_all()
exit()
```

9. Run the backend server on localhost:

```CMD
python app.py
```

You can access the endpoints from your web browser following this url:
```url
http://localhost:5000
```
