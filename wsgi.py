from app import app, socketio

if __name__ == "__main__":
    socketio.run(app)

# gGunicorn and WSGI (web server gateway interface) are both 
# components used un deploying and serving Python web applications, 
#particularly those built with web frameworks like Flask and Django.