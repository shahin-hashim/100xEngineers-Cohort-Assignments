from fastapi import FastAPI, Body, HTTPException, status
from pydantic import BaseModel
import json

app = FastAPI()


class Operation(BaseModel):
    elements: list[float]
    result: float = None  # Optional field for storing the calculated result


operations_file = "operations.json"  # Path to the JSON file


def load_operations():
    try:
        with open(operations_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_operations(operations):
    with open(operations_file, "w") as f:
        json.dump(operations, f, indent=4)


@app.post("/add")
async def add_operation(operation: Operation = Body(...)):
    """Performs addition of elements and stores the operation in a JSON file."""

    if not operation.elements:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No elements provided")

    operation.result = sum(operation.elements)
    operations = load_operations()
    operations.append(operation.dict())
    save_operations(operations)
    return operation


@app.get("/operations")
async def get_operations():
    """Retrieves all stored operations from the JSON file."""

    operations = load_operations()
    return operations


@app.delete("/operations")
async def delete_operations():
    """Deletes all stored operations from the JSON file."""

    with open(operations_file, "w") as f:
        f.write("[]")  # Clear the file content
    return {"message": "Operations deleted successfully"}


@app.put("/operations/{index}")
async def update_operation(index: int, operation: Operation = Body(...)):
    """Updates a specific operation at the given index in the JSON file."""

    operations = load_operations()
    if index < 0 or index >= len(operations):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Operation not found")

    # Optionally update result based on new elements
    operation.result = sum(operation.elements)  # Recalculate sum

    operations[index] = operation.dict()  # Replace existing operation with updated data
    save_operations(operations)
    return {"message": "Operation updated successfully"}


@app.patch("/operations/{index}")
async def patch_operation(index: int, operation: dict = Body(...)):
    """Updates a specific operation at the given index in the JSON file using a PATCH request."""

    operations = load_operations()
    if index < 0 or index >= len(operations):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Operation not found")

    # Update only specified fields (e.g., elements)
    operations[index].update(operation)  # Merge provided data with existing operation

    save_operations(operations)
    return {"message": "Operation patched successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
