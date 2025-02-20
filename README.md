# Event Management API (NLW Project)

This project is a Python-based API designed to handle events, subscribers, and links. It was developed as part of Next Level Week (NLW), an online educational program by Rocketseat.

## Features

- **Event Management:** Create and read events.
- **Subscriber Management:** Manage subscriber information and subscriptions.
- **Link Management:** Associate links with events.

## Prerequisites

- Python 3.6+
- `pip` (Python package installer)
- Basic knowledge of virtual environments

## Getting Started

Follow these steps to set up and run the API:

### 1. Clone the Repository

```bash
git clone https://github.com/RenatoTMLima/nlw_connect.git
cd nlw_connect
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to isolate project dependencies.

```bash
python3 -m venv venv
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages from the requirements.txt file.

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

This project uses SQLite as the database.

- Create the schema.db file:

  Open a Python terminal:

  ```bash
  python
  ```

  Then, execute the following commands:

  ```bash
  import sqlite3
  sqlite3.connect('schema.db')
  exit()
  ```

- Create the database tables:

  Execute the SQL script located in init/schema.sql against your schema.db file. You can do this using the sqlite3 command-line tool or a database management tool that supports SQLite.

  Using sqlite3 command-line:

  ```bash
  sqlite3 schema.db < init/schema.sql
  ```

  Explanation of the sql scripts:

  The init/schema.sql file contains SQL commands to create the necessary tables for the API. Please review the file to understand the database schema.

### 5. Run the API

Start the API server by executing the run.py script.

```bash
python run.py
```

The API will start running, and you can access it at the specified address (usually http://127.0.0.1:3000 or similar).

## API Endpoints

- **`POST /event`**
  - Body: `{"name": string}`
  - Description: Creates an event.
- **`POST /subscriber`**
  - Body: `{"name": string, "email": string, "link": string, "event_id": number}`
  - Description: Creates a subscriber. The `link` field is optional.
- **`POST /events_link`**
  - Body: `{"event_id": number, "subscriber_id": number}`
  - Description: creates a link to be used for new subscribers.
- **`GET /subscriber/link/:link/event/:event_id`**
  - Description: Retrieves a list of subscribers for a specific event who used a particular link.
  - Parameters:
    - `:link` - The link used by subscribers.
    - `:event_id` - The ID of the event.
- **`GET /subscriber/ranking/event/:event_id`**
  - Description: Retrieves a ranked list of subscribers for each link associated with a specific event.
  - Parameters:
    - `:event_id` - The ID of the event.
