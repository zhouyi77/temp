import pytest
# 详细断言异常
def test_zero_division_long():
    with pytest.raises(ZeroDivisionError) as excinfo:
        var = 1 / 0

    # 断言异常类型 type
    assert excinfo.type == ZeroDivisionError
    # 断言异常 value 值
    assert "zero" in str(excinfo.value)

print('chongtu')


