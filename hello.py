from urllib.parse import parse_qs


def wsgi_app(environ, start_response):
    params = parse_qs(environ['QUERY_STRING'])
    #params = environ['QUERY_STRING']
    start_response("200 OK", [("Content-Type", "text/plain"),
                              ("Content-Length", str(len(params)))])
    #return params
    ans = []
    for el in params.items():
    	ans.append(str(el[0]) + "=" + str(el[1]))
    	ans_str = "\n".join(ans)
    return [bytes(ans_str, 'utf-8')]
