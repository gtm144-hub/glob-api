import pytest
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import pandas as pd
from unittest.mock import Mock, patch
from service.stats import get_query_results
from sqlalchemy import text

@pytest.fixture
def mock_db():
    return Mock(spec=Session)

def test_get_query_results_database_error(mock_db):
    # Arrange
    query = "SELECT * FROM non_existent_table"
    columns = ["id", "name", "value"]
    mock_db.execute.side_effect = Exception("Table not found")
    
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        get_query_results(mock_db, query, columns)
    
    assert exc_info.value.status_code == 400
    assert str(exc_info.value.detail) == "Table not found"

def test_get_query_results_invalid_columns(mock_db):
    # Arrange
    query = "SELECT id, name FROM test_table"
    columns = ["id", "name", "value"]  # Extra column
    mock_result = [
        (1, "Test1"),
        (2, "Test2")
    ]
    mock_db.execute.return_value = mock_result
    
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        get_query_results(mock_db, query, columns)
    
    assert exc_info.value.status_code == 400
    assert "columns" in str(exc_info.value.detail).lower()
