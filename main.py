from fastapi import FastAPI, requests
from models import Todo
app = FastAPI(
    title='Todo App',
    description='The test todo app project in seeing how the fast api framework works',
    docs_url='/documenation',
    root_path='/api/v1',
    version='1.0.0'
    )


@app.get('/')
async def home():
    return {'Message': 'Hello World, see my first API'}

todos=[]

#Get all the todso
@app.get('/todos')
async def get_todos():
    return {'Todos': todos}

#Create a todo
@app.post('/create_todo')
async def create_todos(todo: Todo):
    todos.append(todo)
    return {'Message':'Todo created Successfully!'}


#Get Single todo
@app.get('/todo/{todo_id}')
async def get_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {'todo':todo}
    return {'Message': 'No todo found!'}


# #Delete a todo
@app.delete('/delete_todo/{todo_id}')
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo_id == todo.id:
            todos.remove(todo)
            return {'Message':'Todo has been deleted succesfully!'}
    return {'Message':'No todo found'}

# #Update todo
@app.put('/update_todo/{todo_id}')
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo_id == todo.id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {'Todo': todo}
    return {'Message': 'No such todo exists'}