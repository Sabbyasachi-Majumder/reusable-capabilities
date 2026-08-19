"""
Provides reusable interactive option
selection for manual testing and
E2E execution flows.
"""


class SelectionHelper:
    """
    Provides reusable option selection.
    """

    # Prompts for an option selection.
    @staticmethod
    def select_option(
        title: str,
        options: list[str],
    ) -> str | None:

        while True:

            print(
                f"\n{title}"
            )

            print()

            print(
                "0. Exit"
            )

            print()

            for (
                index,
                option,
            ) in enumerate(
                options,
                start=1,
            ):

                print(
                    f"{index}. {option}"
                )

            selection = input(
                "\nSelection: "
            )

            try:

                selection = int(
                    selection
                )

            except ValueError:

                print(
                    "\nInvalid selection."
                )

                continue

            if selection == 0:

                return None

            if (
                1
                <= selection
                <= len(options)
            ):

                return options[
                    selection - 1
                ]

            print(
                "\nInvalid selection."
            )
