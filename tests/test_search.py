"""
Search & Filter Tests (*Kiểm thử Tìm kiếm & Lọc sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 4 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    SCREENSHOT_DIR,
)


def smart_login(page, test_config):
    page.goto(test_config["base_url"])
    page.wait_for_timeout(3000)
    
    try:
        enable_flutter_semantics(page)
        page.wait_for_timeout(1000)
    except Exception:
        pass

    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    

    page.wait_for_timeout(3000)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found """
    smart_login(page, test_config)

    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Kiểm thử")
    page.wait_for_timeout(2000)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Kiểm thử phần mềm nhập môn" in sem_text

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc04_search_by_name.png"))


def test_search_book_no_results(page, test_config):
    """TC-05: Search book – no results found"""
    smart_login(page, test_config)

    flutter_fill(page, "TSearch by book title or author...", "stqa_non_existent_book_2026")
    page.wait_for_timeout(2000)

    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "No books found" in sem_text or "Borrow this book" not in sem_text

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc05_search_no_results.png"))


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category """
  
    smart_login(page, test_config)

    
    flutter_fill(page, "Filter by category (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    page.wait_for_timeout(2000)

   
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Kiểm thử phần mềm nhập môn" in sem_text

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc06_filter_by_category.png"))


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name """
    
    smart_login(page, test_config)

    # Act: Gõ tên tác giả "Lê Thị Hoa" (Dữ liệu thật có trên màn hình của bạn) vào ô tìm kiếm
    flutter_fill(page, "Search by book title or author...", "Lê Thị Hoa")
    page.wait_for_timeout(2000)

    # Assert: Kiểm tra xem sách của tác giả này có hiển thị đầy đủ không
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Kiểm thử phần mềm nhập môn" in sem_text

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc07_search_by_author.png"))
