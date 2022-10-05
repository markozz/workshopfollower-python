from models.WorkshopFollowerRepository import WorkshopFollowerRepository

service = WorkshopFollowerRepository("http://localhost:3333")
user = service.find_workshop_follower('8c36e86c-13b9-4102-a44f-646015dfd981')
print(user)
