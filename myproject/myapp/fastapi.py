from fastapi import FastAPI
# from .models import User as DjangoUser



app = FastAPI()

@app.get("/api/data")
def hello():
    return {"message" : "welcome from FastAPI"}


# @app.get("/api/users")
# def users():
#     users = DjangoUser.objects.all()
#     user_list = [{"id": user.id, "name": user.name} for user in users]
#     if len(user_list) ==0:
#         return {"Message" : "No Users here yet !"}
    
#     return {"users": user_list}