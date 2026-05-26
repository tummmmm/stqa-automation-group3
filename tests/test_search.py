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
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search keyword "Flutter" → verify Flutter books appear in results.
        (*Đăng nhập → tìm kiếm từ khóa "Flutter" → kiểm tra có sách Flutter trong kết quả.*)

    Hints (*Gợi ý*):
        - login(page, test_config)
        - flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Flutter")
        - Verify: page.locator('flt-semantics[aria-label*="Flutter"]').count() > 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_search_book_no_result(page, test_config):
    """TC-05: Search book – no results (*Tìm kiếm sách — không có kết quả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → search a non-existent keyword (e.g. "xyz_khong_ton_tai_12345")
        → verify no books are displayed.
        (*Đăng nhập → tìm kiếm từ khóa không tồn tại → kiểm tra không có sách nào hiển thị.*)

    Hints (*Gợi ý*):
        - Verify: page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]').count() == 0
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ' (*Lọc sách theo thể loại 'Công nghệ'*)"""
    # 1. Đăng nhập vào hệ thống trước khi thực hiện test
    login(page, test_config)
    
    # 2. Nhập chữ "Công nghệ" vào ô lọc thể loại theo đúng aria-label gợi ý
    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    
    # 3. Đợi một chút để Flutter Web cập nhật danh sách thông minh
    wait_for_flutter(page, text="Công nghệ")
    
    # 4. Lấy danh sách tất cả các card sách đang hiển thị trên màn hình
    books = page.locator('flt-semantics[role="group"][aria-label*="Mã: BOOK"]')
    
    # Kiểm tra xem có cuốn sách nào xuất hiện không (Strong Oracle)
    count = books.count()
    assert count > 0, "Lỗi: Không tìm thấy cuốn sách nào thuộc thể loại Công nghệ!"
    
    # 5. Vòng lặp kiểm tra gắt gao từng card xem có đúng chứa chữ "Công nghệ" không
    for i in range(count):
        aria_label = books.nth(i).get_attribute("aria-label")
        assert "Công nghệ" in aria_label, f"Lỗi: Cuốn sách thứ {i+1} không thuộc thể loại Công nghệ! (Aria-label: {aria_label})"


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)"""
    # 1. Đăng nhập vào hệ thống
    login(page, test_config)
    
    # 2. Nhập tên tác giả "Nguyễn Minh Đức" vào ô tìm kiếm theo đúng aria-label
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Nguyễn Minh Đức")
    
    # 3. Đợi Flutter Web xử lý kết quả tìm kiếm thông minh
    wait_for_flutter(page, text="Nguyễn Minh Đức")
    
    # 4. Kiểm tra xem số lượng kết quả tìm thấy có lớn hơn 0 hay không (Strong Oracle)
    results_count = page.locator('flt-semantics[aria-label*="Nguyễn Minh Đức"]').count()
    assert results_count > 0, "Lỗi: Không tìm thấy bất kỳ sách nào của tác giả Nguyễn Minh Đức!"
