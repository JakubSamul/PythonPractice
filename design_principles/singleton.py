def singleton(class_instance):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_instance not in instances:
            instances[class_instance] == class_instance(*args, **kwargs)
        return instances[class_instance]
    
    return get_instance


@singleton
class MongoDbConnection():
    def __init__(self) -> None:
        print('Mongobd connection initialised')


if __name__ == "__name__":
    mongo_conn_one = MongoDbConnection()
    mongo_conn_two = MongoDbConnection()

    print(mongo_conn_one == mongo_conn_two)