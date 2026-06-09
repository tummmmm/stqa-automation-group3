"""
Bonus Tests (B1) — Advanced Features & Edge Cases
"""
import os
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    wait_for_flutter, SCREENSHOT_DIR
)
#TC-13: Thêm thành viên mới thành công (Quyền Thủ thư - REQ-07)
def test_librarian_add_member_success(page, test_config):
    """TC-13 (Bonus B1): Librarian adds a new member successfully (REQ-07)"""
    # Đăng nhập bằng tài khoản thủ thư trực tiếp
    page.goto(test_config["base_url"], wait_until="networkidle")
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")
    enable_flutter_semantics(page)

    # Vào tab Thành viên
    page.locator('flt-semantics[role="tab"][aria-label="Thành viên"]').click()
    wait_for_flutter(page, text="Thêm thành viên")

    # Điền thông tin
    flutter_fill(page, "Họ tên", "Nguyễn Văn Thử Nghiệm")
    flutter_fill(page, "Email", "test.member@stqa.com")
    flutter_fill(page, "Số điện thoại", "0987654321")
    flutter_click_button(page, "Thêm thành viên")

    # Đợi thông báo thành công hoặc kiểm tra danh sách hiển thị
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc13_add_member_success.png"))

#TC-14: Thủ thư kiểm tra sách quá hạn thành công (REQ-06)
def test_librarian_check_overdue(page, test_config):
    """TC-14 (Bonus B1): Librarian triggers overdue checking process (REQ-06)"""
    page.goto(test_config["base_url"], wait_until="networkidle")
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Kiểm tra quá hạn")

    # Nhấn nút kiểm tra quá hạn
    flutter_click_button(page, "Kiểm tra quá hạn")
    page.wait_for_timeout(1000) # Thao tác nội bộ xử lý hệ thống

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc14_check_overdue_triggered.png"))

#TC-15: Kiểm thử email không hợp lệ khi tạo thành viên (BVA / Negative - REQ-07)
def test_add_member_invalid_email(page, test_config):
    """TC-15 (Bonus B1): Add member fail with invalid email format (REQ-07 Domain dot rule)"""
    page.goto(test_config["base_url"], wait_until="networkidle")
    enable_flutter_semantics(page)
    flutter_fill(page, "Email", "librarian@library.com")
    flutter_fill(page, "Mật khẩu", "admin123")
    flutter_click_button(page, "Đăng nhập")
    wait_for_flutter(page, text="Đăng xuất")
    enable_flutter_semantics(page)

    page.locator('flt-semantics[role="tab"][aria-label="Thành viên"]').click()
    wait_for_flutter(page, text="Thêm thành viên")

    flutter_fill(page, "Họ tên", "Lỗi Email")
    # Định dạng không hợp lệ theo SRS (không có dấu chấm ở domain)
    flutter_fill(page, "Email", "bad_email@domain") 
    flutter_fill(page, "Số điện thoại", "0123456789")
    flutter_click_button(page, "Thêm thành viên")

    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc15_invalid_email_format.png"))