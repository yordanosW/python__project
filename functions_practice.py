def hello():
    print("Hello user ")

def pack(el_1, el_2, el_3):
    return [el_1, el_2, el_3]


def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty")
    for food_index in range(len(my_lunch)):
        if food_index == 0:
            print(f"First i eat {my_lunch[food_index]}")
        elif food_index < len(my_lunch):
            print(f"Then I eat {my_lunch[food_index]}")
        else:
            print("my lunchbox is empty")

            

hello()            
print(pack(1,5,10))
print(pack("a","b", "c"))



eat_lunch([])
eat_lunch(["Eggs"])
eat_lunch(["Eggs","Beans","chicken Tendies","Milk"])



    