
def internal_exception_logger(tag_1, tag_2):
    exception = "There was an error executing the decorated func and an exception was raised"
    
    def decorator(fun):
        def log(exception_string, tags):
            import logging
            print("Initializing logger")
            logging.basicConfig(filename="internal_exception_logger.log", filemode="a", level=logging.INFO,
                                format="%(asctime)s- %(levelname)-8s- %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
            logging.info(f"{exception_string}", extra={"tag1": {tags[0]}, "tag2": {tags[1]}})

        def wrapper(*args, **kwargs):
            try:
                print("Trying to execute function")
                return fun(*args, **kwargs)
            except:
                print("Function execution failed, invoking the logger function!")
                return log(exception, [tag_1, tag_2])
        return wrapper
    return decorator


@internal_exception_logger("tag_1", "tag_2")
def test_call():
    raise Exception("This is an exception")


test_call()
