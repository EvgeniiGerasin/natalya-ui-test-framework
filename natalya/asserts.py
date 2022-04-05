import allure


class Assert:

    _not = False

    @classmethod
    def not_be(cls):
        cls._not = True
        return Assert

    @classmethod
    def compare(
        cls,
        variable_first,
        comparison_sign: str,
        variable_second,
        text_error: str,
    ):
        with allure.step(
            'Assertion: comparing "{}" {} "{}"'.format(
                variable_first, comparison_sign, variable_second,
            )
        ):
            if comparison_sign == '=' or comparison_sign == '==':
                assert variable_first == variable_second, text_error
            elif comparison_sign == '!=':
                assert variable_first != variable_second, text_error
            elif comparison_sign == '>':
                assert variable_first > variable_second, text_error
            elif comparison_sign == '<':
                assert variable_first < variable_second, text_error
            elif comparison_sign == '>=':
                assert variable_first >= variable_second, text_error
            elif comparison_sign == '<=':
                assert variable_first <= variable_second, text_error
            else:
                raise ValueError(
                    'Unknown comparison sign {}'
                    .format(comparison_sign)
                )

    @classmethod
    def contains(
        cls,
        variable_what,
        variable_where,
        text_error: str,
    ) -> None:
        """Checking the content in something (a in b)

        :Args:
            variable_what(any): what should be contained
            variable_where(any): where it should be contained
            text_error(str): error text
        """
        if cls._not:
            cls._not = False
            with allure.step(
                'Assertion: not contains "{}" in "{}"'.format(
                    variable_what, variable_where
                )
            ):
                try:
                    assert variable_what not in variable_where
                except:
                    assert False, text_error
        else:
            with allure.step(
                'Assertion: contains "{}" in "{}"'.format(
                    variable_what, variable_where
                )
            ):
                try:
                    assert variable_what in variable_where
                except:
                    assert False, text_error
