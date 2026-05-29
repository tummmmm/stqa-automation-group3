import os
import time
import pytest
from playwright.sync_api import expect
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter
)

def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found"""
    login(page, test_config)
    
    search_box_label = "Tìm kiếm theo tên sách hoặc tác giả..."
    keyword = "Flutter"
    
    flutter_fill(page, search_box_label, keyword)
    page.keyboard.press("Enter")
    
    # ASSERT: Chờ card sách chứa từ khóa xuất hiện công khai trên UI
    matching_books = page.locator('flt-semantics[role="group"][aria-label*="Flutter"]')
    expect(matching_books.first).to_be_visible()


def test_search_book_not_found(page, test_config):
    """TC-05: Search book by name – no results found"""
    login(page, test_config)
    
    search_box_label = "Tìm kiếm theo tên sách hoặc tác giả..."
    invalid_keyword = "Sách này chắc chắn không tồn tại 123456"
    
    flutter_fill(page, search_box_label, invalid_keyword)
    page.keyboard.press("Enter")
    
    # ASSERT: Đảm bảo không có card sách nào hiển thị trên màn hình
    all_book_cards = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    expect(all_book_cards).to_have_count(0)


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category"""
    login(page, test_config)
    
    category_label = "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    selected_category = "Công nghệ"
    
    flutter_fill(page, category_label, selected_category)
    page.keyboard.press("Enter")
    
    # ASSERT MẠNH: Định vị tất cả sách hiển thị sai thể loại (không chứa chữ "Công nghệ")
    wrong_category_books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]:not([aria-label*="Công nghệ"])')
    
    # Ép Playwright chờ đến khi số lượng sách sai thể loại giảm về bằng 0 (Đã lọc xong)
    expect(wrong_category_books).to_have_count(0)
    
    # Đảm bảo có ít nhất 1 cuốn sách đúng thể loại hiển thị công khai
    matching_books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"][aria-label*="Công nghệ"]')
    expect(matching_books.first).to_be_visible()


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name"""
    login(page, test_config)
    
    search_box_label = "Tìm kiếm theo tên sách hoặc tác giả..."
    author_name = "Nguyễn Minh Đức"
    
    flutter_fill(page, search_box_label, author_name)
    page.keyboard.press("Enter")
    
    # ASSERT: Tự động chờ card sách có chứa tên tác giả xuất hiện
    matching_author_books = page.locator(f'flt-semantics[role="group"][aria-label*="{author_name}"]')
    expect(matching_author_books.first).to_be_visible()