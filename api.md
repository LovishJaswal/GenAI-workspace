# API Calls with Python (`requests`)

---

# What is an API?

An **API (Application Programming Interface)** allows two applications to communicate with each other.

For example:

- A weather app fetching weather data.
- A payment gateway processing payments.
- A chatbot communicating with an LLM.

---

# URL Structure

A URL generally consists of:

```text
https://example.com/about-us?id=10&name=Lovish
```

| Part | Description |
|------|-------------|
| `https://` | Protocol |
| `example.com` | Domain Name |
| `/about-us` | Endpoint |
| `?id=10&name=Lovish` | Query Parameters |

Example:

```text
https://jsonplaceholder.typicode.com/posts?userId=1&id=2
```

---

# HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Update an entire resource |
| PATCH | Update specific fields of a resource |
| DELETE | Delete a resource |

---

# Making API Calls using `urllib`

Python provides the built-in `urllib` module for making HTTP requests.

Example:

```python
from urllib.request import Request, urlopen

req = Request(
    url="https://jsonplaceholder.typicode.com/posts",
    method="GET"
)

response = urlopen(req)

print(response.read())
```

Although this works, it is more verbose than using the `requests` library.

---

# Making API Calls using `requests`

The `requests` library is the most commonly used library for HTTP requests.

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

print(response.json())
```

---

# Response Object

`requests.get()` returns a **Response object**.

```python
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)
```

Useful properties:

```python
response.status_code
response.headers
response.cookies
response.elapsed
response.content
response.json()
```

---

# Status Codes

Some common HTTP status codes:

| Status Code | Meaning |
|-------------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

Example:

```python
print(response.status_code)
```

---

# Response Methods

## `response.json()`

Converts JSON response into a Python object.

```python
print(response.json())
```

---

## `response.content`

Returns raw response data in bytes.

```python
print(response.content)
```

---

## `response.headers`

Returns response headers.

```python
for key, value in response.headers.items():
    print(key, value)
```

---

## `response.cookies`

Returns cookies sent by the server.

```python
print(response.cookies)
```

---

## `response.elapsed`

Returns the time taken to receive the response.

```python
print(response.elapsed)
```

---

# GET Request

```python
import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    response.raise_for_status()

    print(response.json())

except Exception as e:
    print(e)
```

---

# GET Request with Query Parameters

Instead of writing:

```text
https://jsonplaceholder.typicode.com/posts?userId=1&id=2
```

Use:

```python
import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        params={
            "userId": 1,
            "id": 2
        }
    )

    response.raise_for_status()

    print(response.json())

except Exception as e:
    print(e)
```

Using `params` is cleaner and automatically constructs the URL.

---

# POST Request

Used to create a new resource.

```python
import requests

try:

    response = requests.post(
        url="https://jsonplaceholder.typicode.com/posts",
        data={
            "title": "Test",
            "body": "Test Body",
            "userId": 999
        }
    )

    response.raise_for_status()

    print(response.json())

except Exception as e:
    print(e)
```

---

# PUT Request

PUT replaces the **entire resource**.

```python
import requests

try:

    response = requests.put(
        url="https://jsonplaceholder.typicode.com/posts/1",
        data={
            "id": 1,
            "title": "Updated Title",
            "body": "Updated Body",
            "userId": 444
        }
    )

    response.raise_for_status()

    print(response.json())

except Exception as e:
    print(e)
```

---

# PATCH Request

PATCH updates only specific fields.

```python
import requests

try:

    response = requests.patch(
        url="https://jsonplaceholder.typicode.com/posts/1",
        data={
            "title": "Updated Title"
        }
    )

    response.raise_for_status()

    print(response.json())

except Exception as e:
    print(e)
```

Unlike PUT, PATCH does **not** replace the complete resource.

---

# DELETE Request

Deletes a resource.

```python
import requests

try:

    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    response.raise_for_status()

    print(response.status_code)

except Exception as e:
    print(e)
```

---

# `raise_for_status()`

Raises an exception if the request fails.

```python
response.raise_for_status()
```

- Does nothing if the request is successful.
- Raises an HTTP exception for error status codes (4xx or 5xx).

It is recommended to call this after every API request.

---

# API Calls and Exception Handling

Always wrap API calls inside a `try-except` block.

```python
import requests

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    response.raise_for_status()

    print(response.json())

except Exception as e:
    print(e)
```

---

# cURL

`curl` is a command-line tool used to send HTTP requests.

Example:

```bash
curl http://192.168.1.2:11434/api/chat -d '{
  "model": "phi3:latest",
  "messages": [
    {
      "role": "user",
      "content": "Why is the sky blue?"
    }
  ]
}'
```

The above command sends a request to a locally running LLM (for example, Ollama).

---

# Local API Example

If Ollama is running on your machine, the default endpoint is:

```text
http://localhost:11434
```

or

```text
http://192.168.x.x:11434
```

for other devices on the same network.

---

# Best Practices

- Use the `requests` library instead of `urllib`.
- Always call `raise_for_status()`.
- Wrap API calls in `try-except`.
- Use `params` instead of manually creating query strings.
- Use `PATCH` for partial updates and `PUT` for full updates.
- Check the status code before processing responses.

---

# Summary

- APIs allow communication between applications.
- A URL consists of a domain, endpoint, and optional query parameters.
- `requests` is the preferred library for making HTTP requests.
- Common HTTP methods are GET, POST, PUT, PATCH, and DELETE.
- The Response object provides useful information like status code, headers, cookies, and JSON data.
- Always use exception handling with API calls.
- `curl` can also be used to send HTTP requests from the command line.