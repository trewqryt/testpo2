import pytest
from student_result import get_result


# --- Позитивные и граничные случаи ---
@pytest.mark.parametrize(
    "score, attendance, expected",
    [
        # Отлично
        (95, 85, "Отлично"),
        (90, 80, "Отлично"),
        (100, 100, "Отлично"),
        (90, 100, "Отлично"),
        (100, 80, "Отлично"),

        # Хорошо
        (89, 80, "Хорошо"),
        (75, 75, "Хорошо"),
        (70, 70, "Хорошо"),
        (89, 70, "Хорошо"),
        (70, 79, "Хорошо"),

        # Зачёт
        (69, 70, "Зачёт"),
        (60, 65, "Зачёт"),
        (50, 60, "Зачёт"),
        (69, 60, "Зачёт"),
        (50, 69, "Зачёт"),

        # Незачёт
        (49, 60, "Незачёт"),
        (80, 59, "Незачёт"),
        (0, 0, "Незачёт"),
        (49, 100, "Незачёт"),
        (100, 59, "Незачёт"),
        (69, 59, "Незачёт"),
        (49, 69, "Незачёт"),

        # Некорректные диапазоны
        (-1, 80, "Некорректный балл"),
        (101, 80, "Некорректный балл"),
        (0, -1, "Некорректная посещаемость"),
        (50, 101, "Некорректная посещаемость"),
        (-5, -10, "Некорректный балл"),
    ],
)
def test_get_result_valid_and_boundary(score, attendance, expected):
    assert get_result(score, attendance) == expected


# --- Невалидные типы ---
@pytest.mark.parametrize(
    "score, attendance",
    [
        ("90", 80),
        (90, "80"),
        (None, 80),
        (90, None),
        ([90], 80),
        (90, [80]),
        ({"score": 90}, 80),
        (90.5, "80"),
    ],
)
def test_get_result_invalid_type(score, attendance):
    with pytest.raises(TypeError) as exc_info:
        get_result(score, attendance)
    assert "должны быть числом" in str(exc_info.value) or "должна быть числом" in str(exc_info.value)