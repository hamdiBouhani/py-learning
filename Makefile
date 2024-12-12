# Variables
PYTHON := python
FLASK_APP := server.py
TESTS := test_server.py

.PHONY: run test clean install

# Install dependencies
install:
	$(PYTHON) -m pip install -r requirements.txt

# Run the Flask server
run:
	$(PYTHON) $(FLASK_APP)

# Run tests
test:
	$(PYTHON) -m unittest $(TESTS)

# Run tests with pytest (optional, if pytest is installed)
pytest:
	pytest $(TESTS)

# Clean up __pycache__ and temporary files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
