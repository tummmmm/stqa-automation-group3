"""
Logout & Language Tests — Library Book Borrowing System
"""

import os
import pytest
from conftest import (
    enable_flutter_semantics,
    flutter_fill,
    flutter_click_button,
    SCREENSHOT_DIR,
)


def smart_login(page, test_config):
    """Login an toàn cho Flutter Web"""
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


def test_logout(page, test_config):
    """
    TC-11: Logout success
    Đăng nhập → Đăng xuất → quay về màn hình login
    """
    # Arrange
    smart_login(page, test_config)

    # Act
    flutter_click_button(page, "Đăng xuất")
    page.wait_for_timeout(3000)

    try:
        enable_flutter_semantics(page)
    except Exception:
        pass

    # Assert (Strong Oracle - Khớp chuẩn xác dữ liệu thật trên web mẫu)
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Tài khoản thử nghiệm:" in sem_text

    # Screenshot
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc11_logout_success.png"))


def test_switch_language_to_english(page, test_config):
    """
    TC-12: Switch language to English
    Đăng nhập → click EN → giao diện chuyển English
    """
    # Arrange
    smart_login(page, test_config)

    # Act
    flutter_click_button(page, "EN")
    page.wait_for_timeout(2500)

    try:
        enable_flutter_semantics(page)
    except Exception:
        pass

    # Assert (Strong Oracle)
    sem_text = " ".join(page.locator("flt-semantics").all_text_contents())
    assert "Logout" in sem_text or "Available categories" in sem_text

    # Screenshot
    page.screenshot(path=os.path.join(SCREENSHOT_DIR, "tc12_switch_language_en.png"))