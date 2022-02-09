class WrongPowerArguments(Exception):
    def __init__(
        self,
        alpha: float,
        power: float,
        total_observations: int,
    ):
        args = [alpha, power, total_observations]
        args_msg = self._list_args_msg(*args)

        num_nones = args.count(None)
        if num_nones == 0:
            message = (
                "All arguments were provided. Exactly one of "
                "alpha, power, or total_observations must be None. "
                f"Arguments: {args_msg}"
            )
        elif num_nones > 1:
            message = (
                "More than 1 argument was provided. Exactly one of "
                "alpha, power, or total_observations must be None. "
                f"Arguments: {args_msg}"
            )
        else:
            pass  # Should never get here

        super().__init__(message)

    def _list_args_msg(
        self,
        alpha: float,
        power: float,
        total_observations: int,
    ) -> str:
        msg = (
            f"alpha = {alpha}, power = {power}, "
            f"total_observations = {total_observations}."
        )
        return msg
