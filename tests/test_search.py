"""
Search & Filter Tests (*Kiểm thử Tìm kiếm & Lọc sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 4 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.*)

Hints (*Gợi ý*):
    - After logging in, use flutter_fill() to type into the search box
      (*Sau khi đăng nhập, dùng flutter_fill() để nhập vào ô tìm kiếm*)
    - Search box aria-label: "Tìm kiếm theo tên sách hoặc tác giả..."
    - Category filter aria-label: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    - Each book card has role="group" and aria-label containing book info
      (*Mỗi card sách có role="group" và aria-label chứa thông tin sách*)
    - Use login() helper from conftest.py to log in before testing
      (*Dùng login() helper từ conftest.py để đăng nhập trước khi test*)
"""
import os
from conftest import wait_for_flutter
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found 
    """
    pytest.skip("Not implemented — student must complete")


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' """
    login(page, test_config)

    flutter_fill(page, "Filter by category (e.g., Technology, Economics, etc.)", "Technology")
    wait_for_flutter(page, text="Technology")
    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    
    count = books.count()
    assert count > 0, "Error: No books found in the Technology category!"

    for i in range(count):
        aria_label = books.nth(i).get_attribute("aria-label")
        assert "Công nghệ" in aria_label, f"Error: Book {i+1} does not belong to the Technology category! (Aria-label: {aria_label})"


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name """
   
    login(page, test_config)
    
    flutter_fill(page, "Search by book title or author....", "Nguyễn Minh Đức")
    
    wait_for_flutter(page, text="Nguyễn Minh Đức")
    
    results_count = page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count()
    assert results_count > 0, "Error: No books by author Nguyễn Minh Đức were found.
"
