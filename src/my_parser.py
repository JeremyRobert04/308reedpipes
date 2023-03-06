import sys
import src.my_print as Print

# USAGE
#   ./308reedpipes r0 r5 r10 r15 r20 n
# DESCRIPTION
#   r0 radius (in cm) of pipe at the 0cm abscissa
#   r5 radius (in cm) of pipe at the 5cm abscissa
#   r10 radius (in cm) of pipe at the 10cm abscissa
#   r15 radius (in cm) of pipe at the 15cm abscissa
#   r20 radius (in cm) of pipe at the 20cm abscissa
#   n number of points needed to display the radius

def print_help() -> None:
    """display Help to start the programs

    Returns:
        None: No return
    """

    print("USAGE")
    print("\t./308reedpipes r0 r5 r10 r15 r20 n\n")
    print("DESCRIPTION")
    print("\tr0\t\tradius (in cm) of pipe at the 0cm abscissa")
    print("\tr5\t\tradius (in cm) of pipe at the 5cm abscissa")
    print("\tr10\t\tradius (in cm) of pipe at the 10cm abscissa")
    print("\tr15\t\tradius (in cm) of pipe at the 15cm abscissa")
    print("\tr20\t\tradius (in cm) of pipe at the 20cm abscissa")
    print("\tn\t\tnumber of points needed to display the radius")
    sys.exit(0)

def safeFloatConverter(number: str) -> float | None:
        """Safely convert a string to it corresponding number

        Args:
            number (str): string representing the number

        Returns:
            float | None: the number (float) or None if failed
        """
        try:
            result = float(number)
            return result
        except:
            return None

class MyParser():
    def __init__(self, args = []) -> None:
        self.args = [x for ind, x in enumerate(args) if ind != 0]
        self.parsed_args = []
        self.parsed_dict = {
            'r0': None,
            'r5': None,
            'r10': None,
            'r15': None,
            'r20': None,
            'n': None
        }
        self.check_cmd()

    def get_parsed_args(self) -> dict:
        """get the parsed args from class

        Returns:
            dict: dictionnary of parsed input
        """
        return self.parsed_dict

    def check_for_help(self) -> None:
        """check if -h or --help do display help
        """
        if self.args[0] in ("-h", "--help"):
            print_help()

    def check_cmd(self):
        if not self.args:
            Print.print_error("Missing parameters\n\tDo -h to see help.")
        self.check_for_help()
        if len(self.args) < 6:
            Print.print_error(f"Not enough arguments. Got {len(self.args)} but expected 6")
        if len(self.args) > 6:
            Print.print_error(f"Too many arguments. Got {len(self.args)} but expected 6")
        self.parsed_args = [ safeFloatConverter(value) for value in self.args]
        if any(value is None for value in self.parsed_args):
            Print.print_error("Parameters should only contains positive numbers.")
        if not all(i > 0 for i in self.parsed_args):
            Print.print_error("Parameters should only contains positive numbers.")
        for arg, index in zip(self.parsed_dict, range(0, len(self.parsed_args))):
            self.parsed_dict[arg] = self.parsed_args[index]
        self.parsed_dict['n'] = int(self.parsed_dict['n'])