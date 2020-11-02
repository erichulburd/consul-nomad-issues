import http.client
import sys


def healthcheck():
    conn = http.client.HTTPConnection('127.0.0.1', 8080, timeout=10)
    conn.request("GET", "/")
    res = conn.getresponse()
    assert res.status == 200
    print('Stdout')
    print("Stderr", file=sys.stderr)
    raise Exception("A test exception")


if __name__ == '__main__':
    healthcheck()
