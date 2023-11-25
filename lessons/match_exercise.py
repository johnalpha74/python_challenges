def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

http_status = input("Enter a number between 399 and 420 \n")

http_error(404)

print(http_error(http_status))
