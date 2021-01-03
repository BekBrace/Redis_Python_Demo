import redis
redis_host = 'localhost'
redis_port = 6379


def redis_string():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)
        r.set("message", "Hello, world!")
        msg = r.get("message")
        print(msg)
    except Exception as e:
        print(e)


def redis_integer():
    try:
        r = redis.StrictRedis(
            host=redis_host, port=redis_port, decode_responses=True)
        r.set("number", "100")
        o_number = r.get("number")
        r.incr("number")
        incr_number = r.get('number')
        print(o_number)
        print(incr_number)
    except:
        print('something went wrong!')


if __name__ == "__main__":
    redis_string()
    redis_integer()
