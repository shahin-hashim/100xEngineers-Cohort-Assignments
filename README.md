## FastAPI Addition Calculator with JSON Storage

This FastAPI application provides an API for performing addition operations, storing them in a JSON file, and retrieving or updating them.

**Features:**

- Add multiple numbers through a POST request.
- Retrieve all stored operations using a GET request.
- Delete all stored operations with a DELETE request.
- Update a specific operation by index using PUT or PATCH requests.
  - PUT replaces the entire operation data (elements and result).
  - PATCH allows modifying only specific fields (e.g., elements).

**Requirements:**

- Python 3.6+
- FastAPI

**Installation:**

1. Clone this repository or download the code.
2. Install dependencies: `pip install fastapi`

**Running the application:**

1. Open a terminal and navigate to the project directory.
2. Run the application using `uvicorn main:app --host 0.0.0.0 --port 8000` (replace the port if needed).

**API Endpoints:**

| Endpoint | Method | Description |
|---|---|---|
| `/add` | POST | Add a new operation with a JSON body containing `elements` (list of numbers). |
| `/operations` | GET | Retrieve all stored operations from the JSON file. |
| `/operations` | DELETE | Delete all stored operations. |
| `/operations/{index}` | PUT | Update a specific operation at the given index with a JSON body containing `elements` (and optionally `result`). |
| `/operations/{index}` | PATCH | Partially update a specific operation at the given index with a JSON body containing only the fields to update (e.g., `elements`). |

**Example Usage (using Postman or curl):**

**1. Add an operation (POST /add):**

```json
{
  "elements": [1, 2, 3]
}
```

**2. Retrieve all operations (GET /operations):**

**3. Delete all operations (DELETE /operations):**

**4. Update an operation at index 1 (PUT /operations/1):**

```json
{
  "elements": [4, 5]
}
```

**5. Partially update an operation at index 1 (PATCH /operations/1):**

```json
{
  "elements": [7, 8]
}
```

**Additional Notes:**

- The operations are stored in a file named `operations.json`.
- Error handling is implemented for invalid requests and operations.
