# CVApp

CVApp is a FastAPI application that provides CRUD functionality for managing CV (Curriculum Vitae) data. Users can create, retrieve, update, and delete CV records using a RESTful API. The application also includes utility functions for validating CV data.

## Installation

To use CVApp, you will need Python 3.7 or above. Clone the repository and install the required dependencies using pip:

```
git clone https://github.com/your-username/cvapp.git
cd cvapp
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```
uvicorn main:app --reload
```

The application will run on `http://localhost:8000`. Visit this URL in your browser to access the CVApp homepage.

## API Endpoints

### GET /cv

Retrieve a list of all CV records.

### POST /cv

Create a new CV record. The request body should include the following fields:

- name: The name of the CV owner.
- label: The label or title for the CV.
- location: The location of the CV owner.
- email: The email address of the CV owner.
- phone: The phone number of the CV owner.
- website: The website URL of the CV owner.

### GET /cv/{id}

Retrieve a specific CV record by its ID.

### PUT /cv/{id}

Update a specific CV record by its ID. The request body should include the fields to be updated.

### DELETE /cv/{id}

Delete a specific CV record by its ID.

## Utility Functions

The CVApp includes several utility functions in the `utilities.py` file. These functions can be used to validate CV data before creating or updating records. The following utility functions are available:

- `validate_email(email: str) -> bool`: Validates an email address.
- `validate_url(url: str) -> bool`: Validates a URL.
- `validate_date_range(start_date: datetime, end_date: datetime) -> bool`: Validates a date range.
- `validate_cv_data(cv_data: Dict[str, Any]) -> List[str]`: Validates a CV data dictionary and returns a list of error messages, if any.

## Contributing

Contributions to CVApp are welcome! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Submit a pull request.

## License

CVApp is licensed under the [MIT License](LICENSE).