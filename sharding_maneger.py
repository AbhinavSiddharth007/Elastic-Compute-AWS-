import pymysql

# Static config for 3 shards
SHARD_CONFIG = {
    0: {"host": "ec2-1-1-1-1.compute.amazonaws.com", "port": 3306, "user": "admin", "password": "pass", "db": "shifts"},
    1: {"host": "ec2-2-2-2-2.compute.amazonaws.com", "port": 3306, "user": "admin", "password": "pass", "db": "shifts"},
    2: {"host": "ec2-3-3-3-3.compute.amazonaws.com", "port": 3306, "user": "admin", "password": "pass", "db": "shifts"},
}

SHARD_COUNT = len(SHARD_CONFIG)

def get_shard_id(user_id):
    return user_id % SHARD_COUNT

def get_db_connection(user_id):
    shard_id = get_shard_id(user_id)
    config = SHARD_CONFIG[shard_id]
    return pymysql.connect(
        host=config["host"],
        port=config["port"],
        user=config["user"],
        password=config["password"],
        database=config["db"],
        cursorclass=pymysql.cursors.DictCursor
    )
