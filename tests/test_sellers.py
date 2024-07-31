import os
import sys
from unittest.mock import mock_open, patch

import pytest

from parser_reiting import check_new_seller

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def html_content():
    path = os.path.join(os.path.dirname(__file__), 't1.html')
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

@pytest.fixture
def mock_sellers_data():
    return {
        '0435740b1afaa2e7c712c98089460790': 'https://www.avito.ru/user/0435740b1afaa2e7c712c98089460790/profile?src=fs&page_from=from_favorite_sellers'
    }

# @patch("builtins.open", new_callable=mock_open)
# @patch("data.date_sellers.load_sellers", return_value={})
# @patch("data.date_sellers.save_sellers")
# def test_update_sellers(mock_save_sellers, mock_load_sellers, mock_file, html_content):
#     mock_file.return_value.read.return_value = html_content
#     update_sellers()
#     mock_save_sellers.assert_called_once()
#     assert mock_load_sellers.call_count == 1
#     assert mock_file.call_count == 1

@patch("builtins.open", new_callable=mock_open)
def test_check_new_seller(mock_file, html_content, mock_sellers_data):
    mock_file.return_value.read.return_value = html_content
    sellers_link = {}
    updated_sellers_link = check_new_seller(sellers_link)
    assert len(updated_sellers_link) == 1
    assert updated_sellers_link == mock_sellers_data

@patch("builtins.open", new_callable=mock_open)
def test_check_new_seller_with_existing_sellers(mock_file, html_content, mock_sellers_data):
    mock_file.return_value.read.return_value = html_content
    sellers_link = mock_sellers_data.copy()
    updated_sellers_link = check_new_seller(sellers_link)
    assert len(updated_sellers_link) == 1
    assert updated_sellers_link == mock_sellers_data

@patch("builtins.open", side_effect=FileNotFoundError)
def test_check_new_seller_file_not_found(mock_file):
    sellers_link = {}
    updated_sellers_link = check_new_seller(sellers_link)
    assert updated_sellers_link is None