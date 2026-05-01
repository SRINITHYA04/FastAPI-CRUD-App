# 📚 FastAPI CRUD Application (In-Memory DB)

## 🚀 Overview
This project is a simple yet powerful CRUD (Create, Read, Update, Delete) application built using **FastAPI**. It uses an **in-memory database (Python list)** to demonstrate backend fundamentals, request validation, and REST API design.

---

## 🛠️ Tech Stack
- **FastAPI**: The web framework.
- **Pydantic**: For data validation and settings management.
- **Python Typing**: For clear and concise type hinting.

---

## 📌 Features

### ✅ 1. Get All Books
- **Endpoint:** `GET /books`
- Returns a list of all stored books.
- Uses `response_model=List[Book_Strict]` for automated response validation.

### ✅ 2. Get Book by ID
- **Endpoint:** `GET /books/{book_id}`
- Uses **path parameters** to find a specific entry.
- Returns the book object or a `404 Not Found` error.

### ✅ 3. Create a Book
- **Endpoint:** `POST /books`
- Uses **Pydantic BaseModel (`Book_Strict`)** to ensure all required fields are sent.
- Converts the Pydantic object to a dictionary using `.model_dump()`.

### ✅ 4. Partial Update (PATCH)
- **Endpoint:** `PATCH /books/{book_id}`
- Uses a **Flexible Base Model (`Book_Flexible`)** where all fields are `Optional`.
- **Implementation:** `book.update(book_update_data.model_dump(exclude_unset=True))`
- This ensures only the fields you actually send are updated, leaving the rest untouched.

### ✅ 5. Delete a Book
- **Endpoint:** `DELETE /books/{book_id}`
- Removes the book from the in-memory list.
- Returns the deleted object for confirmation.

---

## 🧠 Validation Strategy


| Model | Usage | Requirement |
| :--- | :--- | :--- |
| **Book_Strict** | `POST` (Creation) | All fields are mandatory. |
| **Book_Flexible** | `PATCH` (Updates) | All fields are `Optional[type] = None`. |

---

## ⚠️ Important Learnings
- **`Optional` vs Default:** `Optional[type]` only helps with type checking; `= None` is what actually makes the field optional in the API request.
- **`exclude_unset=True`:** This is the "secret sauce" for PATCH requests. It prevents your database from being overwritten by `null` values for fields you didn't send.

---

## ▶️ How to Run

1. **Activate your environment:**
   ```bash
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate     # On Windows
   ```

2. **Run the server:**
   ```bash
   uvicorn app:app --reload
   ```

---

## 🎯 Conclusion
This project demonstrates the core pillars of FastAPI:
- Clean REST API design.
- Data integrity through Pydantic.
- Efficient partial updates using PATCH.

---
