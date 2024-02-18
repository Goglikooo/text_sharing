# Django Text Processing Web App

This Django web application allows users to submit and store text. Each submitted text is stored in a database, and users can access the stored text using a generated URL. The application also supports text editing.

## Instructions for Users

1. **Enter Text:**
   - Users should enter the desired text in the provided text field on the main page.

2. **Save Text:**
   - Save the entered text by submitting the form. The text will be stored in the database.

3. **Access Stored Text:**
   - The application generates a unique URL for each stored text. Users can access the stored text by visiting this URL.

4. **Edit Text:**
   - Users can edit the stored text by clicking the "Edit" button. The text will be copied back to the text field, allowing modifications.

## Additional Features

- **URL Slug:**
  - The application uses SHA hashing to create URL slugs for easy and secure access to stored text.

## Setup Instructions

To set up and run the project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
