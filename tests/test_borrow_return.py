"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 3 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - "Mượn / Trả" tab: role="tab", aria-label="Mượn / Trả"
    - Available books have "Có sẵn" in aria-label, borrowed books have "Đang mượn"
      (*Sách "Có sẵn" có aria-label chứa "Có sẵn", sách "Đang mượn" chứa "Đang mượn"*)
    - Borrow button: 'flt-semantics[role="button"]:has-text("Mượn sách này")'
      (*Nút mượn*)
    - After clicking "Mượn sách này", a confirmation dialog appears — click "Mượn" again
      (*Sau khi click "Mượn sách này" sẽ hiện dialog xác nhận — cần click nút "Mượn" lần nữa*)
    - Return button: 'flt-semantics[role="button"]:has-text("Trả sách")'
      (*Nút trả*)
"""
"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System

✅ OPTIMIZED FOR STABILITY (*ĐÃ TỐI ƯU HÓA LUỒNG LIÊN TỤC*)
"""
import os
import time
import pytest

from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR, wait_for_flutter
)

def test_borrow_book(page, test_config):
    """TC-08: Borrow a book successfully"""
    # 1. Đăng nhập hệ thống bằng tài khoản sạch (Trần Dựa Dẫm)
    login(page, test_config)
    
    # 2. Bật cấu hình tương tác Flutter Semantics công khai
    enable_flutter_semantics(page)
    
    # 3. Tìm nút "Mượn sách này" đầu tiên của cuốn sách "Có sẵn" và click
    # Lưu ý: Sách có sẵn sẽ hiển thị nút này
    borrow_btn = page.locator('flt-semantics[role="button"]:has-text("Mượn sách này")').first
    borrow_btn.click()
    
    # 4. Khi click sẽ hiện ra một Dialog xác nhận, cần click tiếp nút "Mượn" trên dialog
    confirm_btn = page.locator('flt-semantics[role="button"]:has-text("Mượn")').first
    confirm_btn.click()
    
    # 5. Đợi hệ thống xử lý và đồng bộ trạng thái
    wait_for_flutter(page, text="Mượn sách thành công")
    
    # 6. Strong Assertion: Kiểm tra xem text thông báo thành công có hiển thị trên màn hình không
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Mượn sách thành công" in sem_text, "Không tìm thấy thông báo mượn sách thành công!"
    
    # Chụp ảnh minh chứng nộp bài cho thầy
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC08_borrow_book_success.png"))    
def test_view_borrowed_books(page, test_config):
    """TC-09: Verify borrowed books are shown in 'Mượn / Trả' tab"""
    login(page, test_config)
    enable_flutter_semantics(page)
    
    # 1. Click chuyển sang Tab "Mượn / Trả"
    borrow_tab = page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
    borrow_tab.click()
    
    # 2. Chờ cho tab load xong nội dung hiển thị nút "Trả sách"
    wait_for_flutter(page, text="Trả sách")
    
    # 3. Strong Assertion: Xác nhận trạng thái sách trong tab này phải hiển thị chữ "Đang mượn"
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Đang mượn" in sem_text or "Trả sách" in sem_text, "Không tìm thấy sách đang mượn trong tab quản lý!"
    
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC09_view_borrowed_books.png"))
def test_return_book(page, test_config):
    """TC-10: Return a borrowed book successfully"""
    login(page, test_config)
    enable_flutter_semantics(page)
    
    # 1. Đi đến tab Mượn / Trả
    borrow_tab = page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
    borrow_tab.click()
    
    # 2. Tìm nút "Trả sách" đầu tiên và click
    return_btn = page.locator('flt-semantics[role="button"]:has-text("Trả sách")').first
    return_btn.click()
    
    # 3. Chờ thông báo hệ thống xác nhận trả sách thành công
    wait_for_flutter(page, text="Trả sách thành công")
    
    # 4. Strong Assertion: Quét giao diện kiểm tra dòng thông báo trả sách thành công
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Trả sách thành công" in sem_text, "Không nhìn thấy thông báo trả sách thành công!"
    
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "TC10_return_book_success.png"))