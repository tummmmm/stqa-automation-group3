
import os
import pytest

from conftest import (
    enable_flutter_semantics,
    flutter_fill,
    flutter_click_button,
    wait_for_flutter,
    SCREENSHOT_DIR,
)


def test_login_success(page, test_config):
    """TC-01: Login success with valid credentials"""

    # Arrange
    page.goto(
        test_config["base_url"],
        wait_until="networkidle",
        timeout=60000
    )

    enable_flutter_semantics(page)

    # Act
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", test_config["password"])
    flutter_click_button(page, "Đăng nhập")

    # Wait
    wait_for_flutter(page, text="Đăng xuất")

    # Screenshot
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "login_success.png"
        )
    )

    # Assert
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    has_user_name = (
        test_config["display_name"] in sem_text
    )

    has_logout = (
        "Đăng xuất" in sem_text
        or "Logout" in sem_text
    )

    assert has_user_name or has_logout


def test_login_fail_wrong_password(page, test_config):
    """TC-02: Login fail – wrong password"""

    # Arrange
    page.goto(
        test_config["base_url"],
        wait_until="networkidle",
        timeout=60000
    )

    enable_flutter_semantics(page)

    # Act
    flutter_fill(page, "Email", test_config["email"])
    flutter_fill(page, "Mật khẩu", "wrongpassword")
    flutter_click_button(page, "Đăng nhập")

    # Wait
    wait_for_flutter(
        page,
        text="Mật khẩu không đúng"
    )

    # Screenshot
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "login_fail_wrong_password.png"
        )
    )

    # Assert
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    assert "Mật khẩu không đúng" in sem_text


@pytest.mark.parametrize(
    "email, password",
    [
        ("", ""),
    ]
)
def test_login_fail_empty_fields(
    page,
    test_config,
    email,
    password
):
    """TC-03: Login fail – empty fields"""

    # Arrange
    page.goto(
        test_config["base_url"],
        wait_until="networkidle",
        timeout=60000
    )

    enable_flutter_semantics(page)

    # Act
    flutter_fill(page, "Email", email)
    flutter_fill(page, "Mật khẩu", password)
    flutter_click_button(page, "Đăng nhập")

    # Wait
    wait_for_flutter(
        page,
        text="Vui lòng nhập email và mật khẩu"
    )

    # Screenshot
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "login_fail_empty_fields.png"
        )
    )

    # Assert
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    assert (
        "Vui lòng nhập email và mật khẩu"
        in sem_text
    )


