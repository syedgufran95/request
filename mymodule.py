import json







def gprint(obj):
	#takes in a python object and converts it into a string
	prv=type(obj)
	text=json.dumps(obj,sort_keys=True,indent=4)
	
	print("Previously the data was of %s, After dumps the data is :   %s  And the data is given below: \n           %s       "%(prv,type(text),text))



def code(x):
	dict={200: "Everything went okay, and the result has been returned (if any).",
		  201:"Created The request has succeeded and a new resource has been created as a result. This is typically the response sent after POST requests, or some PUT requests",
		  202:"Accepted The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing.",
		  203: "Non-Authoritative Information This response code means the returned meta-information is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the \"200 OK\" response is preferred to this status.",
		  204: "No Content There is no content to send for this request, but the headers may be useful. The user-agent may update its cached headers for this resource with the new ones.",
		  205: "Reset Content Tells the user-agent to reset the document which sent this request.",
		  206: "Partial Content This response code is used when the Range header is sent from the client to request only part of a resource.",
		  207: "Multi-Status (WebDAV) Conveys information about multiple resources, for situations where multiple status codes might be appropriate.",
		  208: "Already Reported (WebDAV) Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.",
		  226: "IM Used (HTTP Delta encoding) The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.Redirection messages",
		  300: "Multiple Choice The request has more than one possible response. The user-agent or user should choose one of them.(There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)",
 		  301: "The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.",
		  302: "Found This response code means that the URI of requested resource has been changed temporarily. Further changes in the URI might be made in the future. Therefore, this same URI should be used by the client in future requests.",
		  303: "See Other The server sent this response to direct the client to get the requested resource at another URI with a GET request.",
		  304: "Not Modified This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.",
		  305: "Use Proxy Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy.",
		  306: "unused This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1 specification.",
		  307: "Temporary Redirect The server sends this response to direct the client to get the requested resource at another URI with same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP method used: If a POST was used in the first request, a POST must be used in the second request.",
		  308: "Permanent Redirect This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header.This has the same semantics as the 301 Moved Permanently HTTP response code, with the exception that the user agent must not change the HTTP method used: If a POST was used in the first request, a POST must be used in the second request.",





		  400:"The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.",
		  401:"The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.",
		  403:"The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.",
		  404:"The resource you tried to access wasn’t found on the server.",
		  503:"The server is not ready to handle the request.",







		  }



	print("status code is %s , and the description is given below: \n %s\n"%(x,dict[x]))