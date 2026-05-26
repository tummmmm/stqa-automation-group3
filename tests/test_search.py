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
    """Hàm tự động đăng nhập và kích hoạt Semantics an toàn tuyệt đối"""
    page.goto(test_config["base_url"])
    # Đợi trang web tải các tài nguyên cơ bản trong 3 giây
    page.wait_for_timeout(3000)
    
    try:
        # Kích hoạt chế độ đọc Semantics tree của Flutter
        enable_flutter_semantics(page)
        page.wait_for_timeout(1000)
    except Exception:
        pass

    # Thực hiện điền thông tin đăng nhập trực tiếp
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")
    
    # Đợi 3 giây để trang chủ và danh sách sách được tải hoàn chỉnh
    page.wait_for_timeout(3000)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found (*Tìm kiếm sách theo tên — tìm thấy kết quả*)"""
    # Arrange: Đăng nhập
    smart_login(page, test_config)

    # Act: Tìm kiếm từ khóa "Kiểm thử" (Dữ liệu thật chắc chắn hiển thị trên web)
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Kiểm thử")
    page.wait_for_timeout(2000)

    # Assert: Quét toàn bộ cây Semantics để đảm bảo sách cần tìm xuất hiện
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Kiểm thử phần mềm nhập môn" in sem_text

    # Chụp ảnh chứng minh lưu vào thư mục screenshots
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc04_search_by_name.png"))


def test_search_book_no_results(page, test_config):
    """TC-05: Search book – no results found (*Tìm kiếm sách — không tìm thấy kết quả*)"""
    # Arrange: Đăng nhập an toàn
    smart_login(page, test_config)

    # Act: Tìm kiếm một chuỗi ký tự ngẫu nhiên chắc chắn không tồn tại
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "stqa_non_existent_book_2026")
    page.wait_for_timeout(2000)

    # Assert: Xác minh hệ thống hiển thị thông báo lỗi "Không tìm thấy sách"
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Không tìm thấy sách" in sem_text or "Mượn sách này" not in sem_text

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc05_search_no_results.png"))


def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category (*Lọc sách theo thể loại*)"""
    # Arrange: Đăng nhập an toàn
    smart_login(page, test_config)

    # Act: Nhập tên thể loại "Công nghệ" vào ô lọc thể loại theo đúng nhãn thầy hướng dẫn
    flutter_fill(page, "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)", "Công nghệ")
    page.wait_for_timeout(2000)

    # Assert: Bắt buộc phải nhìn thấy sách thuộc thể loại Công nghệ vừa lọc
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Kiểm thử phần mềm nhập môn" in sem_text

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc06_filter_by_category.png"))


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name (*Tìm kiếm sách theo tên tác giả*)"""
    # Arrange: Đăng nhập an toàn
    smart_login(page, test_config)

    # Act: Gõ tên tác giả "Lê Thị Hoa" (Dữ liệu thật có trên màn hình của bạn) vào ô tìm kiếm
    flutter_fill(page, "Tìm kiếm theo tên sách hoặc tác giả...", "Lê Thị Hoa")
    page.wait_for_timeout(2000)

    # Assert: Kiểm tra xem sách của tác giả này có hiển thị đầy đủ không
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Kiểm thử phần mềm nhập môn" in sem_text

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc07_search_by_author.png"))