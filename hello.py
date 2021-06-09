from urllib.parse import parse_qs


def wsgi_app(environ, start_response):
    #params = parse_qs(environ['QUERY_STRING'])
    params = environ['QUERY_STRING']
    start_response("200 OK", [("Content-Type", "text/plain"),
                              ("Content-Length", str(len(params)))])
   # return [(params.keys()[0]).encode('utf-8')]
    body = [bytes(i + '\n', 'ascii')
            for i in environ['QUERY_STRING'].split('&')]
    #ans = []
    # for el in params.items():
    #    ans_str = str(el[0]) + "=" + str(el[1][0]) + "\n"
    #    ans.append(bytes(ans_str, 'ascii'))
    return body
