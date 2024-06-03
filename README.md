# Frappe External JS Handler App

This Frappe app is designed to create an external JavaScript handler for another app. The handler adds and manages dates for the Article Doctype in the tutorial app, updating the date when an article is issued and displaying the number of days since issuance.

## Features

- **Date Management**: Adds a date field to the Article Doctype in the tutorial app and updates it when the article is issued.
- **Status Dialog**: Displays a dialog showing the number of days since the article was issued when the article page is opened and its status is issued.
- **Workflow**: Implements a workflow for the Article Doctype, allowing articles to move through 'draft', 'issued', 'returned', and 'discarded' states.

## Installation

### Prerequisites

Ensure you have Frappe framework installed and the tutorial app set up.

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mali-nutan/training_task_frappe_app.git

2. **Install the App**:

   cd training_task_frappe_app
   bench --site <site-name> install-app training_task_frappe_app


3.**Update Your Site**:
   bench --site <site-name> migrate
 
## Usage

Add Date Field: Add a date field to the Article Doctype of the tutorial app. This field will be updated when the article is issued.


Show Dialog: When an Article page is opened and its status is 'issued', a dialog will appear showing the number of days since the article was issued.


Article Workflow: The Article Doctype has a workflow that allows each article to transition through the 'issue', 'return', and 'discarded' states.

