# REST - representational state transfer
## Architectural constraints: 
(A system that complies with some or all of these constraints is loosely referred to as RESTful) 
> - Client–server architecture:
separating the user interface concerns from the data storage concerns.

Client-Server is a design pattern:
The client enables users to interact with data
The server waits for and respond to requests for many clients
 
> - Statelessness:  no session information is retained by the receiver, usually a server.

every packet of information transferred can be understood in isolation, without context information from previous packets in the session.
increasing performance by removing server load 

> - Cacheability:
clients and intermediaries can cache responses. 

Responses must, implicitly or explicitly, define themselves as either cacheable or non-cacheable


> - Layered system:
A client cannot ordinarily tell whether it is connected directly to the end server or to an intermediary along the way. 

If a proxy or load balancer is placed between the client and server, it won't affect their communications


> - Code on demand (optional):
Servers can temporarily extend or customize the functionality of a client by transferring executable code.

for example, compiled components such as Java applets, or client-side scripts such as JavaScript

> - Uniform interface:
1) Resource identification in requests - Individual  esources are identified in requests. 
for example using URIs in RESTful Web services. The resources themselves are conceptually separate from the representations that are returned to the client. For example, the server could send data from its database as HTML, XML or as JSON—none of which are the server's internal representation.

2) Resource manipulation through representations - When a client holds a representation of a resource, including any metadata attached, it has enough information to modify or delete the resource's state.

3) Self-descriptive messages - Each message includes enough information to describe how to process the message. For example, which parser to invoke can be specified by a media type.[1]
4) Hypermedia as the engine of application state (HATEOAS) - Having accessed an initial URI for the REST application—analogous to a human Web user accessing the home page of a website—a REST client should then be able to use server-provided links dynamically to discover all the available resources it needs. As access proceeds, the server responds with text that includes hyperlinks to other resources that are currently available. There is no need for the client to be hard-coded with information regarding the structure or dynamics of the application.

## HTTP-based RESTful APIs are defined with the following aspects:
- a base URI
- standard HTTP methods (e.g., GET, POST, PUT, and DELETE)


## HTTP response status codes
HTTP response status codes indicate whether a specific HTTP request has been successfully completed
1) Informational responses (100–199)


2) Successful responses (200–299)
   * 200 OK
   The request succeeded. The result meaning of "success" depends on the HTTP method:
     - GET: The resource has been fetched and transmitted in the message body.
     - HEAD: The representation headers are included in the response without any message body.
     - PUT or POST: The resource describing the result of the action is transmitted in the message body.
     - TRACE: The message body contains the request message as received by the server.
   * 201 Created
   The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.

3) Redirection messages (300–399)

4) Client error responses (400–499)
   * 400 Bad Request
   The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

   * 401 Unauthorized
   Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.
   * 404 Not Found
   The server can not find the requested resource. In the browser, this means the URL is not recognized
 
5) Server error responses (500–599)


# HTTP Hypertext Transfer Protocol
application layer protocol.

Allows a client to fetch and update resources from a server. It could be used to fetch hypertext documents, text, and binary data. It can also be used to create, update, and delete data on a server.

Use a request response message pair

REST APIs use well-defined URLs that contain the resource type being operated on.

## URL Uniform Resource Locator

http(s)://<_host>:<_port>/<_path_to_resource>?<_params_name>=<_params_value>

## HTTP response status codes
HTTP response status codes indicate whether a specific HTTP request has been successfully completed
1) Informational responses (100–199)


2) Successful responses (200–299)
   * 200 OK
   The request succeeded. The result meaning of "success" depends on the HTTP method:
     - GET: The resource has been fetched and transmitted in the message body.
     - HEAD: The representation headers are included in the response without any message body.
     - PUT or POST: The resource describing the result of the action is transmitted in the message body.
     - TRACE: The message body contains the request message as received by the server.
   * 201 Created
   The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.

3) Redirection messages (300–399)

4) Client error responses (400–499)
   * 400 Bad Request
   The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

   * 401 Unauthorized
   Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.
   * 404 Not Found
   The server can not find the requested resource. In the browser, this means the URL is not recognized
 
5) Server error responses (500–599)
