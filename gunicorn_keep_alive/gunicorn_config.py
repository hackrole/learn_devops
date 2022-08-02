import multiprocessing


bind = "127.0.0.1:8000"

wsgi_app = "hello:app"
workers = 1
worker_class = "gthread"
threads = 10

# workers = multiprocessing.cpu_count() * 2 + 1
# spew = True


keepalive = 3
