"""
Provides terminal publishing functionality.

Responsible for publishing reporting
content to the terminal.
"""


class TerminalDestination:
    """
    Terminal reporting destination.
    """

    # Publishes content to the terminal.
    def publish(
        self,
        content: str,
    ) -> None:

        print(
            content
        )

    # Runs the destination manually.
    def manual_run(
        self,
    ) -> None:

        print(
            "\nTerminal Session Started"
        )

        while True:

            print(
                "\n1. Publish Content"
            )

            print(
                "0. Exit"
            )

            selection = input(
                "\nSelection: "
            )

            if selection == "0":

                print(
                    "\nTerminal Session Ended"
                )

                break

            if selection != "1":

                print(
                    "\nInvalid selection."
                )

                continue

            content = input(
                "\nContent: "
            )

            self.publish(
                content
            )


if __name__ == "__main__":

    TerminalDestination().manual_run()
