import sys

class CubicSplines():
    def __init__(self, args):
        self.parameters = args
        self.result = [None for i in range(self.parameters['n'])]
        self.abscissa = [0, 5, 10, 15, 20]
        self.ordinate = [value for key, value in args.items() if key != 'n']
        self.vector = [0, None, None, None, 0]

    def calculate_abscissa_step(self, i: int) -> float | int:
        """calculate the step between points ex: 0.0 - 2.0 - 4.0 ... 20.0 based on parameters how many 'n'

        Args:
            i (int): at which step we are looking for

        Returns:
            float | int: result of abscissa (ex: 1.7 - 3.3 ect...)
        """
        return self.abscissa[-1] / (self.parameters['n'] - 1) * i

    def print_result(self) -> None:
        """Print the final result
        """
        print("vector result: [{:.1f}, {:.1f}, {:.1f}, {:.1f}, {:.1f}]".format(
            self.vector[0], self.vector[1], self.vector[2], self.vector[3], self.vector[4],
        ))
        for i in range(self.parameters['n']):
            print("abscissa: {:.1f} cm\tradius: {:.1f} cm".format(
                self.calculate_abscissa_step(i), self.result[i]))

    def find_vector(self) -> None:
        """find the second derivative
        """
        buff = []
        for i in range(1, len(self.abscissa) - 1):
            buff.append(6 * (self.ordinate[i + 1] - 2 * self.ordinate[i] + self.ordinate[i - 1]) / ((self.abscissa[i + 1] - self.abscissa[i - 1]) * (self.abscissa[i + 1] - self.abscissa[i])))
        self.vector[2] = (buff[1] - (buff[0] + buff[2]) / 4) * 4 / 7
        self.vector[1] = buff[0] / 2 - 0.25 * self.vector[2]
        self.vector[3] = buff[2] / 2 - 0.25 * self.vector[2]

    def calculate(self) -> None:
        self.find_vector()
        for i in range(self.parameters['n']):
            abscissa_step = self.calculate_abscissa_step(i)
            fi = int((abscissa_step - 0.01) / 5) + 1
            hi = self.abscissa[i] - self.abscissa[i - 1] if i > 0 and i < len(self.abscissa) - 1 else 5
            self.result[i] = (-self.vector[fi - 1] / (6 * hi) * pow(abscissa_step - self.abscissa[fi], 3) \
                + self.vector[fi] / (6 * hi) * pow(abscissa_step - self.abscissa[fi - 1], 3) \
                - (
                    self.ordinate[fi - 1] / hi - hi * self.vector[fi - 1] / 6
                ) * (abscissa_step - self.abscissa[fi]) \
                + (
                    self.ordinate[fi] / hi - hi / 6 * self.vector[fi]
                ) * (abscissa_step - self.abscissa[fi - 1])
            )